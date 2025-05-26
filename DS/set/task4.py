#find who have attended all city event
#find all unique persons
#find who have attended udaipur event but not mumbai's

events = [{"Ahme_Event":["ram","amit","shyam","ram"]},{"Udaipur_Event":["ram","amit","kunal"]},{"mumbai_Event":["ram","parth","amit","ajay","jay"]}]
name_set = set()
ahm_set = set()
uda_set = set()
mum_set = set()

ahm = events[0]
udaipur = events[1]
mumbai = events[2]

ahm_names = events[0].values()
udaipur_names = events[1].values()
mumbai_names = events[2].values()

for names in ahm_names:
    for name in names:
        ahm_set.add(name)
        name_set.add(name)

for names in udaipur_names:
    for name in names:
        uda_set.add(name)
        name_set.add(name)

for names in mumbai_names:
    for name in names:
        mum_set.add(name)
        name_set.add(name)

print(ahm_set.intersection(uda_set).intersection(mum_set)) #attended all events

print(name_set) #unique persons list

print(uda_set.difference(mum_set)) #attended udaipur but not mumbai