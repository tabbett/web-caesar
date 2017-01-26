
def rotate_character(char, rot):
    if rot > 26:
        rot = rot%26
    if char.isalpha():
        new_position = ord(char) + rot
        if char.isupper() and new_position <= 90:
            return chr(new_position)
        elif char.isupper():
            return chr(new_position-26)
        elif new_position <=122:
            return chr(new_position)
        else:
            return chr(new_position - 26)
    else:
        return char        

def encrypt(text, rot):
    # rotate characters in list and append on new list
    secret_message = ""
    for char in text:
        secret_message += rotate_character(char,rot)
    return secret_message