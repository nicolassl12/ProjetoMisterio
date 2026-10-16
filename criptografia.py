def cifrar(palavra, chave="artyom"):
    palavra = palavra.lower()
    resultado = ""

    for i, l in enumerate(palavra):
        letra_chave = chave[i % len(chave)]
        deslocamento = ord(letra_chave) - ord("a")
        nova = (ord(l) - ord("a") + deslocamento) % 26
        resultado += chr(nova + ord("a"))

    return resultado[1:] + resultado[0]

def parOuImpar(palavra):
    n = len(palavra)
    if (n % 2 == 0):
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
        if parOuImpar(palavra):
            if l.lower() in vogais:
                vogaisOuConsoantes += l
        else:
            if l.lower() in consoantes:
                vogaisOuConsoantes += l

    cifrada = cifrar(palavra)

    print(palavra[0] + cifrada + seqInvertida[1:] + ultimaLetra + vogaisOuConsoantes)




