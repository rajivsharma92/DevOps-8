class Server:
    def __init__(self,hostname, ram,newtworkStatus,deplymentStatus, port):
        self.hostname = hostname
        self.ram = ram
        self.networkStatus = newtworkStatus
        self.deployemntStatus = deplymentStatus
        self.port = port

# Method Start
    def start (self):
        self.networkStatus = "connected".lower()
        self.deployemntStatus = "yes".lower()

        if self.deployemntStatus == "yes" and self.networkStatus == "connected":
            print(self.hostname,":" "Server Started")
        else:
            print(self.hostname, ":" "Internet connection failed")
 
# Method stop
    def stop (self):
        self.networkStatus = "Connected".lower()
        self.deployemntStatus = "yes".lower()

        if self.networkStatus != "connected":
            print(self.hostname, ":" "Server stoped")
        else:
            print(self.hostname, ":" "Server connection failed")

    def status(self):
        if self.networkStatus == "connected":
            print(self.hostname, ":" "Server is working")

        else:
            print(self.hostname, ":" "Server is not working")

server1 = Server("server1", 4,"connected", "yes", 500)

server2 = Server("server2", 2,"not connected", "no", 500)
 
server1.start()

server2.stop()

server1.status()