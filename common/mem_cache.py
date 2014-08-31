#encoding=utf8
OBJ_DICT = {}

def memorize(function):
    """内存缓存, 用于不定参数的函数
    Usage:
        def xxx(key1,key2,refresh=False)
            return instance
        def xxx(key1,key2,key2,x1=xx,x2=yyy)
            return instance
    """
    def helper(*args, **kwargs):
        refresh = False
        if refresh in kwargs:
            refresh = kwargs['refresh']
        key = '%s#%s' % (function.__name__, '#'.join(args))
        ret_obj = None
        if refresh:
            del OBJ_DICT[key]
            return None
        else:
            try:
                ret_obj = OBJ_DICT[key]
            except KeyError:
                ret_obj = function(*args, **kwargs)
                OBJ_DICT[key] = ret_obj
            return ret_obj
    return helper

def init_mem_cache():
    OBJ_DICT.clear()