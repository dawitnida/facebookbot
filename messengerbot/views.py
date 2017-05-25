"""
Ethiopian Movie Database.
"""

__author__ = "EtMDB Developers (developers@etmdb.com)"
__date__ = "Date: 25/05/2017"
__version__ = "Version: 1.0"
__Copyright__ = "Copyright: @etmdb"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

'''
'''


def index(request):
    return HttpResponse("Hello Bot World")
