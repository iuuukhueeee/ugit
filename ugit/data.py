import os


GIT_DIR = '.ugit'


def init():
    if os.path.isdir('.ugit'):
        print('Already initialized')
        return False
    else:
        os.makedirs(GIT_DIR)
        return True
