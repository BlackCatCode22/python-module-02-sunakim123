#Payroll Program with Overtime
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)


#add exception handling to your payroll program
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)


#code up a program that uses a function named compute pay
def computepay(hours, rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp

    else:
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay:", xp)


#code up using nested if statements
a = int(input("Enter the first numeber: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("The largest of", a,b,c,"is",largest)


