def isValid(func):

    def inner(data,query):

        if query in data:
            func(data) #getData(data)
        else:
            print("string is not valid...")        
    
    return inner

@isValid
def getData(data):        
    print("data is valid...",data)

getData("royal","z")    