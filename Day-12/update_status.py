#function to update server status
def update_status(file_path, new_status):

    #read file
    with open(file_path, "r") as file:
        lines = file.readlines()

    #rewrite file with updated status
    with open(file_path, "w") as file:
        for line in lines:

            if line.startswith("status"):
                file.write("status=" + new_status + "\n")
            else:
                file.write(line)
    
#main program
file_name = "server.conf"
print("Updating Server Status...")
update_status(file_name, "stopped")
print("Server Status Updated Successfully.")

