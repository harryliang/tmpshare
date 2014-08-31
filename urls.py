#encoding=utf8
import tornado.web
import settings
from share import v_share
import os

application = tornado.web.Application([
    (r"/", v_share.Index),
    (r"/list/", v_share.FileList),
    (r"/upload/", v_share.Upload),
    (r"/uploads/(.*)", v_share.MyFile, {"path":os.path.join(settings.SITE_ROOT, 'uploads')})
],**settings.settings)
