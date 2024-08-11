class Server:

    def __init__(self, ipAddress, os, ram, typeOfStorage, serverName):

        self.ipAddress = ipAddress

        self.os = os

        self.ram = ram

        self.typeOfStorage = typeOfStorage

        self.serverName = serverName

        self.status = "stopped"

    def start(self):

        if self.status == "started":

            print("Server is already started")

        else:

            self.status = "started"

            print("Server started in", self.ipAddress)

    def stop(self):

        if self.status == "stopped":

            print("Server is already stopped")

        else:

            self.status = "stopped"

            print("Server stopped")

    def getServerDetails(self):

        print(self.serverName, self.os, self.ram, self.ipAddress, self.status)

# Content Server Class
class ContentServer(Server):
    def __init__(self, ipAddress, os, ram, typeOfStorage, serverName, backuprRecovery, accessControl, loggingMonitoring, location):
        super().__init__(ipAddress, os, ram, typeOfStorage, serverName)
        self.backupRecovery = backuprRecovery
        self.accessControl = accessControl
        self.loggingMonitoring = loggingMonitoring
        self.location = location

    def getServerDetails(self):

        print(self.serverName, self.os, self.ram, self.ipAddress, self.status,self.backupRecovery, self.accessControl, self.loggingMonitoring)

# Deployment Server class

class DevlopmentServer(Server):
    def __init__(self, ipAddress, os, ram, typeOfStorage, serverName, portConfiguration, virtualHost, securitySettings, loadBalancer):
        super().__init__(ipAddress, os, ram, typeOfStorage, serverName)
        self.portConfiguration= portConfiguration
        self.virtualHost = virtualHost
        self.securitySettings = securitySettings
        self.loadBalancer = loadBalancer


# Database Server class
class DataBaseServer (Server):
    def __init__(self, ipAddress, os, typeOfStorage, ram, serverName,storageEngine, performanceTunning, logsCollector):
        super().__init__(ipAddress, os, typeOfStorage, ram, serverName)
        self.storageEngine = storageEngine
        self.performanceTunning = performanceTunning
        self.logsCollector = logsCollector
    




server2 = DataBaseServer("localHost", "Linux", 256, "HDD", 112, "RHEL", "TDP", "EXTRADB")

server2.getServerDetails()