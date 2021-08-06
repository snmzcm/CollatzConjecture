def main():
    def ParityCheck(numberX):
            numberX = int(numberX)
            numbparity = False
            if numberX % 2 == 0:
                return True
            else:
                return False
    def Collatz(x):
            parity = ParityCheck(x)
            if parity == True:
                x = x // 2
                print(x)
                if x == 1:
                    return 1
                else:
                    Collatz(x)
                    
            elif parity == False:
                x = 3 * x + 1;
                print(x)
                if x == 1:
                    return 1
                else:
                    Collatz(x)
            
        
        
    
    
    
    
    
    
    
    
    numb = int(input("Enter the number\n"))
    Collatz(numb)
    
    
    










main()