text = input("Input a number of words: ")

words = [word for word in text.split(",")]

print(",".join(sorted(list(set(words)))))
