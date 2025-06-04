def outer():
    print("Outer fnc called...")

    def inner():
        print("Inner fnc called...")
    
    inner()

outer()