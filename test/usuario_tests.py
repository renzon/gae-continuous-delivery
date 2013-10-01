# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from base import GAETestCase
from usuario.crud import SalvarValidando


class SalvarUsuarioTests(GAETestCase):
    def test_salvar(self):
        cmd=SalvarValidando("")
        cmd.execute(True)
        self.assertEqual(1,len(cmd.errors))
