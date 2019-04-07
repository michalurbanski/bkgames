from functools import wraps

__instances = {}

def singleton(cls):
    """ https://xiaoxing.us/2018/04/15/singleton-in-python/ """
    @wraps(cls)
    def getInstance(*args, **kwargs):
        instance = __instances.get(cls, None)
        if not instance:
            instance = cls(*args, **kwargs)
            __instances[cls] = instance
        return instance
    return getInstance
