#encoding=utf8

import tornado.ioloop
import tornado.web
from urls import application
import settings
import os

if __name__ == "__main__":
    uploads = os.path.join(settings.SITE_ROOT, 'uploads')
    if not os.path.exists(uploads):
        os.makedirs(uploads)

    port = settings.SITE_PORT
    application.listen(port)
    print 'tornado server started on port %s' % port
    tornado.ioloop.IOLoop.instance().start()
