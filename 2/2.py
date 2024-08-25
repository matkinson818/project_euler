# conditions:
# less the 4000000
# has to be even 

num1 = 1
num2 = 1
addr = 0
sum = 0

while addr < 4000000:
    addr = (num1 + num2)
    if addr % 2 == 0:
        sum += addr

    num1 = num2
    num2 = addr 

print(sum)
