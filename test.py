import dictionary

testimport = {
    'abc':1,
    'def':2
}

dictionary.listDictProps(testimport)

TRUE = 1
FALSE = 0
inputRange = range(2, 100)

#check whether the number is prime
def isPrimeNumber(num):
    bPrime = TRUE
    if num == 4:
         return FALSE
    lstDivisors = range(2, num // 2)
    for divisor in lstDivisors:
        if num % divisor == 0:
            bPrime = FALSE
            break

    return bPrime


#print all prime numbers in range
def printPrimeNumbers(inputRange = range(2, 10)):
    for num in inputRange:
        if isPrimeNumber(num) == TRUE:
            print(num, "is Prime number")

#return average of numbers
def numAverage(*args):
    count = 0
    total = 0
    for num in args:
        total += num
        count += 1
        
    avg = total / count
    return avg
    
        
#print(inputRange)
#printPrimeNumbers(inputRange)
avglist = [2, 4, 6, 8]
print(numAverage(*range(2,10, 2)))
print(avglist)














    



