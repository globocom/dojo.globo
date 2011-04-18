# -*- coding: utf-8 -*-

import unittest
from cheque_por_extenso import Cheque

class Tester(unittest.TestCase):
   
    def test_cheque_um_real(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(1)
        self.assertEquals(valor_calculado, 'um real')
        
    def test_dois_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(2)
        self.assertEquals(valor_calculado, 'dois reais')
        
    def test_tres_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(3)
        self.assertEquals(valor_calculado, 'tres reais')

    def test_quatro_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(4)
        self.assertEquals(valor_calculado, 'quatro reais')   
        
    def test_cheque_cinco_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(5)
        self.assertEquals(valor_calculado, 'cinco reais')
        
    def test_cheque_seis_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(6)
        self.assertEquals(valor_calculado, 'seis reais')
    
    def test_cheque_dez_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(10)
        self.assertEquals(valor_calculado, 'dez reais')
        
    def test_cheque_quinze_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(15)
        self.assertEquals(valor_calculado, 'quinze reais')
        
    ######
        
    def test_cheque_vinte_e_um_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(21)
        self.assertEquals(valor_calculado, 'vinte e um reais')
        
    def test_cheque_vinte_e_dois_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(22)
        self.assertEquals(valor_calculado, 'vinte e dois reais')
        
    def test_cheque_vinte_e_sete_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(27)
        self.assertEquals(valor_calculado, 'vinte e sete reais')
        
    def test_cheque_trinta_e_sete_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(37)
        self.assertEquals(valor_calculado, 'trinta e sete reais')
        
    def test_cheque_quarenta_e_dois_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(42)
        self.assertEquals(valor_calculado, 'quarenta e dois reais')
        
    def test_cheque_dezoito_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(18)
        self.assertEquals(valor_calculado, 'dezoito reais')
        
    def test_cheque_cento_e_cinco_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(105)
        self.assertEquals(valor_calculado, 'cento e cinco reais')
        
    def test_cheque_cento_e_vinte_e_cinco_reais(self):
        cheque = Cheque()
        valor_calculado = cheque.retorna_valor_por_extenso(125)
        self.assertEquals(valor_calculado, 'cento e vinte e cinco reais')
        
   

unittest.main()
