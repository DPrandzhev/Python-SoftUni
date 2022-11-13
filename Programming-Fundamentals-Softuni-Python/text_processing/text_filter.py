filter = input().split(', ')
text = input()

for word in filter:
    text = text.replace(word, '*' * len(word))

print(text)