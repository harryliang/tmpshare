#encoding=utf8
import tornado.web
import settings
from share import v_share

application = tornado.web.Application([
    (r"/", v_share.Index),
    (r"/list/", v_share.FileList),
    (r"/upload/", v_share.Upload),
],**settings.settings)
