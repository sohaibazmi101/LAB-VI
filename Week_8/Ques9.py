def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

def is_palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]

user_input = input("Enter a sentence: ")

reversed_sentence = reverse_words(user_input)
print("Words in reverse order:", reversed_sentence)

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
