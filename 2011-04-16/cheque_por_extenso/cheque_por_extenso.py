# coding: utf-8

unidades = {1:"um", 2:"dois", 3:"tres", 4:"quatro", 5:"cinco", 6:"seis",7:"sete",
            10: "dez",15: "quinze", 18: "dezoito",
            20:"vinte", 30:"trinta", 40:"quarenta",
            100:"cento", 120:"cento e vinte"}

class Cheque(object):
    def fatorar(self, numero):
        dezena, unidade = divmod(numero, 10)
        centena = 0
        if dezena > 10:
            centena, dezena = divmod(dezena, 10)
            
        return [centena, dezena, unidade]
    
    def brincar_feiamente(self):
        numero = 1003
        comprimento = len(str(numero))
    
    def retorna_valor_por_extenso(self, numero):
        if numero == 1:
            moeda = "real"
        else:
            moeda = "reais"
            
        if numero < 20:
            return "%s %s" % (unidades[numero], moeda)
        else :
            
            centena, dezena, unidade = self.fatorar(numero)
            if centena == 0:
                return "%s e %s %s" % (unidades[dezena*10], unidades[unidade], moeda)
            else:
                return "%s e %s e %s %s" % (unidades[centena*100], unidades[dezena*10], unidades[unidade], moeda)
            
      
