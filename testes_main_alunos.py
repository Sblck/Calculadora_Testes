import unittest
import math
import operator
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4


class TestCalculadora(unittest.TestCase):

    valores = [2, -2, 2.5, -2.5]

    def _loop_combinacoes_valores(self, func):
        operacoes = [
            ('+', operator.add),
            ('-', operator.sub),
            ('*', operator.mul),
            ('/', operator.truediv),
            ('%', operator.mod),
            ('^', operator.pow),
        ]
        # Teste operações básicas de cada operador + - * / % ^
        for a in self.valores:
            for b in self.valores:
                 for simbolo, op_func in operacoes:
                    teorico = op_func(a, b)
                    nossa_implmentacao = func(a, b, simbolo)
                    #print(f"Testando: {a} {simbolo} {b} | Esperado: {teorico} | Resultado: {nossa_implmentacao}")
                    self.assertEqual(
                        nossa_implmentacao, teorico,
                        msg=f"Erro para a={a}, b={b}, operação='{simbolo}'"
                    )
                #self.assertEqual(func(a, b, '^'), a ^ b, msg=f"Erro para a={a}, b={b}, operação='^'")
                # a ^ b é bitwise em python é XOR !

    def teste_operacoes_basicas(self):
        self._loop_combinacoes_valores(calculadora)

    def teste_v2_operacoes(self):
        self._loop_combinacoes_valores(calculadora_v2)

    def teste_v3_operacoes(self):
        self._loop_combinacoes_valores(calculadora_v3)

    def teste_v4_operacoes(self):
        self._loop_combinacoes_valores(calculadora_v4)

    def teste_operacoes_diversas(self):
        valores = [0] + self.valores
        for funcao in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                for op in ['/','%']:
                    with self.subTest(a=a, op=op, funcao=funcao):
                        try:
                            resultado_div = funcao(a, 0, op)
                            self.assertTrue(math.isnan(resultado_div), msg=f"Esperado nan para {a} / 0 com {funcao.__name__}")
                        except Exception as e:
                            self.fail(f"{type(e).__name__} para {a} {op} 0 com {funcao.__name__}: {e}")

        # Teste operador inválido - fazer três testes para todas as versões
        valores = [0] + self.valores
        for funcao in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                for b in valores:
                    for op in ['$', '#', 'qwe']:
                        with self.subTest(a=a, b=b, op=op, funcao=funcao):
                            try:
                                resultado = funcao(a, b, op)
                                self.assertTrue(
                                    math.isnan(resultado),
                                    msg=f"Esperado nan para {a} {op} {b} com {funcao.__name__}"
                                )
                            except Exception as e:
                                self.fail(f"{type(e).__name__} para {a} {op} {b} com {funcao.__name__}: {e}")

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
                with self.subTest(funcao=funcao, a=a, b=0, op='^'):
                    try:
                        # a^0 = 1
                        self.assertEqual(funcao(a, 0, '^'), 1)
                    except Exception as e:
                        self.fail(f"{type(e).__name__} para {a} ^ 0 com {funcao.__name__}: {e}")
            for b in valores:
                with self.subTest(funcao=funcao, a=0, b=b, op='^'):
                    try:
                        # 0^b = 0 para b != 0, 0^0 == 1
                        esperado = 1 if b == 0 else 0
                        self.assertEqual(funcao(0, b, '^'), esperado)
                    except Exception as e:
                        self.fail(f"{type(e).__name__} para 0 ^ {b} com {funcao.__name__}: {e}")


if __name__ == '__main__':
    unittest.main()

# para correr os testes: python -m unittest -v testes_main_alunos.py
