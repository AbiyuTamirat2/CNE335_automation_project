# This is the template code for the CNE335 Final Project
# Abiyu Gebremeskel
# CNE 335 Winter
# Reference: https://tinyurl.com/bd4wk78

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Abiyu")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    my_server = Server("34.219.128.55", r'C:\Users\abiyu\Downloads\Final_Project_key.pem')
    # TODO - Call Ping method and print the results
    if my_server.ping():
        my_server.run_a_command("sudo apt update && sudo apt-get upgrade -y")
