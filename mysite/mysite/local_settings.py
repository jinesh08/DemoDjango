DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'mysite',
       'USER': 'root',
       'PASSWORD': 'testing',
       'HOST': 'localhost',
       'PORT': '3306',
   }
}

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000',
    'localhost:3000',
    'localhost',
    'http://127.0.0.1',
    'localhost:9000'
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'localhost:3000',
    'localhost',
    'http://127.0.0.1',
    'localhost:9000'
]

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)