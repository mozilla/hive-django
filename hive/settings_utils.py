import os
import sys

def set_default_env(**kwargs):
    for key in kwargs:
        if not key in os.environ:
            os.environ[key] = kwargs[key]

def set_default_db(default):
    set_default_env(DATABASE_URL=default)
    url = os.environ['DATABASE_URL']
    if url.upper() == url:
        # The environment variable is naming another environment variable,
        # whose value we should retrieve.
        os.environ['DATABASE_URL'] = os.environ[url]

def parse_secure_proxy_ssl_header(field):
    name, value = field.split(':')
    return ('HTTP_%s' % name.upper().replace('-', '_'), value.strip())

def is_running_test_suite():
    return (os.path.basename(sys.argv[0]) == 'manage.py' and 
            len(sys.argv) > 1 and sys.argv[1] == 'test')
