# coding=utf-8
import requests

from digital_license_manager._version import __version__
from requests.auth import HTTPBasicAuth


class Client(object):

    def __init__(self, base_api_url, consumer_key, consumer_secret):
        self.user_agent = 'Digital License Manager - Python Client v' + __version__
        self.api_url = (base_api_url.rstrip('/') if base_api_url.endswith('/') else base_api_url) + '/wp-json/dlm/v1/'
        self.api_auth = HTTPBasicAuth(consumer_key, consumer_secret)
        self.api_headers = {'User-Agent': self.user_agent}

    def send(self, type, endpoint, params=None):
        endpoint_url = self.api_url + (endpoint.lstrip('/') if endpoint.startswith('/') else endpoint)
        if type == 'post':
            r = requests.post(url=endpoint_url, headers=self.api_headers, auth=self.api_auth, data=params)
        else:
            r = requests.get(url=endpoint_url, headers=self.api_headers, auth=self.api_auth, data=params)
        if r.ok:
            return r.json()
        else:
            try:
                return r.json()
            except Exception as e:
                raise Exception('Failed to parse JSON response from the remote API.')

    def find_license(self, license_key):
        return self.send('get', 'licenses/' + license_key)

    def activate_license(self, license_key, software_id=-1):
        endpoint = 'licenses/activate/' + license_key
        if software_id > 0:
            endpoint += '?software=' + str(software_id)
        return self.send('get', endpoint)

    def validate_license_activation(self, token):
        return self.send('get', 'licenses/validate/' + token)

    def deactivate_license_activation(self, token):
        return self.send('get', 'licenses/deactivate/' + token)
