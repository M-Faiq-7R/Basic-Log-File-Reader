import file_handler as fh

               
#### Processing ###
data = fh.read_file()           
total_entries = len(data)
p_entry , n_entry , u_ip , failed , ip_set = fh.positive_negative_entries(data)
most_active_ip , active_ip_count , sus_ips = fh.count_ip(data)


print(f"Total Entries := {total_entries} \n Passed Enteries := {p_entry}  \n Failed Enteries := {n_entry} ")
for i in range (len(failed)) :
    print(f"{i}. Failed Log: {failed[i]}" , end='')
print(f"Failure Rate : {len(failed)/len(data) * 100} %")
print(f"Most active ip := {most_active_ip} with count {active_ip_count}")
print(f"Sus Ips :")
for i in sus_ips:
    print(i)
