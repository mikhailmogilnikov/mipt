input_string = input("Введите несколько слов, разделённых пробелами: ")
words = input_string.split()
reversed_words = [word[::-1] for word in words]
sorted_reversed_words = sorted(reversed_words)
for word in sorted_reversed_words:
    print(word)