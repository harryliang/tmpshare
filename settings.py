#encoding=utf8

import os

DEBUG = False
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = 'http://127.0.0.1'
SITE_PORT = 80
SECRET_KEY = "asdlfjkhlkasdflasdkfjhagg;d9dfjsdkfhsdfjksdf"

IP_CHECK = False

try:
    from local_settings import *
except:
    pass

if SITE_PORT != 80:
    SITE_URL = '%s:%s' % (SITE_URL, SITE_PORT)

settings = dict(
    cookie_secret=SECRET_KEY,
    login_url="/login/",
    template_path=os.path.join(SITE_ROOT, "templates"),
    static_path=os.path.join(SITE_ROOT, "static"),
    xsrf_cookies=True,
    autoescape="xhtml_escape",
    debug=DEBUG,
    xheaders=True,
)