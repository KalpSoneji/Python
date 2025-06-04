def isValid(func):
    
    def inner(data, query):
    
        if query in data:
            func()  
        else:
            print("string is not valid...")
    
    return inner

@isValid
def getData():
    print("data is valid...")

getData("royal", "b")