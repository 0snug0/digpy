from typing import List, Dict, Union

class Result:
    def __init__(self, status_code: int, message: str = '', res: List[Dict] = None):
        """
        Model for result of an API call
        :param status_code: The HTTP status code of the response
        :param message: The HTTP status message of the response
        :param res: The JSON response body
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.res = res if res else []

class Page:
    def __init__(self, total: int, prev: str, next: str):
        """
        Model for the results of Events pagination
        :param total: total number of events
        :param prev: link to previous page
        :param next: link to next page
        """
        self.total = total
        self.prev = prev
        self.next = next

class Event:
    def __init__():
        # TODO
        pass

class Events:
    def __init__(self, data: List[Dict], page: Union[Page, Dict]):
        """
        Model for the results of Events
        :param data: where events are stored
        :param page: where pagination data is stored
        """
        self.data = data if data else []
        self.page = Page(**page) if isinstance(page, dict) else page
