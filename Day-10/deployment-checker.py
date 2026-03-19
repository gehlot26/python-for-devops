#Mini Project : Functions + Lists + Exception Handling

servers = ["web-server-1","web-server-2","db-server-1"]

#function to display servers
def show_servers():
    print("\nAvailable Servers: ")
    for i in range(len(servers)):
        print(i,"->", servers[i])

#function to select server
def select_server():
    try:
        index = int(input("\nEnter Server Number: "))
        server = servers[index]
        return server
    except ValueError:
        print("Invalid Input, please enter a number.")
        return None
    except IndexError:
        print("Server does not exist.")
        return None

#function to simulate deployment check
def deploy(server):
    if server is None:
        print("Deployment Cancelled.")
        return
    print("\nDeploying Application to: ",server)

    #simulated condition
    if server == "web-server-2":
        print("Deployment failed due to configuration issue.")
    else:
        print("Deployment Successful")

show_servers()
selected = select_server()
deploy(selected)

