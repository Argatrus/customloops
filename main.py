def is_key_present(dictionary, key):
    for k in dictionary:
        if k == key:
            return True
    return False

def for_loop(index = 0,**kwargs):
    if is_key_present(kwargs, 'length'):
        if index < kwargs['length']:
            try:
                kwargs['function'](index)
            except:
                kwargs['function']()
            for_loop(index + 1, function = kwargs['function'], length = kwargs['length'])
    else:
        if index < len(kwargs['iterable']):
            kwargs['function'](kwargs['iterable'][index])
            for_loop(index+1, iterable = kwargs['iterable'], function = kwargs['function'])
