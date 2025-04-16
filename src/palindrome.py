def is_palindrome(text):
    clean_text = clean_text_function(text)
    return clean_text == clean_text[::-1]
