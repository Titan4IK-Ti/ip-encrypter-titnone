def replace_dots_with_custom_words(input_str):
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

    replaced_str = ''.join(replacements.get(char, char) if char != '.' else replacements[char][i % 3] for i, char in enumerate(input_str))
    return replaced_str

result1 = "Hello my ip is: 123.456.789.0"
result2 = replace_dots_with_custom_words(result1)

print(result2)
