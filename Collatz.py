def main():
    def ParityCheck(numberX):
            numberX = int(numberX)
            if numberX % 2 == 0:
                return True
            else:
                return False
    def Collatz(x):
            parity = ParityCheck(x)
            if parity == True:
                print(x," -Even Number")
                x = x // 2
                if x == 1:
                    print(1, " -Odd Number")
                    return 1
                else:
                    Collatz(x)
                    
            elif parity == False:
                print(x, " -Odd Number")
                x = 3 * x + 1;
                if x == 1:
                    print(1, " -Odd Number")
                    return 1
                else:
                    Collatz(x)
    
    
    
    while True:
        numb = int(input("Enter a positive integer\n"))
        if numb > 0:
            Collatz(numb)
        else:
           print("Number has to be a positive integer, Try again!")
    
    










main()