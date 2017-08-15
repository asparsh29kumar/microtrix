import mechanize
from BeautifulSoup import BeautifulSoup


class SanitizeHandler(mechanize.BaseHandler):
    def __init__(self):
        pass

    def http_response(self, request, httpResponse):
        if not hasattr(httpResponse, "seek"):
            httpResponse = mechanize.response_seek_wrapper(httpResponse)
        # If HTML used, get it though a robust Parser like BeautifulSoup
        if 'content-type' in httpResponse.info().dict and ('html' in httpResponse.info().dict['content-type']):
            soup = BeautifulSoup(httpResponse.get_data())
            httpResponse.set_data(soup.prettify())
        return httpResponse
