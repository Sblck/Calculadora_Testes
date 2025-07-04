import unittest
# import math TODO: Validar futuramente
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadoraEdgeCases(unittest.TestCase):
    # TESTES : Comutatividade e associatividade
    def test_comutatividade_associatividade(self):
        # Comutatividade (int,int)(-int,int)(int,-int)(-int,-int)
        #                (float,float)(-float,float)(float,-float)(-float,-float) = 8 combinaçoes
        # Total de combinacoes tem de ser: 2 tipos de variavel de a,b, 2 tipos de sinal de a,b
        # Total de combinacoes = int(a) +- = 2 , int(b) +- = 2
        #                      = int(a) +- = 2 , float(b) +- = 2
        #                      = float(a) +- = 2, float(b) +- = 2
        #                      = float(a) +- = 2, int(b) +- = 2
        # Total de combinações =  16 
        #  = n ^ k, ( considerando a ordem como importante), n= 2 tipos x 2 sinais , k = nºvariaveis
        valores = [2, -2, 2.5, -2.5]
        for funcao in [calculadora,calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                for b in valores:
                    soma_ab = funcao(a, b, '+')
                    soma_ba = funcao(b, a, '+')
                    mult_ab = funcao(a, b, '*')
                    mult_ba = funcao(b, a, '*')
                    self.assertEqual(soma_ab, soma_ba, msg=f"Falha comutatividade soma para a={a}, b={b}")
                    self.assertEqual(mult_ab, mult_ba, msg=f"Falha comutatividade multiplicação para a={a}, b={b}")
        # Associatividade
        # Total de combinações = n^k, n = 4 , k = 3 -> Total de combinações = 64
        for funcao in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            for a in valores:
                for b in valores:
                    for c in valores:
                        print(a,b,c)
                        self.assertEqual(
                            funcao(funcao(a, b, '+'), c, '+'),
                            funcao(a, funcao(b, c, '+'), '+'),
                            msg=f"Falha: associatividade soma para a={a}, b={b}, c={c}"
                        )
                        self.assertEqual(
                            funcao(funcao(a, b, '*'), c, '*'),
                            funcao(a, funcao(b, c, '*'), '*'),
                            msg=f"Falha: associatividade multiplicação para a={a}, b={b}, c={c}"
                        )


if __name__ == '__main__':
    unittest.main() 