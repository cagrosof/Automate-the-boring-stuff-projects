def collatz(y):
    
    if (y)%2 == 0:
        y = y//2
        return y 
    else:
        y= 3*y+1
        return y 

print("Input a number:")

try:
    x = int(input())
except:
    print("Not that")


while not x == 1:
    print(collatz(x))
    x=collatz(x)
    

