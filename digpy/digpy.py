import requests, yaml, logging
from typing import List, Dict
from json import JSONDecodeError
from models.models import Result
from exceptions import DigException

class Config(object):
    """
    Contains the configuration for the digpy client.
    Optional environement variables, configs, or arguments can be used to
    """
    def __init__(self, config_file=None):
        # self.config_file = "~/.digpy/config.yml"
        self.config_file = "./config.yml"
        with open(self.config_file, "r") as f:
            self.config = yaml.safe_load(f)
            self.current_env = self.config["current-environment"]
            self.current_product = self.config["current-product"]
            
            for item in self.config["environments"]:
                if item['name'] == self.current_env:
                    self.secure_token = item['secure']['token']
                    self.monitor_token = item['monitor']['token']
                    self.url = item['url']
       
class ApiClient(object):
    def __init__(self, config=None, logger: logging.Logger = None):
        """
        Constructor for ApiClient
        :param config: config object from config.yaml
        :param logger: (optional) If your app has a logger, pass it in here.
        """
        self._logger = logger or logging.getLogger(__name__)
        self.config = Config()
        self.url = self.config.url
        self.headers = {'Authorization': f'Bearer {self.config.secure_token}'}
    
    def _do(self, http_method: str, path: str, params: Dict = None, data: Dict = None) -> Result:
        """
        Private method for get(), post(), delete(), etc.
        :param http_method: GET, POST, DELETE, etc.
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :params data: (optional) A dict of data to include in the request body
        :return: a Result object
        """
        logger: logging.Logger = None
        url = self.url + path
        log_line_pre = f"method={http_method}, url={url}, params={params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))

        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            # self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=url, headers=self.headers, params=params, json=data)
        except requests.exceptions.RequestException as e:
            # self._logger.error(msg=(str(e)))
            raise DigException("Request failed") from e
        
        # Deserialize JSON output to Python object, or return failed Result on exception
        try:
            res = response.json()
        except (ValueError, JSONDecodeError) as e:
            # self._logger.error(msg=log_line_post.format(False, None, e))
            raise DigException("Bad JSON in response") from e
        
        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        # log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            # self._logger.debug(msg=log_line)
            return Result(status_code=response.status_code, message=response.reason, res=res)
        # self._logger.error(msg=log_line)
        raise DigException(res, response.request.url, response.request.headers, response.request.body)
    
    def get(self, path: str, params: Dict = None) -> Result:
        """
        Perform a GET request to the API
        :param http_method: The HTTP method to use, e.g. "GET"
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :return: a Result object
        """
        return self._do(http_method="GET", path=path, params=params)
    
    def post(self, path: str, params: Dict = None, data: Dict = None) -> Result:
        """
        Perform a POST request to the API
        :param http_method: The HTTP method to use, e.g. "POST"
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :params data: (optional) A dict of data to include in the request body
        :return: a Result object
        """
        return self._do(http_method="POST", path=path, params=params, data=data)
    
    def put(self, path: str, params: Dict = None, data: Dict = None) -> Result:
        """
        Perform a PUT request to the API
        :param http_method: The HTTP method to use, e.g. "PUT"
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :params data: (optional) A dict of data to include in the request body
        :return: a Result object        
        """
        return self._do(http_method="PUT", path=path, params=params, data=data)
    
    def delete(self, path: str, params: Dict = None, data: Dict = None) -> Result:
        """
        Perform a DELETE request to the API
        :param http_method: The HTTP method to use, e.g. "DELETE"
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :params data: (optional) A dict of data to include in the request body
        :return: a Result object
        """
        return self._do(http_method="DELETE", path=path, params=params, data=data)
    
    def patch(self, path: str, params: Dict = None, data: Dict = None) -> Result:
        """
        Perform a PATCH request to the API
        :param http_method: The HTTP method to use, e.g. "PATCH"
        :param path: The path to the resource, e.g. "/api/users/me"
        :params params: (optional) A dict of query parameters to include in the request
        :params data: (optional) A dict of data to include in the request body
        :return: a Result object
        """
        return self._do(http_method="PATCH", path=path, params=params, data=data)





if __name__ == "__main__":
  client = ApiClient()
  me = client.get("/api/users/me")
  print(me.res)

#   events = client.get("/api/v1/secureEvents", params={"limit": 50})
#   for event in events:
#       print(event)