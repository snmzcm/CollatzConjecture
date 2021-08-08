
__author__ = "Ali Cem Sonmez(snmzcm)"
__license__ = "MIT License"
__version__ = "1.1"

# Contributers:-
# [Misnad](https://github.com/Misnad)



def main():
    def ParityCheck(numberX: int):
            if numberX % 2:
                return False
            return True


    def Collatz(x):
            if ParityCheck(x):
                print(x,"\t-Even Number")
                x = x // 2
                if x == 1:
                    print(1, "\t-Odd Number\n\n")
                    return 1
                Collatz(x)
            else:
                print(x, "\t-Odd Number")
                Collatz(3 * x + 1)


    while True:
        numb = int(input("Enter a positive integer: "))
        if numb > 0:
            Collatz(numb)
        else:
           print("Number has to be a positive integer, Try again!")


if __name__=='__main__':
    main()