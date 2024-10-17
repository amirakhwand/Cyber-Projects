import socket

def scan_port(target_ip, port):
    """
    Attempts to connect to a specific port on a target IP address.
    Args:
        :param target_ip: the IP address of the target machine
        :param port: The port number to scan
        
    Returns:
        :return: 
        True if the port is open, False otherwise.
    """

    try:
        sock = socket.socket(socket.AF_INET, socket,SOCK_STREAM)
        sock.settimeout(1)

    #Set a timeout for the connnection attempt
        sock.connect((target_ip, port))
        sock.close()
        return True
    except:
        return False

if __name__ == '__main__':
    target_ip = input('Enter IP Address: ')
    for port in range(1,1025): #Scan ports 1 to 1024
        if scan_port(target_ip, port):
            print(f'Port {port} is open on {target_ip}')