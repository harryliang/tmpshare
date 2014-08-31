#encoding:utf-8

# use log4py as logger

import os,sys
if __name__ == '__main__':
  sys.path.insert(0,os.path.abspath(os.curdir))

from common import log4py

#create logger
def getLogger(func_name):
    return log4py.Logger().get_instance(func_name)

def test():
    log = getLogger('test')
    log.debug('this is a debug msg')
    log.info('this is a debug msg')
    log.warn('this is a debug msg')
    log.error('this is a debug msg')

def another_test():
    log = getLogger('another_test')
    log.debug('this is a debug msg')
    log.info('this is a debug msg')
    log.warn('this is a debug msg')
    log.error('this is a debug msg')

if __name__ == '__main__':
    test()
    another_test()