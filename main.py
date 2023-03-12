# Celine Watcharaapakorn-Smith
# Automation Project
# CNE 335

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Celine Watcharaapakorn-Smith")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_ip = "3.144.108.187"
    rsa_key = r"C:\Users\celin\Downloads\Celine_Launch_and_Connect.ppk"
    username = 'ubuntu'
    # run upgrade and update command
    upgrade = 'sudo apt update && sudo apt upgrade -y'
    my_serv = Server(server_ip, rsa_key, username, upgrade)
    # TODO - Call Ping method and print the results
    print(my_serv.ping())
    print("Updating server...")
    ssh_result = my_serv.upgrade
    print(ssh_result)
