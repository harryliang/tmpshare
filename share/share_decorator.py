#encoding=utf8

import functools
import json
import os
import settings

def ip_check(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        remote_ip = self.request.remote_ip
        allowed_ip_list = set(json.load(file(os.path.join(settings.SITE_ROOT, 'config', 'allowed_ip.json'))))
        if allowed_ip_list and remote_ip not in allowed_ip_list:
            self.write("Access denied!")
            return
        return method(self, *args, **kwargs)
    return wrapper