i = 1
while i<=200:
    if i % 5 == 0 and i % 7 == 0 :
        print("FizzBuzz, ", end =" ")
        i+=1
    elif i % 5 == 0:
        print("Fizz, ", end =" ")
        i+=1
    elif i % 7 == 0:
        print("Buzz, ", end =" ")
        i+=1
    else:
        print(f"{i}, ", end =" ")
        i+=1