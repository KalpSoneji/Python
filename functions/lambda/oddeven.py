eo = lambda x : "Even" if x % 2 == 0 else "Odd"

print(eo(4))

max = lambda a, b : a if a > b else b

print(max(3, 5))

# elif doesn't work with lambda

posneg = lambda x : "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")

print(posneg(5))

grade = lambda x : "A" if x > 90 else ("B" if x > 80 else ("C" if x > 70 else "Fail"))

print(grade(65))