#Practicing Python Operators with a Devops mindset.

#Arithmetic Operators
total_space_gb = 100
used_space_gb = 65
free_space_gb = total_space_gb - used_space_gb
used_percentage = (used_space_gb/total_space_gb)*100

#Assignment Operator
threshold_percentage = 70
threshold_percentage += 5

#Relational Operators
if used_percentage > threshold_percentage:
    print("WARNING : Disk usage above threshold. Consider Cleanup.")
else:
    print("Disk usage is within limits.")

#Logical Operators
has_logs = True
has_temp_files = False
if has_logs or has_temp_files:
    print("Cleanup Possible: Logs or temporary files found.")
else:
    print("No cleanup files found.")

#Membership Operators
cleanup_list = ["logs","temp_files","cache"]
if "logs" in cleanup_list:
    print("Logs found in cleanup list.")
else:
    print("Logs not found in cleanup list.")

if "backups" not in cleanup_list:
    print("Backups not included in cleanup list.")
else:
    print("Backups included in cleanup list.")

