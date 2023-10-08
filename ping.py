import socket

def ping(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"{colorama.Fore.GREEN}CONNECTED {colorama.Fore.WHITE} . . {colorama.Fore.CYAN}Successful connection to {colorama.Fore.BLUE}{ip}{colorama.Fore.WHITE} at port {colorama.Fore.BLUE}{port}{colorama.Fore.WHITE} . . {colorama.Fore.GREEN}CONNECTION UP!{colorama.Fore.WHITE} . .")
    except:
        print(f"{colorama.Fore.LIGHTRED_EX}DOWN {colorama.Fore.WHITE} . . {colorama.Fore.YELLOW}Unsuccessful connection to {colorama.Fore.RED}{ip}{colorama.Fore.WHITE} at port {colorama.Fore.RED}{port}{colorama.Fore.WHITE} . . {colorama.Fore.GREEN}CONNECTION DOWN!{colorama.Fore.WHITE} . .")
