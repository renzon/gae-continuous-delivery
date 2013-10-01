# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from usuario import facade


def salvar(_handler,_resp,nome):
    cmd=facade.salvar_usuario(nome).execute(True)
    if cmd.errors:
        _resp.write(cmd.errors)
    else:
        _handler.redirect("/")



