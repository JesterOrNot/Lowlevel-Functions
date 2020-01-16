def reverse_every_other_word(text):
    words = text.split(" ")
    count = 1
    for word in words:
        if count % 2 == 0:
            words[count-1] = reverse(word)
        count += 1
    return " ".join(words)

def reverse(word):
    return "".join([i for i in list(word)[::-1]])

print(reverse_every_other_word("one two three four"))
