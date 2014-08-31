#encoding=utf8

import tornado.ioloop
import tornado.web
from urls import application
import settings

if __name__ == "__main__":
    port = settings.SITE_PORT
    application.listen(port)
    print 'tornado server started on port %s' % port
    tornado.ioloop.IOLoop.instance().start()
