#1. Basic - Print al integers from 0 to 150.
#Made it inclusive of start 0 and stop 150 in what gets printed by
#making the end of the range 151
for i in range(0,151):
    print(i)
    
#2. Multiples of Five
#Added stepwise of 5 to the range method
for i in range(5,1001,5):
    print(i)
    
#3. Counting, the Dojo Way
for i in range(1,101):
    if (i%10 == 0):
        print("Coding Dojo")
    elif (i%5 == 0):
        print("Coding")
    else:
        print(i)
        
#4. Whoa. That Sucker's Huge
j = 0
for i in range(500000):
    j += i
print(j)

#5. Countdown by Fours
for i in range(2018,0,-4):
    print(i)
    
mult = 3
lowNum = mult
highNum = 9
for i in range(lowNum,highNum+1,mult):
    print(i)