def individual_list():
    f = open('running-config.cfg')
    t1 = []
    t2 = []
    t3 = []
    for line in f:
        if 'transit_access_in' in line:
            t1.append(line)
        elif:
           'fw-management_access_in' in line:
            t2.append(line)
        elif:
           'global_access' in line:
            t3.appen(line)
     print(t1)
     print(t2)
     print(t3)


