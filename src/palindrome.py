def is_palindrome(text):
    clean_text = clean_text_function(text)
    return clean_text == clean_text[::-1]

def comparar_caracteres(texto_limpio):
    return texto_limpio == texto_limpio[::-1]