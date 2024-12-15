words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for k, v in words.items():
    i = 0
    response = []
    while v > i:
        response.append(k)
        i += 1
    print(''.join(response))
