#encoding=utf8
from mimetypes import guess_type
import os
from datetime import datetime, timedelta
import settings
import shutil

from common.log_utils import getLogger
log = getLogger('share_utils.py')

MAX_MINUTES_TO_KEEP = 10
max_delta = timedelta(minutes=MAX_MINUTES_TO_KEEP)

def getdir(filepath):
    file_list = []
    files_to_remove = []
    now = datetime.now()
    for root, dirs, files in os.walk(filepath):
        for fname in files:
            fname = os.path.join(root,fname).replace('\\','/')
            #log.debug('fname=%s' % fname)
            if os.path.isfile(fname):
                stat_info = os.stat(fname)
                modified = datetime.fromtimestamp(stat_info.st_mtime)
                if now - modified > max_delta:
                    files_to_remove.append(fname)
                    continue
                info = {
                    'name':fname,
                    'modified':modified.strftime('%Y-%m-%d %H:%M:%S'),
                    'type':guess_type(fname)[0],
                    'href':'%s/%s' % (settings.SITE_URL, fname)
                }
                file_list.append(info)
    file_list.sort(key=lambda x:x['modified'], reverse=True)
    for fname in files_to_remove:
        os.remove(fname)
    return file_list

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
