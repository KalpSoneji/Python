name = "Kalp "

try:
    if " " in name:
        raise Exception("Space found")
    
    else:
        print(name)

except ValueError as e:
    print("Value Error:", e)