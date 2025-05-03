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
Step 1 changed the default password of the victim machine using "passwd"
Step 2 installed fail2ban in the victim machine using: sudo apt update
                                                       sudo apt install fail2ban -y
Step 3 configured the fail2bon config file using:   sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

                                                    sudo nano /etc/fail2ban/jail.local

                                                    enabled = true
                                                    port = ssh
                                                    filter = sshd
                                                    logpath = /var/log/auth.log
                                                    maxretry = 3
                                                    bantime = 3600
                                                    findtime = 600
Step 4 restart fail2ban using:      sudo systemctl restart fail2ban
Step 5 run the attack script
Step 6 check the status of fail2ban using :     sudo fail2ban-client status sshd
you should see the IP of the attacker in the output