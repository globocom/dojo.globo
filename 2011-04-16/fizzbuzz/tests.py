import unittest

from fizzbuzz import fizzbuzz, monta_lista

class tester(unittest.TestCase):
    def test_falando_negativo_levanta_excecao(self):
        self.assertRaises(ValueError, fizzbuzz, -1)

    def test_falando_1_retorna_1(self):
        self.assertEquals(fizzbuzz(1), '1')

    def test_falando_0_levanta_excecao(self):
        self.assertRaises(ValueError, fizzbuzz, 0)

    def test_falando_2_retorna_2(self):
        self.assertEquals(fizzbuzz(2), '2')

    def test_falando_3_retorna_fizz(self):
        self.assertEquals(fizzbuzz(3), 'fizz')

    def test_falando_5_retorna_buzz(self):
        self.assertEquals(fizzbuzz(5), 'buzz')    
    
    def test_falando_6_retorna_fizz(self):
        self.assertEquals(fizzbuzz(6), 'fizz')
    
    def test_falando_15_retorna_fizzbuzz(self):
        self.assertEquals(fizzbuzz(15), 'fizzbuzz')
    
    def test_falando_45_retorna_fizzbuzz(self):
        self.assertEquals(fizzbuzz(45), 'fizzbuzz')
    
    def test_falando_lista_ate_3_retorna_0_1_2_fizz(self):
        lista_esperada = ['1', '2', 'fizz']
        self.assertEquals(monta_lista(3), lista_esperada)

    def test_falando_lista_ate_5_retorna_0_1_2_3_fizz_4_buzz(self):
        lista_esperada = ['1', '2', 'fizz','4','buzz']
        self.assertEquals(monta_lista(5), lista_esperada)
    
    def test_falando_lista_ate_2_retorna_0_1_2(self):
        lista_esperada = ['1', '2']
        self.assertEquals(monta_lista(2), lista_esperada)
    
    def test_falando_lista_ate_15_retorna_1_a_fizzbuzz(self):
        lista_esperada = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
        self.assertEquals(monta_lista(15), lista_esperada)
unittest.main()
