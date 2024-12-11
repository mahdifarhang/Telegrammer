from django.conf import settings

import requests
import json
from urllib.parse import urljoin
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class APIRequester(object):
    """
    This base request can be instantiated with a base URL for an API.
    Subsequent calls can be made with the usual arguments for :meth:`requests.request`, specifying only the API route::
        >>> api_request = APIRequest('http://example.com/api/v3')
        >>> response = api_request('POST', '/login', data={'username': 'foo', 'password': 'bar'})
    etc.
    """

    base_url = getattr(settings, 'TELEGRAM_BOT_API_BASE_URL', 'https://api.telegram.org')
    timeout = 3.0

    def __init__(self, base_url=None, headers=None, json_response=True, timeout=None):
        self.json_response = json_response
        if base_url is not None:
            self.base_url = base_url
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        if timeout is not None:
            self.timeout = timeout
        if headers is not None:
            self.headers = headers
        else:
            self.headers = {}

            # Could be a useful code for later:
            #
            # if self.base_url == getattr(settings, 'TELEGRAM_BOT_API_BASE_URL'):
            #     self.headers.update({
            #         'Authorization': f"Token {getattr(settings, 'NOBITEX_AUTHORIZATION_TOKEN')}"
            #     })

    def __call__(self, endpoint, method="GET", **kwargs):
        self.endpoint = endpoint
        if self.endpoint.startswith('/'):
            self.endpoint = self.endpoint[1:]
        if not self.base_url.endswith('/'):
            self.base_url += '/'

        self.url = urljoin(self.base_url, self.endpoint, allow_fragments=False)
        headers = kwargs.pop('headers', {})
        self.headers.update(headers)

        response = requests.request(method=method, url=self.url, headers=headers, timeout=self.timeout, **kwargs)
        if response.status_code // 100 == 2:
            if self.json_response:
                return json.loads(response.text)
            return response.text
        else:
            raise Exception(response.text)
        # if 'data' in kwargs:
        #     log.info(u'{} {} with headers:\n{}\nand data:\n{}'.format(
        #         method,
        #         self.url,
        #         json.dumps(headers, indent=4),
        #         json.dumps(kwargs['data'], indent=4)
        #     ))
        # elif 'json' in kwargs:
        #     log.info(u'{} {} with headers:\n{}\nand JSON:\n{}'.format(
        #         method,
        #         self.url,
        #         json.dumps(headers, indent=4),
        #         json.dumps(kwargs['json'], indent=4)
        #     ))
        # else:
        #     log.info(u'{} {} with headers:\n{}'.format(
        #         method,
        #         self.url,
        #         json.dumps(headers, indent=4)
        #     ))
        #
        # log.info(
        #     u'Response to {} {} => {} {}\n{}'.format(
        #         method,
        #         self.url,
        #         response.status_code,
        #         response.reason,
        #         response.text[:100])
        # )
