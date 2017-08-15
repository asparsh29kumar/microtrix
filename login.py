import time
import sys
import mechanize
import ssl
from SanitizeHandler import SanitizeHandler

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    print("Attribute Error!!")
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.add_handler(SanitizeHandler())
        # Now you get good HTML
        br.open('https://mahe3.dvois.com/24online/webpages/client.jsp')
        response = br.response()
        # print response.geturl()  # URL of the page we just opened
        # print response.info()  # headers
        # print response.read()  # body
        try:
            br.select_form('clientloginform')
            br.form.set_all_readonly(False)
            br.form['username'] = sys.argv[1]
            br.form['password'] = sys.argv[2]
            br.submit()
            response = br.response()
            mystr = response.read().lower()
            print("Timestamp: %s" % time.ctime())
            if mystr.find("different user name") != -1:
                print("Different username on the same IP.")
            elif (mystr.find("successfully") != -1) or (mystr.find(sys.argv[1]) != -1):
                print("Successful login.")
            elif mystr.find("wrong") != -1:
                print("Wrong login.")
            else:
                print("Strange scenario.")
        except Exception, e:
            print str(e)

    except (KeyboardInterrupt, SystemExit):
        print("There was a keyboard interrupt. Exiting the login procedure.")
