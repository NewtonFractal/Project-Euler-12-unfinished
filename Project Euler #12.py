import time
start = time.time()
sums = [1]
primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def triangle_number(w):
    for y in range(2,w+1):
        sums.append(int(((y+1)*y)/2))
    print(sums)

triangle_number(50)

end = time.time()
print(end - start)

def Highly_divisible_triangular_number(what):
    for z in sums:
        for x in primelist:
            factor = True
            while factor == True:
                if number % x != 0:
                    factor = False
                    break
                Factors.append(x)
                number = int(number/x)
            if x > number+ 1:
                break
        for y in range(103, number + 1, 2):
            prime = True
            for x in primelist2:
                if y % x == 0:
                    prime = False
                    break
                if x > math.sqrt(y):
                    break
            if prime == True:
                primelist2.append(y)
                factor2 = True
                while factor2 == True:
                    if number % y != 0:
                        factor2 = False
                        break
                    Factors.append(y)
                    number = number / y
                    if y > number + 1:
                        break
                if y > number + 1:
                    break
            if y > number + 1:
                break

primefactoring(int(number))
print(Factors)
end = time.time()
print(end - start)
