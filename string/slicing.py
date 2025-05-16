data = "ahmedabad1"

#start, end, increment/decrement

print(data[::])
print("Starting from 4 till end ", data[4::])
print("From start till 4th index: ", data[:5:]) # end index is not included (n-1)
print("Every 2nd char will be printed ", data[::2])
print("Reverse word will be printed ", data[::-1])
print(data[5:2:-1])