def anti_vocal(cadena):
    cadena_sin_vocales = list(cadena)
    lista_vocales = list("aeiouAEIOU")
    for c in cadena_sin_vocales:
        if c in lista_vocales:
            indice = cadena_sin_vocales.index(c)
            cadena_sin_vocales[indice] =""
            cadena_final = "".join(cadena_sin_vocales)
    return cadena_final
    
cadena = raw_input("Ingresa la palabra,\nfrase o lo que sea en que quieras \"eliminar\" las vocales :): " )