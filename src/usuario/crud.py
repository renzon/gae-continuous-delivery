# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import Command, CommandList
from usuario.model import Usuario


class SalvarUsuarioCmd(Command):
    def __init__(self, nome):
        Command.__init__(self,nome=nome)

    def do_business(self, stop_on_error=True):
        pass

    def commit(self):
        return Usuario(nome=self.nome)


class ValidarUsuarioCmd(Command):
    def __init__(self, nome):
        Command.__init__(self,nome=nome)

    def do_business(self, stop_on_error=True):
        if not self.nome:
            self.add_error('nome', 'Nome é obrigatório')


class SalvarValidando(CommandList):
    def __init__(self, nome):
        CommandList.__init__(self,[ValidarUsuarioCmd(nome), SalvarUsuarioCmd(nome)])


