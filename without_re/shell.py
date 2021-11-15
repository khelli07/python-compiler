import basic

while True:
    text = input(">> ")
    result, error = basic.run("<stdin>", text)

    if error:
        error.print_error()
    else:
        print(result)
