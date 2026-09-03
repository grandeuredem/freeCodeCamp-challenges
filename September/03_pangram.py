def is_pangram(sentence, letters):
    mod_sentence = set()
    sentence = sentence.lower()
    for char in sentence:
        if char.isalpha():
            mod_sentence.add(char)
    return mod_sentence == set(letters)

print(is_pangram('A b c a a b c-a','abc'))
