# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nome=ndb.StringProperty(required=True)
