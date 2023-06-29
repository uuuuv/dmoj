# Triển khai production

## Sử dụng biến môi trường thay vì hard code, đặc biệt là các thông tin nhạy cảm
Thêm biến môi trường vào file site.conf ở /etc/supervisor/conf.d
```conf
[program:site]
command=/site/path/venv/bin/uwsgi --ini uwsgi.ini
directory=/site/path/site
startsecs=0
user=<user>
group=<user>
environment=
    DJANGO_HOST=<domain name>,
    DJANGO_SECRET_KEY=<secret key>,
    DJANGO_DEBUG=False,
    DJANGO_SENDGRID_API_KEY=<sendgrid key>
stopsignal=QUIT
stdout_logfile=/log/file/dir/site.stdout.log
stderr_logfile=/log/file/dir/site.stderr.log
```

## sửa lại file local_settings.py
```python
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','123')
HOST = os.environ.get('DJANGO_HOST', '127.0.0.1')
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
ALLOWED_HOSTS = [HOST,]

#######################################
############### caching ###############
#######################################

# Mình đã định sử dụng Redis, nhưng Redis caching chỉ hỗ trợ Django 4.
# DMOJ hiện tại là Django 3.2
# Do đó mình dùng memcached

## Cài memcached:
# sudo apt update
# sudo apt install memcached libmemcached-tools
# sudo systemctl start memcached
# Mặc định chạy ở port 11211

## Cài pymemcache binding
# (venv) pip3 install pymemcache
# Config lại khi DEBUG == False như dưới đây
if DEBUG == True:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        },
    }

if DEBUG == False: 
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }


# Email
if DEBUG == True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG == False: 
    # production mail config

EVENT_DAEMON_GET = 'ws://{}/event/'.format(HOST)
EVENT_DAEMON_GET_SSL = 'wss://{}/event/'.format(HOST) 

# cho phép iframe embedding
if DEBUG == False:
    X_FRAME_OPTIONS = 'ALLOWALL'
    CSRF_COOKIE_SAMESITE = 'None'
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'

```