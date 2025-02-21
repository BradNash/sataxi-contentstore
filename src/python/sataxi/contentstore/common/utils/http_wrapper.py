from typing import Dict

from tornado.httpclient import HTTPRequest, AsyncHTTPClient, HTTPError


class HttpWrapper:
    def __init__(self, headers: Dict[str, str]):
        super().__init__()
        self.headers = headers

    async def send_http_request(self, method: str, url: str, body: str, timeout: int):
        try:
            client = AsyncHTTPClient()
            req = HTTPRequest(
                method=method,
                url=url,
                body=body,
                headers=self.headers,
                connect_timeout=timeout,
            )
            response = await client.fetch(req)
            return response.body
        except HTTPError as http_error:
            raise http_error
