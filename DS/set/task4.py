#find who have attended all city event
#find all unique persons
#find who have attended udaipur event but not mumbai's

events = [{"Ahme_Event":["ram","amit","shyam","ram"]},{"Udaipur_Event":["ram","amit","kunal"]},{"mumbai_Event":["ram","parth","amit","ajay","jay"]}]

ahm = set(events[0]["Ahme_Event"])
udaipur = set(events[1]["Udaipur_Event"])
mumbai = set(events[2]["mumbai_Event"])
all = ahm.union(udaipur).union(mumbai)

print(ahm.intersection(udaipur).intersection(mumbai)) #attended all events

print(all) #unique persons list

print(udaipur.difference(mumbai)) #attended udaipur but not mumbai  