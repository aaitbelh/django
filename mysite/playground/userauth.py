# from django.contrib.auth.models import User
from django.conf import settings
def authenticateUser():
    print (settings.mode)
    return 1