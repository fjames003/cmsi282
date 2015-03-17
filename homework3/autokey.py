def autokey_vigenere_encode(plain, key):
    plain_points = convert_codepoint(plain.upper())
    key_points = convert_codepoint(key.upper())
    cipher_points = []
    
    for i,c in enumerate(plain_points):
        if i < len(key_points):
            cipher_points.append(65 + ((c + key_points[i]) % 26))
        else:
            print((c + plain_points[i - len(key_points)]) % 26)
            cipher_points.append(65 + ((c + plain_points[i - len(key_points)]) % 26))

    print cipher_points
    return convert_text(cipher_points)

def autokey_vigenere_decode(cipher, key):
    pass

def convert_codepoint(text):
    codepoints = [ord(c) for c in text]
    return codepoints

def convert_text(codepoints):
    text = ""
    for i in codepoints:
        text += chr(i)
    return text


trial = "TAKEACOPYOFYOURPOLICYTONORMAWILCOXONTHETHIRDFLOOR"
trial = trial.lower()
print(autokey_vigenere_encode(trial, "quark"))
print("JUKVKVOZCOHMDSFUMZCTNHZVQPFOJWCOOTWYVVBHUBYHYSWFU")