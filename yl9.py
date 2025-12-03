a = float(input("A külg: "))
b = float(input("B külg: "))
c = float(input("C külg: "))


if a <= 1 or b <= 1 or c <= 1:
    print("See pole kolmnurk")
else:
    if a == b == c:
        print("Võrdkülgne")
    else:
        if a == b or b == c or a ==c:
            print("Võrdhaarne")
        else:
            print("Erikülgsed")