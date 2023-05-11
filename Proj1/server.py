from socket import *
import random


port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
s_soc.listen(1)
ServerName = "Server of Cameron Holbrook"
print(ServerName + " is now ONLINE")

while True:

        con, addr = s_soc.accept()
        data = con.recv(1024).decode()
        data = data.split(" ")
        name = data[0] + " " + data[1]
        num = data[2]
        num = (int)(num)

        print("Client: " + name + ", Server: " + ServerName)
        num2 = random.randint(1,100)
        num = num + num2

        string1 = "Servername: " + ServerName + ", Generated Value: " + (str)(num2) + ", Sum: " + (str)(num)

        con.send(string1.encode())
        print("Sent")
        con.close()
