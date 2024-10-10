
SSH Brute Force Script
This script attempts to brute force SSH credentials by trying multiple passwords from a file until it successfully logs in or exhausts the list of passwords. The script uses the paramiko library to establish SSH connections.

How It Works
The script asks the user for:

SSH server IP address.
SSH username.
Path to a file containing a list of passwords.
It then attempts to log in to the SSH server using each password from the password list, one at a time.

If the login is successful, the script prints the correct credentials (username:password) and stops further attempts.

If the login fails, the script moves on to the next password in the list.

A 1-second delay between each attempt is added to avoid detection by SSH servers with brute-force protections.

Usage
Install Dependencies
Make sure you have Python installed along with the paramiko library. You can install paramiko using pip:

copy:
pip install paramiko
-------
Prepare Input Files

Prepare a text file containing passwords, with one password per line (e.g., passwd.txt).
Prepare a text file with a list of usernames, or use a single username input
 
Run the Script Execute the script in your terminal:
copy:
python3 ssh_brute_force.py
-------

The script will prompt you to enter:

The SSH server's IP address.
The SSH username.
The path to the password file.
Example

SSH Server IP:
Username: admin
Password file: /home/kali/Desktop/GitHub/passwd.txt
Example command to run:

copy:
python3 ssh_brute_force.py
-------

-------------------------------------------
Notes
The script is designed for ethical hacking and penetration testing within legal boundaries.
Unauthorized access to systems is illegal and punishable by law.
--------------------------------------------

