def cifrar(palavra, chave="artyom"):
    palavra = palavra.lower()
    resultado = ""

    for i, l in enumerate(palavra):
        letraChave = chave[i % len(chave)]
        deslocamento = ord(letraChave) - ord("a")
        nova = (ord(l) - ord("a") + deslocamento) % 26
        resultado += chr(nova + ord("a"))

    return resultado[1:] + resultado[0]

def ehPrimo(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def mostraVogais(palavra):
    return not ehPrimo(len(palavra))

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
        if mostraVogais(palavra):
            if l.lower() in vogais:
                vogaisOuConsoantes += l
        else:
            if l.lower() in consoantes:
                vogaisOuConsoantes += l

    cifrada = cifrar(palavra)

    print(palavra[0] + cifrada + seqInvertida[1:] + ultimaLetra + vogaisOuConsoantes)
