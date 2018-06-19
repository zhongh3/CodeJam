def reverse_words(string):
    words = string.split()  # list
    words.reverse()
    return " ".join(words)
    # return " ".join(reversed(words))


cases = int(input())
# print(cases)

for case in range(1, cases+1):
    x = input()
    print("Case #{}: {}".format(case, reverse_words(x)))
    # print("Case #", case, ": ", reverse_words(x))


