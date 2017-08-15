import mechanize
from BeautifulSoup import BeautifulSoup


class SanitizeHandler(mechanize.BaseHandler):
    def __init__(self):
        pass

    def http_response(self, request, response):
        if not hasattr(response, "seek"):
            response = mechanize.response_seek_wrapper(response)
        # if    HTML   used   get   it though  a    robust  Parser    like  BeautifulSoup
        if response.info().dict.has_key('content-type') and ('html' in response.info().dict['content-type']):
            soup = BeautifulSoup(response.get_data())
            response.set_data(soup.prettify())
        return response


try:
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.add_handler(SanitizeHandler())
    # Now    you get    good   HTML
    br.open('https://mahe3.dvois.com/24online/webpages/client.jsp')

    response = br.response()
    originalPage = response.read()
    br.select_form('clientloginform')
    br.form.set_all_readonly(False)

    br["mode"] = "193"
    br["checkClose"] = "1"

    br.submit()
    mystr = response.read().lower()

    if mystr.find("different user name") != -1:
        print("Couldn't log out.")
    else:
        print("Successfully logged out.")
except (KeyboardInterrupt, SystemExit):
    print("There was a keyboard interrupt. Exiting the logout procedure.")
