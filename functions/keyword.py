def getUserDetail(name,age,email,status):
    print(f"Name = {name} age = {age} email = {email} status = {status}")

getUserDetail("ram","ram@gmail.com","23",True)    #this doesn't know the order, so it will print in a line accordingly
getUserDetail(name="ram",email="ram@gmail.com",status=True,age=22) #since we've used keyword arguments, we can pass them in any order

