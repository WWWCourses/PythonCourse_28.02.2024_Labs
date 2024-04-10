words = []
while True:
    word = input()
    if word == '':
        break
    words.append(word)
filtered_word = []
for word in words:
    if word not in filtered_word:
        filtered_word.append(word)
for word in filtered_word:
    print(word)
