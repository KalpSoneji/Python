#sales = [7 days]
#how much dispunt you want?
#10
#[100,200...]
#aftedis[90,180...]

sales = [100, 200, 300, 400, 500, 600, 700]

discount = int(input("Enter discount: "))

print(sales)

final = list(map(lambda sale : int(sale - (sale * discount)/100) , sales))

print(final)