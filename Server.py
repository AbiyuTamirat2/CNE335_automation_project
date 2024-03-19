# This is the template code for the CNE335 Final Project
# Abiyu Gebremeskel
# CNE 335 Winter
# Reference: https://tinyurl.com/bd4wk78

import os
import paramiko


class Server:
    """ Server class for representing and manipulating servers. """

    # Setting up the server's IP, Creating SSH client and private key
    def __init__(self, server_ip, key_file):
        self.server_ip = server_ip
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(key_file)

    # Check if the server is reachable by pinging it
    def ping(self):
        # TODO - Use os module to ping the server
        if os.system(f"ping -n 5  {self.server_ip}") == 0:
            return True
        else:
            return False

    # Run command on the server through SSH
    def run_a_command(self, command):
        self.ssh.connect(hostname=self.server_ip, username="ubuntu", pkey=self.key)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        line = stdout.readline()
        while line:
            print(line)
            line = stdout.readline()
            print(stderr.read().decode().splitlines())

    # Close the SSH connection
        self.ssh.close()
