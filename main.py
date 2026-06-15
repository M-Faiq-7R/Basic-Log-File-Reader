import file_handler as fh

               
#### Processing ###
data = fh.read_file()           
total_entries = len(data)

p_entry , n_entry , u_ip , failed = fh.positive_negative_entries(data)

print(f"Total Entries := {total_entries} \n Passed Enteries := {p_entry}  \n Failed Enteries := {n_entry} ")
for i in range (len(failed)) :
    print(f"{i}. Failed Log: {failed[i]}")
print(f"Failure Rate : {len(failed)/len(data) * 100} %")

