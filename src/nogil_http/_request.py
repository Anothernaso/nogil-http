from http import HTTPMethod
from http.client import HTTPMessage
from io import BufferedIOBase


class HTTPRequest:
    method: HTTPMethod | None = None
    headers: HTTPMessage | None = None
    rfile: BufferedIOBase | None = None
