def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

sentence = input("Enter a sentence: ")
print(f"Original: {sentence}")
print(f"Reversed: {reverse_words(sentence)}")
