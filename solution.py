def length(object):
    if type(object) == dict:
        keys = list(object.keys())
        return keys.index(keys[-1], -1) + 1
    elif type(object) == set:
        object = list(object)
        return object.index(object[-1], -1) + 1
    elif type(object) == list or type(object) == str:
        return object.index(object[-1], -1) + 1
    else:
        return object.index(object[-1]) + 1
