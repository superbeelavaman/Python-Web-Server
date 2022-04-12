#Web Address for this server to listen to.
#Default address: 
#http://localhost:8080
#hostName = "localhost"
#serverPort = 8080
hostName = "localhost"
serverPort = 8080

#Where HTML Documents are stored.
fileRoot = '/home/superbee/Python Projects/html'

#Filestring type. type "Windows" or "Linux/Mac"
systemType = 'Linux/Mac'

def get():
    return [hostName, serverPort, fileRoot, systemType]
