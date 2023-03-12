# Celine Watcharaapakorn-Smith
# Automate_Ping
# CNE 335

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Celine Watcharaapakorn-Smith")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = "3.15.21.156"
    rsa_key = r"C:\Users\celin\Downloads\Celine_Launch_and_Connect.ppk"
    my_serv = Server(server_ip, rsa_key)
    # TODO - Call Ping method and print the results
    print(my_serv.ping())
    ssh_result = my_serv
    print(ssh_result)
