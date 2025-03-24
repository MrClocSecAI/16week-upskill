def add(a, b): # Function-takes inputs
    result = a + b
    return result # Outputs result

def subtract(a, b): # New function
    return  a - b # One-line magic

x = 32
y = 74

total = add(x, y) #Call it
print("Jazzy Total:", total)

diff = subtract(x, y)
print("Funky Diff:", diff)

if total > 12: # Condition
    print("Big Freakin' total!")
else:
    print("Teensy total.")

if diff > 12: # Another condition
    print("That Diff is Still a Big Freakin' number!")
else:
    print("That Diff is gettin' to be a tiny number!")
