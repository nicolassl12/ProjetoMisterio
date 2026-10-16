def cifrar(palavra, chave="artyom"):
    palavra = palavra.lower()
    resultado = ""

    for i, l in enumerate(palavra):
        letraChave = chave[i % len(chave)]
        deslocamento = ord(letraChave) - ord("a")
        nova = (ord(l) - ord("a") + deslocamento) % 26
        resultado += chr(nova + ord("a"))

    return resultado[1:] + resultado[0]

def par_Mult5Imp_Impar(palavra):
    n = len(palavra)
    if (n % 2 == 0):
        return True
    elif (n % 5 == 0) and (n % 2 != 0) and (n != 5):
        return True
    return False

while 1: 
    palavra = input()

    tamanhoPalavra = len(palavra)

    finalPalavra = palavra[1:]    

    seqInvertida = finalPalavra[::-1]

    ultimaLetra = palavra[tamanhoPalavra - 1]

    vogaisOuConsoantes = ""

    vogais = "aeiou"
    consoantes = "bcdfghjklmnpqrstvwxyz"

    for l in palavra:
        if par_Mult5Imp_Impar(palavra):
            if l.lower() in vogais:
                vogaisOuConsoantes += l
        else:
            if l.lower() in consoantes:
                vogaisOuConsoantes += l

    cifrada = cifrar(palavra)

    print(palavra[0] + cifrada + seqInvertida[1:] + ultimaLetra + vogaisOuConsoantes)




