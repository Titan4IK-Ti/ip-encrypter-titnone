def create_reverse_replacements(replacements):
    reverse_replacements = {}
    for key, value in replacements.items():
        if isinstance(value, list):
            for i, word in enumerate(value):
                reverse_replacements[word.strip()] = key
        else:
            reverse_replacements[value.strip()] = key
    return reverse_replacements

def decrypt_custom_words(input_str, reverse_replacements):
    decrypted_str = ''.join(reverse_replacements.get(word.strip(), word) for word in input_str.split())
    return decrypted_str

replacements = {
    '.': ['because ', 'but ', 'because '],
    '0': 'animal ',
    '1': 'banana ',
    '2': 'beauty ',
    '3': 'bicycle ',
    '4': 'carbon ',
    '5': 'champion ',
    '6': 'company ',
    '7': 'diesel ',
    '8': 'economy ',
    '9': 'finish '
}

reverse_replacements = create_reverse_replacements(replacements)

encrypted_str = "banana beauty bicycle because carbon champion company but diesel economy finish because animal" # crypted ip example
decrypted_str = decrypt_custom_words(encrypted_str, reverse_replacements)

print(decrypted_str)
