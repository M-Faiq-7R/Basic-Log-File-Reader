data = [] # Stores all data from file
ip_set = set()

### Functions ###
def read_file():
    global data
    with open("logs.txt",'r') as file:
        for line in file:
            data.append(line)

def positive_negative_entries():
    global data
    p_entries = 0
    n_entries = 0
    failed = []
    for d in data:
        u_ip = ip_find(d)
        if "LOGIN_SUCCESS" in d:
            p_entries = p_entries + 1
        elif "LOGIN_FAILED" in d:
            n_entries = n_entries + 1
            failed.append(d)
    return p_entries,n_entries , u_ip , failed

def ip_find(line):  # 2026-06-12 LOGIN_FAILED 192.168.1.10
    global ip_set
    l_data = line.split()
    ip_set.add(l_data[2])
    return len(ip_set)
     
    
                      
#### Processing ###
read_file()           
total_entries = len(data)

p_entry , n_entry , u_ip , failed = positive_negative_entries()

print(f"Total Entries := {total_entries} \n Passed Enteries := {p_entry}  \n Failed Enteries := {n_entry} \n Unique IPs = {len(ip_set)}")
print(f"Failed Log: {failed} \n Failure Rate : {len(failed)/len(data) * 100} %" )

