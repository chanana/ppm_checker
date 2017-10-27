#PPM plus minus calculator
def plus_minus(ref, ppm):
    pls = ref * (1 + (ppm * 1e-6))
    mis = ref * (1 - (ppm * 1e-6))
    return(pls, mis)

while True:
    ref, ppm = [float(x) for x in raw_input("Enter Ref <space> PPM: ").split()]
    print(plus_minus(ref, ppm))
    i = raw_input("Press any key to continue or ENTER to exit")
    if not i:
        break
