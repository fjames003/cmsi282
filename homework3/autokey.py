def autokey_vigenere_encode(plain, key):
    cipher_points, key_points, plain_points = [], convert_codepoint(key.replace(" ", "").upper()), convert_codepoint(plain.replace(" ", "").upper())
    
    for i,c in enumerate(plain_points):
        if i < len(key_points):
            cipher_points.append(65 + ((c + key_points[i]) % 26))
        else:
            cipher_points.append(65 + ((c + plain_points[i - len(key_points)]) % 26))

    return convert_text(cipher_points)

def autokey_vigenere_decode(cipher, key):
    cipher_points, key_points, plain_points = convert_codepoint(cipher.upper()), convert_codepoint(key.upper()), []
    
    for i,c in enumerate(cipher_points):
        if i < len(key_points):
            plain_points.append(65 + ((c - key_points[i]) % 26))
        else:
            plain_points.append(65 + ((c - plain_points[i - len(key_points)]) % 26))

    return convert_text(plain_points)

def convert_codepoint(text):
    codepoints = [ord(c) for c in text]
    return codepoints

def convert_text(codepoints):
    text = ""
    for i in codepoints:
        text += chr(i)
    return text


trial = "Attack at dawn"
cipher = autokey_vigenere_encode(trial, "frankie")
print(cipher)
plain = autokey_vigenere_decode(cipher, "frankie")
print(plain)

