#Lists and Tuples Practice

#List of servers (can change)
servers = ["web-server-1","web-server-2","db-server-1"]

#Tuple of Allowed Service ports (fixed config)
allowed_ports = (22,80,443)

print("Servers in Infrastructure: ")
print(servers)
print("\nAllowed Service Ports: ")
print(allowed_ports)

#Asks user which port they want to check
port = int(input("\nEnter a Port Number to check: "))

if port in allowed_ports:
    print("Port",port,"is an allowed service port.")
else:
    print("Port",port,"is not part of standard service configuration.")

#Add new service dynamically
new_server = input("\nEnter a new server to add to inventory: ")
if new_server:
    servers.append(new_server)
    print("\nServer Added Successfully.")
else:
    print("\nNo Server Added.")

print("\nUpdated Server Inventory: ")
print(servers)

print("***********************************")
