been_called = False

def example2():
    global been_called
    been_called = True

example2()
print(been_called)