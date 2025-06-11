class User:

    def __userData(self):
        print("Fnc called")

    def get(self):
        self.__userData()

u = User()
u.get()

# this is how we call a function which is private