def sum_of_words(s):
    words = 0
    flag = 0
    for i in range(len(s)):
        if s[i] != ' ' and flag == 0:
            words += 1
            flag = 1
        else:
            if s[i] == ' ':
                flag = 0
    return words


def min_of_number(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= b and c <= a:
        return c

     
result = min_of_number(sum_of_words('hello world again'), sum_of_words('hello world'), sum_of_words('hello world again and again'))
print(result)




