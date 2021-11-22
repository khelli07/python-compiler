for y in range(12, -14, -1):
    for x in range(30, -30, -1):
        if (x/2)**2 + (((5*y)/4) - (2 * (abs(x))**(1/2)))**2 < 120:
            print("*", end="")
        else:
            print(" ", end="")
    print()
