# FAIL2BAN IMPLEMENTATION (Metasploit & Custom Python Script)


Phase 3 demonstrates two approaches to counter brute-forcing SSH credentials:
- Using **Metasploit's `fail2ban` auxiliary module**
- A **custom Python script** leveraging `paramiko`

---

## 🧰 Requirements

- Kali Linux (or compatible penetration testing environment)
- Python 3.7+
- Metasploit Framework
- `paramiko` (for the custom script)

---

## DEFENSE MECHANISM

### Defense 1 Changed the Default Password of the Victim 
-Run "passwd" after sign in
-Enter old password
-Enter new password

### Defense 2 installed fail2ban in the victim machine using
-Run sudo apt update
-Run sudo apt install fail2ban -y
-configure fail2ban
-run sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local to get a copy

sudo nano /etc/fail2ban/jail.local

enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600

- restart fail2ban using:      sudo systemctl restart fail2ban
- run the attack script
- check the status of fail2ban using :     sudo fail2ban-client status sshd
- you should see the IP of the attacker in the output
