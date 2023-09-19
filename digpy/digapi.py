import logging, time
from typing import List, Dict
import urllib.parse
import utils
from digpy import ApiClient
from models.models import *
from exceptions import DigException
from models.secureevents import SecureEvents

class DigApi:
    def __init__(self):
        self.client = ApiClient(logger=logging.getLogger(__name__))

    def get_me(self):
        """
        Get the current user
        :return: a Result object
        """
        request = self.client.get(path="/api/users/me")
        return request.res

    def _get_secure_events(self, filter: str = '', limit: int = 100, time_from: str = '-1d', time_to: str = 'now', cursor: str = None):
        """
        Private method for all secure events, including auditTrail and originator in benchmarks, compliance, cloudsec, use get_secure_events() instead for filtered results
        :param filter: (optional) The filter to apply to the query, default is None
        :param limit: (optional) The maximum number of results to return, default 100
        :param time_from: (optional) The start time of the query, default is 1 day
        :param time_to: (optional) The end time of the query, default is now
        :param cursor: (optional) The cursor to use for pagination, default is None
        :return: a Result object
        """
        if time_to == 'now':
            to_ = time.time_ns()
        else:
            to = time.time_ns() + utils.convert_to_nanoseconds(time_to)# Need to get time in ns from time_to
        from_ = to_ + utils.convert_to_nanoseconds(time_from) # 1 day
        self.params = {"limit": limit, "from": from_, "to": to_}
        request = self.client.get(path=f'/api/v1/secureEvents?{filter}', params=self.params)
        result = Events(**request.res)
        return result

    def get_secure_events(self, filter: str = '', limit: int = 100, time_from: str = '-1d', time_to: str = 'now', cursor: str = None):
        """
        Get secure events, excluding auditTrail and originator in benchmarks, compliance, cloudsec, as you would get in the events feed
        :param filter: (optional) The filter to apply to the query, default is None
        :param limit: (optional) The maximum number of results to return, default 100
        :param time_from: (optional) The start time of the query, default is 1 day
        :param time_to: (optional) The end time of the query, default is now
        :param cursor: (optional) The cursor to use for pagination, default is None
        :return: a Result object
        """
        # Default Filter to exclude auditTrail and originator in benchmarks, compliance, cloudsec
        # source != "auditTrail" and severity in ("0","1","2","3","4","5","6","7") and not originator in ("benchmarks","compliance","cloudsec")
        self.default_filter = "filter=source%20%21%3D%20%22auditTrail%22%20and%20severity%20in%20%28%226%22%29%20and%20not%20originator%20in%20%28%22benchmarks%22%2C%22compliance%22%2C%22cloudsec%22%29"
        if filter:
            filter = "%s%20and%20%s" % (self.default_filter, filter)
        else:
            filter = self.default_filter
        request = self._get_secure_events(filter=filter, limit=limit, time_from=time_from, time_to=time_to, cursor=cursor)
        return request

    def get_inventory(self, filter: str = '', page_number: int = 1, page_size: int = 100):
        """
        Get inventory resources, for new graph API use get_inventory_resource_graph
        :param filter: (optional) The filter to apply to the query, default is None
        :param page_number: (optional) The page number to return, default is 1
        :param page_size: (optional) The number of results per page, default is 100
        :return: a Result object
        """
        params = {"filter": filter, "pageNumber": page_number, "pageSize": page_size}
        request = self.client.get(path="/api/cspm/v1/inventory/resources", params=params)
        return request.res
    
    def get_inventory_resource(self, id: str, fields: str = None ):
        """
        Get inventory resource, doesn't actually seem to work as expected, for new graph API use get_inventory_resource_graph_resource
        :param id: The id of the resource
        :param fields: (optional) The fields to return, default is None
        :return: a Result object
        """
        if fields:
            params = {"fields": fields}
        else:
            params = None
        request = self.client.get(path=f'/api/cspm/v1/inventory/resources/{id}')
        return request.res
    
    def get_inventory_cloud_resource(self, resource_hash: str, fields: str = None):
        """
        Get inventory resource, for new graph API
        :param resource_hash: The hash of the resource
        :param fields: (optional) The fields to return, default is None
        :return: a Result object
        """
        params = {"resourceHash": resource_hash}
        if fields:
            params["fields"] = fields
        request = self.client.get(path=f'/api/cspm/v1/cloud/resource', params=params)
        return request.res
    
    def get_inventory_resource_graph(self, page_number: int = 1, page_size: int = 100, filter: str = '', fields: str = None, entities: List[str] = None):
        """
        TODO: Fix filters
        Get inventory resources, for new graph API
        :param page_number: (optional) The page number to return, default is 1
        :param page_size: (optional) The number of results per page, default is 100
        :param filter: (optional) The filter to apply to the query, default is None
        :param fields: (optional) The fields to return, default is None
        :param entities: (optional) The entities to return, default is None
        :return: a Result object
        """
        if filter:
            params = {"fields": filter}
        else:
            params = None
        request = self.client.get(path='/api/cspm/v1/inventory/graph-resources', params=params)
        return request.res

    def get_inventory_resource_graph_resource(self, resource_hash: str, resource_kind: str, fields: str = None):
        """
        TODO: Map the URI to the proper endpoint, ie kube, cloud, clusteranalysis, use get_inventory_resource_graph_resource2 for now
        Get inventory resource, for new graph API
        :param resource_hash: The hash of the resource
        :param resource_kind: The kind of the resource
        :param fields: (optional) The fields to return, default is None
        :return: a Result object
        """
        params = {"resourceHash": resource_hash, "resourceKind": resource_kind}
        request = self.client.get(path=f'/api/cspm/v1/inventory/graph-resources', params=params)
        return request.res

    def get_inventory_resource_graph_resource2(self, endpoint:str):
        """
        Get inventory resource, for new graph API
        :param endpoint: The endpoint of the resource
        :return: a Result object
        """
        request = self.client.get(path=endpoint)
        return request.res

if __name__ == "__main__":
    api = DigApi()
    # print(api.get_me())
    # print(api.get_secure_events().data)
    # print(api.get_inventory())
    # print(api.get_inventory_resource(id="574f45a2f797cfac7ee23736a7ccb561")) # old
    # print(api.get_inventory_resource_graph())
    # print(api.get_inventory_resource_graph_resource(resource_hash="574f45a2f797cfac7ee23736a7ccb561", resource_kind="aws_ec2_instance"))
    print(api.get_inventory_resource_graph_resource2(endpoint="/api/cspm/v1/kube/resource?resourceHash=827943c7614fe14822bcf7c60d44c264&resourceKind=Job"))
