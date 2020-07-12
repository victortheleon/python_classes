been_called = False

def example2():
    global been_called
    been_called = True

# example2()
# print(been_called)

def sort_words_by_length():
    fin = open('words.txt')
    lt = []
    for line in fin:
        line = line.strip()
        lt.append((len(line), line))
    lt.sort(reverse=True)
    res = []
    for _, word in lt:
        res.append(word)
    return res

x = sort_words_by_length()
print(x[0])
