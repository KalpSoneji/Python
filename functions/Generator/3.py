def get_users(batch_size=10):
    total_users = 100
    for i in range(0,total_users,batch_size): #loop will run from 0 to 99 in increments of 10 (batch_size)
        
        batch=[] #new list

        for j in range(i,min(i+batch_size,total_users)): #this loop will start from i = 0 and will go until next 10 users but not beyond that
            batch.append(f"user{j}") #adds users to batch
        
        yield batch #Instead of returning all batches at once, the function uses yield to make it a generator.
        # It pauses and returns one batch at a time, resuming from where it left off in the next iteration.

for b in get_users():
    print(b)         # prints all the users