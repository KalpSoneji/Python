# create function accept kwargs if type of any key is not string
# raise TypeError with message "Only string keys are allowed"

def accept_kwargs_dict(data):
    
    try:
        for key in data:
            if type(key) is not str:
                raise TypeError("Only string keys are allowed")
        print("Accepted kwargs:", data)
    
    except TypeError as e:
        print("Error:", e)

d = {1: "math", "name": "Kalp"}
accept_kwargs_dict(**d)  