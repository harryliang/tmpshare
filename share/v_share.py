#encoding=utf8
import tornado.web
from share_utils import getdir, create_folder
from share_decorator import ip_check
import json
import os

from common.log_utils import getLogger
log = getLogger('v_share.py')

class Index(tornado.web.RequestHandler):
    @ip_check
    def get(self):
        params = locals()
        params.pop('self')
        self.render('share/index.html', **params)
        return

    def post(self):
        log.debug(self.request.arguments)
        self.redirect('/')
        return

class FileList(tornado.web.RequestHandler):
    def get(self):
        data = getdir('uploads/')
        self.write(json.dumps(data))

class Upload(tornado.web.RequestHandler):
    def post(self):
        # fn = (isset($_SERVER['HTTP_X_FILENAME']) ? $_SERVER['HTTP_X_FILENAME'] : false);
        fn = self.request.headers.get('X_filename')

        if fn:
            #uploaded file name include path
            fname = self.get_argument('fname', '')
            if fname != '' and fname != 'undefined':
                create_folder('uploads/%s' % os.path.dirname(fname))
                targetfile = 'uploads/%s' % fname
            else:
                targetfile = 'uploads/%s' % fn
            # AJAX call
            file(targetfile, 'wb').write(self.request.body)
            self.write('ok')
        
        else:
            # form submit
            files = self.request.files.get('fileselect')
            for item in files:
                fn = item['filename']
                targetfile = 'uploads/%s' % fn
                file(targetfile, 'wb').write(item['body'])
                self.write("<p>File %s uploaded.</p>" % fn)

    def check_xsrf_cookie(self):
        return

class MyFile(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header("Cache-control", "no-cache")