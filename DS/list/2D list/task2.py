'''
please entrt y for continue and 'n' for exit
y
enter movie name:
enter relese year:

please entrt y for continue and 'n' for exit
y

enter movie name:
enter relese year:
please entrt y for continue and 'n' for exit
n
[["chava",2025],["abc",2050],[]]
iteration :
for i,j in mopves:


'''

movies = []

while(True):
    
    choice = input("Enter your choice: ")

    if choice == 'y':
        movie_name = input("Enter movie name: ")
        release_year = int(input("Enter release year: "))
        movies.append([movie_name, release_year])

    elif choice == 'n':
        print()
        print(movies)
        print()
        break

    else:
        print("Invalid choice. Please enter 'y' for continue and 'n' for exit.")

for i, j in movies:
    print("Movie name: ", i, "\tRelease year: ", j)
    print()
    