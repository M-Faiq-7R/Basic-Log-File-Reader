### Functions ###

def read_file():                       # reads file and stores all its data in a list 
    data = []
    with open("logs.txt",'r') as file:
        for line in file:
            data.append(line)
    return data

def positive_negative_entries(data , i=1):       # Main Function    # It manages all the instructions and data
    
    p_entries = 0
    n_entries = 0
    failed = []
    ip_set = set()
    ip_total = []
    for d in data:
        ip = ip_find(d)
        ip_total.append(ip)
        ip_set.add(ip)
        if "LOGIN_SUCCESS" in d:
            p_entries = p_entries + 1
        elif "LOGIN_FAILED" in d:
            n_entries = n_entries + 1
            failed.append(d)
    if i == 1:
        return p_entries,n_entries , ip , failed, ip_set
    elif i == 0:
        return ip_total

def ip_find(line):  # returns ip
    l_data = line.split()
    if len(l_data) >= 3:
        ip_str = (l_data[2])
        return ip_str
    else:
        pass
     
    
def count_ip(data):
    ip_total = positive_negative_entries(data ,0)
    ip_total_set = set(ip_total)
    sus_ips= []
    ip_count = []
    
    for ip in ip_total_set:
        count = 0                  
        for current_ip in ip_total:
            if current_ip == ip:
                count += 1 
        ip_count.append([ip,count])
        if count >= 3:
            sus_ips.append([ip,count])
        
    
    ip_count_name , ip_count_num = zip(*ip_count)
    
    max_ip = max(ip_count_num)
    index = ip_count_num.index(max_ip) 
    return ip_count_name[index] , max_ip , sus_ips
