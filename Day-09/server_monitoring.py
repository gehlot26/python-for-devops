#Practice example using loops, break and continue statement.

servers = ["web-server-1","test-server","web-server-2","db-server-1"]
print("Starting Infrastructure Monitoring...\n")

for server in servers:
    if server == "test-server":
        print("\nSkipping test server: ",server)
        continue
    print("Checking server: ",server)

#While loop for stimulating 3 monitoring attempts
    attempt = 1
    while attempt <=3:
        print("Health Check Attempt", attempt, "for",server)

#stop monitoring if critical issue detected 
        if server == "web-server-2":
            print("Critical issue detected on", server)
            break
        attempt += 1

#Stop checking other services if critical issue found
    if server == "web-server-2":
        print("Stopping monitoring due to critical server failure.")
        break

print("\nMonitoring process finished.")