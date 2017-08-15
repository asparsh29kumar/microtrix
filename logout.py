import mechanize
from SanitizeHandler import SanitizeHandler


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
