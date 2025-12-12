def upc(number):

    num = str(number)
    
    x = sum([int(num[i]) for i in range(10) if i%2 ==0])
    x *=3
    y = sum([int(num[i]) for i in range (11) if i%2 !=0])
    
    return (x+y)%10

print(upc(12345678910))