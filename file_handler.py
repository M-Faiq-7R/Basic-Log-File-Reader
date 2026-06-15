### Functions ###

def read_file():                       # reads file and stores all its data in a list 
    data = []
    with open("logs.txt",'r') as file:
        for line in file:
            data.append(line)
    return data

def positive_negative_entries(data):       # Main Function    # It manages all the instructions and data
    
    p_entries = 0
    n_entries = 0
    failed = []
    ip_set = set()
    for d in data:
        u_ip = ip_find(d)
        ip_set.add(u_ip)
        if "LOGIN_SUCCESS" in d:
            p_entries = p_entries + 1
        elif "LOGIN_FAILED" in d:
            n_entries = n_entries + 1
            failed.append(d)
    return p_entries,n_entries , u_ip , failed

def ip_find(line):  # returns ip
    l_data = line.split()
    if len(l_data) >= 3:
        ip_str = (l_data[2])
        return ip_str
    else:
        pass
     
    