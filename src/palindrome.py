def is_palindrome(text):
    clean_text = clean_text_function(text)
    return clean_text == clean_text[::-1]

def comparar_caracteres(texto_limpio):
    return texto_limpio == texto_limpio[::-1]

if __name__ == "_main_":
    try:
        while True:
            entrada = input("Ingresá una palabra o frase para verificar si es un palíndromo: ")
            if is_palindrome(entrada):
                print("¡Es un palíndromo!")
            else:
                print("No es un palíndromo.")
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")