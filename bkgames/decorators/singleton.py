from functools import wraps

__instances = {}

def singleton(cls):
    """ Changes object into singleton.

    Implementation based on https://xiaoxing.us/2018/04/15/singleton-in-python/ 
    
    This is valid implementation of the sinleton pattern, although it's no longer used in code.
    Left here for reference only.
    """

    @wraps(cls)
    def getInstance(*args, **kwargs):
        instance = __instances.get(cls, None)
        if not instance:
            instance = cls(*args, **kwargs)
            __instances[cls] = instance
        return instance
    return getInstance
