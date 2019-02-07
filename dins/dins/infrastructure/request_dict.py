from typing import Any

from pyramid.request import Request


class RequestDictionary(dict):
    def __getattr__(self, key):
        return self.get(key)


def create(request: Request) -> RequestDictionary: #prioritized in order for security
    data = {
        **request.GET, # query string
        **request.headers, #HTTP headers
        **request.POST, # form values
        **request.matchdict, # routing options
    }

    return RequestDictionary(data)
