import file_handler as fh
import datetime

def display_report():
    data = fh.read_file()           
    total_entries = len(data)
    p_entry , n_entry , u_ip , failed , ip_set = fh.positive_negative_entries(data)
    most_active_ip , active_ip_count , sus_ips = fh.count_ip(data)
    
    print("=================================")
    print("=================================")
    print("       Log Analyzer Report       ")
    print("=================================")
    
    print("Entries := ")
    print(f" Total Entries : {total_entries}")
    print(f" Passed Entries : {p_entry}")
    print(f" Failed Entries : {n_entry}")
    print(f" Failure Rate : {len(failed)/len(data) * 100} % ")
    print(f" Most active ip : {most_active_ip}  count {active_ip_count} \n")
    
    print(f"Sus ips := ")
    for i in sus_ips:
        print(f" {i[0]} with count {i[1]}")
    print("=================================")
    
    
    further_input_for_processing = int(input("Choose from following options(1/2/3) : \n 1. Show failed logs , \n 2. Save report   \n 3. None \n"))
    if further_input_for_processing == 1:
        for i in range (len(failed)) :
            print(f"{i}. Failed Log: {failed[i]}" , end='')
    elif further_input_for_processing == 2:
        save_file(data , total_entries , p_entry , n_entry , failed , most_active_ip , active_ip_count , sus_ips)
    
    print("Done!")
    
    
    
def save_file(data , total_entries , p_entry , n_entry , failed , most_active_ip , active_ip_count , sus_ips):
    time_ = datetime.datetime.now().strftime("%d-%m-%Y_%H;%M;%S")
    with open (f"log_report_{time_}.txt" , 'x') as file:
        file.write(f" Timed : {time_} \n") 
        file.write("================================= \n")
        file.write("================================= \n")
        file.write("       Log Analyzer Report        \n")
        file.write("================================= \n")
        
        file.write("Entries :=  \n")
        file.write(f" Total Entries : {total_entries} \n")
        file.write(f" Passed Entries : {p_entry} \n")
        file.write(f" Failed Entries : {n_entry} \n")
        file.write(f" Failure Rate : {len(failed)/len(data) * 100} %  \n")
        file.write(f" Most active ip : {most_active_ip}  count {active_ip_count} \n \n")
        
        file.write(f"Sus ips :=  \n")
        for i in sus_ips:
            file.write(f" {i[0]} with count {i[1]} \n")
        file.write("================================= \n")
        
        file.write(f"Failed Logs : \n")
        for i in range (len(failed)) :
            file.write(f"{i}. Failed Log: {failed[i]}")
            
        file.write("================================= \n")
           
