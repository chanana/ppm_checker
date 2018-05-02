#Returns the mass range given a ppm and a reference mass
def plus_minus(reference, ppm):
    mass_upper = reference * (1 + (ppm * 1e-6))
    mass_lower = reference * (1 - (ppm * 1e-6))
    return(mass_lower, mass_upper)

# Checks if string is float or not
def isFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

# Keeps running until user enters 'q'
i = 'a' # just an initial value of i
while i != 'q':
    try:
        ref, ppm = raw_input("\nEnter mass <space> ppm: ").split()
    except ValueError:
        print("\nTry entering TWO values\n")
        continue
    if isFloat(ref) and isFloat(ppm): # if they are both floats,
        print(plus_minus(float(ref), float(ppm)))
    else:
        print("\nPlease enter a number! -_- \n")
    i = raw_input("\nEnter 'q' to quit or anything else to continue: ")
