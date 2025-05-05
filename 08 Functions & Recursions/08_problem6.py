# coverting inches to cm 
# 1 inch = 2.5 cm

def FloatToinch(inch):
    cm = inch * 2.5
    print(f"{cm} cm are the equivalent of {inch} inches")

inch = float(input("Enter the inches: "))
FloatToinch(inch)