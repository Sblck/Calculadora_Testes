import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4


class TestCalculadora(unittest.TestCase):

    valores = [2, -2, 2.5, -2.5]

    def teste_loop_combinacoes_valores(self, func):
        # Teste operações básicas de cada operador + - * / % ^
        for a in self.valores:
            for b in self.valores:
                self.assertEqual(func(a, b, '+'), a + b)
                self.assertEqual(func(a, b, '-'), a - b)
                self.assertEqual(func(a, b, '*'), a * b)
                self.assertEqual(func(a, b, '/'), a / b)
                self.assertEqual(func(a, b, '%'), a % b)
                self.assertEqual(func(a, b, '^'), a ^ b)

    def teste_operacoes_basicas(self):
        self._testa_operacoes_basicas(calculadora)

    def teste_v2_operacoes(self):
        self._testa_operacoes_basicas(calculadora_v2)

    def teste_v3_operacoes(self):
        self._testa_operacoes_basicas(calculadora_v3)

    def teste_v4_operacoes(self):
        self._testa_operacoes_basicas(calculadora_v4)

    def teste_operacoes_diversas(self):
        valores = [0] + self.valores
        for funcao in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                # Teste divisão por zero operador para todas versões / %
                self.assertTrue(math.isnan(calculadora(a, 0, '/')))
                self.assertTrue(math.isnan(calculadora(a, 0, '%')))

        # Teste operador inválido - fazer três testes para todas as versões
        valores = [0] + self.valores
        for funcao in [calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                for b in valores:
                    self.assertTrue(math.isnan(funcao(a, b, '$')))
                    self.assertTrue(math.isnan(funcao(a, b, '#')))
                    self.assertTrue(math.isnan(funcao(a, b, 'qwe')))

        # Teste números de virgula flutuante - fazer três testes para todas as versões

        '''
        
        Nota : Testes anterior já deveram apanhar estes casos;

        #self.assertAlmostEqual(calculadora(2.5, 1.5, '+'), 4.0)
        #self.assertAlmostEqual(calculadora(4.5, 1.5, '-'), 3.0)
        #self.assertAlmostEqual(calculadora(5.5, 1.5, '*'), 8.25)

        # Teste números negativos - fazer 3 testes para todas as versões
        #self.assertEqual(calculadora(-2, 3, '*'), -6)

        # Teste números negativos com divisão e módulo, testar para todas as versões
        #self.assertTrue(calculadora(-6, 3, '/'), -2.0)
        #self.assertTrue(calculadora(-7, 3, '%'), 2.0)

        # Teste números negativos com exponenciação, testar para todas as versões
        #self.assertEqual(calculadora(-2, 3, '^'), -8)

        '''
        # Teste números negativos com exponenciação de zero, testar para todas as versões
        valores = [0, -3, -4.2]
        for funcao in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                #a^0 = 1
                self.assertEqual(funcao(a, 0, '^'), 1)
            for b in valores:
                # 0^b = 0 para b > 0, 0^0 == 1
                if b == 0:
                    self.assertEqual(funcao(0, b, '^'), 1)
                else:
                    self.assertEqual(funcao(0, b, '^'), 0)


if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py
