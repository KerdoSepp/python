str = input("Sisesta string: ").strip()

if len(str) >= 6 and len(str) % 2 == 0:
    print(str[int(len(str)/2) - 1:int(len(str)/2) + 2])