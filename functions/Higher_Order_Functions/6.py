def goa(name):
    print("Goa")
    return "Cashew"

def dubai(name):
    print("Dubai")
    return "Date"

def kashmir(name):
    print("Kashmir")
    return "Saffron"

def trip(cb):
    print("Trip function called")
    return cb("Kalp")     

data = None

budget = int(input("Enter budget: "))

if budget>60000:
    data = trip(kashmir) #shi
elif budget>50000:
    data = trip(dubai)    
elif budget>10000:
    data = trip(goa)

print("Item = ",data)    
    