def is_pangram(sentence, letters):
    mod_sentence = ''
    sentence = sentence.lower()
    for char in sentence:
        if char.isalpha():
            mod_sentence += char
    return all(x in letters for x in mod_sentence) and all(x in mod_sentence for x in  letters)

print(is_pangram('A b c a a b c-a','abc'))
