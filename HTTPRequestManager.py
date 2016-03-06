"""

Contains the HTTPRequestManager class used to
make requests to HTTP servers.

Author: Mihir Kasmalkar
Date created: March 5, 2016

"""

import urllib.request
import urllib.parse


class HTTPRequestManager():
    """

    A class used to make requests to HTTP servers. The reason that a new
    class was made rather than using an existing class is that
    the existing class for some reason would not properly get data
    from the REST server this application requests to (api.wordnik.com),
    so a new class using a different way of making requests was made.

    """
    
    def __init__(self, server, port):
        """

        Initialize the HTTPRequestManager with the server name and the
        TCP/IP port it is on (the http:// must be omitted in the server name.

        """

        self.server = server
        self.port = port


    def request(self, method, url, body={}):
        """
        Make a request to the server this HTTPRequestManager is configured with using the specified method (GET, POST, PUT, DELETE, etc.),
        url (i.e. /v4/word.json/hello/definition), and parameters (api_key=12346&limit=100&...); and return the result.
        """

        #             http://  api.wordnikcom   :           80       /v4/words.json/hello/definition   ?        api_key=1234567890
        requestURL = "http://" + self.server + ":" + str(self.port) +            url                + "?" + urllib.parse.urlencode(body)

        return urllib.request.urlopen(requestURL)
