S = input()
for i in S.split():
    capitalized_word = i[0].upper() + i[1:]
    print(capitalized_word, end=" ")