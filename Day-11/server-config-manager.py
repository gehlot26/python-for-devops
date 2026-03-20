#Example to understand Dictionaries in Python.

servers = {
    "server1":
    {
        "name" : "web-server-1",
        "ip" : "192.168.1.10",
        "status" : "running",
        "env" : "production"
    },
    "server2":
    {
        "name" : "db-server-1",
        "ip" : "192.168.1.20",
        "status" : "stopped",
        "env" : "staging",
    }
}

print("Available Servers: ")
print(list(servers.keys()))

try:
    choice = input("\nEnter Server Key (server1/server2): ")
    server = servers[choice]

    print("\nServer Details: ")
    print("Name: ", server["name"])
    print("IP: ",server["ip"])
    print("Status: ",server["status"])
    print("Environment: ",server["env"])

    #Update status
    new_status = input("\nEnter new status (running/stopped): ")
    server["status"] = new_status
    print("\nUpdated Server Details: ")
    print(server)
except KeyError:
    print("Invalid server key. Please select correct server.")

