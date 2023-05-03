import os
import hashlib


GIT_DIR = '.ugit'


def init():
    if os.path.isdir('.ugit'):
        print('Already initialized')
        return False
    else:
        os.makedirs(GIT_DIR)
        os.makedirs(f'{GIT_DIR}/objects')
        return True


def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f:
        return f.read()