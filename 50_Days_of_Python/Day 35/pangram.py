

sentence = "the quick brown fox jumps over the lazy dog"
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
print(is_pangram(sentence)) #True