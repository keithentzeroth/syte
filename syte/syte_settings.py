
DEPLOYMENT_MODE = 'dev'
COMPRESS_REVISION_NUMBER = '1.0'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_USER_API_URL = 'https://github.com/api/v2/json/user/show/'
GITHUB_REPOS_API_URL = 'https://github.com/api/v2/json/repos/show/'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False 
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
    from local_settings import *
else:
    DEBUG = False
    SITE_ROOT_URI = '[ENTER PROD URL HERE] ex. http://rigoneri.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'
