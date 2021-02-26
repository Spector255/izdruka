i = 1
a = 14825
while i<=a:
    if i == a:          #Pēdējo komātu noņēmšana :)
        if i % 5 == 0 and i % 7 == 0 :
            print("FizzBuzz", end =" ")
            i+=1
        elif i % 5 == 0:
            print("Fizz", end =" ")
            i+=1
        elif i % 7 == 0:
            print("Buzz", end =" ")
            i+=1
        else:
            print(f"{i}", end =" ")
            i+=1
    else:
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