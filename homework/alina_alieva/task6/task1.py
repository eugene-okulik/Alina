text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
new_list = []
for word in words:
    word = word + 'ing'
    ending = word.endswith('.ing')
    if ending is True:
        word = word.replace('.ing', 'ing.')
        # print(word)
    else:
        word = word.replace(',ing', 'ing,')
        # print(word)
    new_list.append(word)
print(' '.join(new_list))
