
def censor(texto,palabra):
    #dividimos el texto con split() convirtiendolo en una lista :) cool !!
    texto = texto.split()
    #con este ciclo for recorro la lista convertida - texto
    for c in texto:
        #saco el indice de la lista texto y guardo en indice_texto
        indice_texto = texto.index(c)
        #comparo si c es igual a la palabra que queremos sensurar y ejecuto
        if c == palabra:
            #comvierto la palabra en una lista para separar sus letras.
            palabra_c_lista = list(c)
            #recorro la lista con el ciclo for dentro de nuestra nueva lista que era la palabra.
            for i in palabra_c_lista:
                #saco el indice de la lista, reemplazo cada letra de la palabra con *, y luego con .join vuelvo a hacerla string
                indice = palabra_c_lista.index(i)
                palabra_c_lista[indice] = "*"
                palabra_cambiada = "".join(palabra_c_lista)
            #cada palabra de texto segun el indice que tengo, guardo el resultado anterior de palabra cambiada
            texto[indice_texto] = palabra_cambiada
    #la lista texto la conviero a string otra vez
    texto =" ".join(texto)
    #retorno el texto
    return texto

        


texto_ingresado = raw_input("Ingresa el texto,\no frase en la que quieres censurar la palabra")
print
palabra_censurar = raw_input("Que palabra deseas censurar?")
print
print censor(texto_ingresado,palabra_censurar)