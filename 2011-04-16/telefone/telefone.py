# coding: utf-8

def telefone(entradas):

    dicionario_letras = {
                'abc': '2',
                'def': '3',
                'ghi': '4',
                'jkl': '5',
                'mno': '6',
                'pqrs': '7',
                'tuv': '8',
                'wxyz': '9',
    }
    
    lista = []
    
    for entrada in entradas:
        for intervalo, numero in dicionario_letras.items():
            if entrada in intervalo:
                lista.append(numero)
        
        if entrada in '01-':
            return str(entrada)
        raise ValueError("Caractere não permitido")
