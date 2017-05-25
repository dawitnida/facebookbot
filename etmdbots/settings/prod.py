"""
Ethiopian Movie Database.
"""

__author__ = "EtMDB Developers (developers@etmdb.com)"
__date__ = "Date: 25/05/2017"
__version__ = "Version: 1.0"
__Copyright__ = "Copyright: @etmdb"
"""
Django settings for etmdbots project. (production)

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from .base_setting import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['46.101.43.214', 'etmdb.com', 'www.etmdb.com', 'etmdb1.etmdb.com', 'developer.etmdb.com',
                 'www.developer.etmdb.com']
