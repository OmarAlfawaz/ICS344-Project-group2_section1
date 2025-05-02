# Phase 2 – SIEM Analysis Using Splunk

This phase focuses on the analysis and visualization of attack logs captured during Phase 1. Using Splunk as the SIEM platform, we extracted, indexed, and visualized key data related to the brute-force SSH attack that compromised the victim machine.

---

## 1. Environment Setup

Splunk Enterprise (v9.4.2) was installed on a Kali Linux virtual machine. The installation was done using the `.deb` package from the official Splunk website. After setup, Splunk was accessed through the browser at `http://localhost:8000`.

### Commands used:
```bash
wget -O splunk-9.4.2.deb "https://download.splunk.com/products/splunk/releases/9.4.2/linux/splunk-9.4.2-e9664af3d956-linux-amd64.deb"
sudo dpkg -i splunk-9.4.2.deb
cd /opt/splunk/bin
sudo ./splunk start --accept-license
```

After installation, we set up an admin user and logged into the Splunk dashboard.

---

## 2. Log Ingestion

The log file `logs.txt` (generated during Phase 1 using Metasploit on a Kali machine) was uploaded to Splunk using the “Search & Reporting” app:

- Selected: **Add Data → Upload**
- File: `logs.txt`
- Index: `main`
- Sourcetype: manually set as `Attacker` for consistency

---

## 3. Search & Event Normalization

After confirming the logs were indexed, we observed that initially all logs appeared as a single long event. To fix this, the logs were re-uploaded using line-breaking settings, ensuring each log line was treated as a distinct event.

**Each event now reflected one log entry**, enabling proper field extraction and visualization.

---

## 4. Dashboard Creation

A new Splunk dashboard titled `Phase 2 - SIEM SSH Attack Analysis` was created. The following panels were added, each created through SPL (Search Processing Language) queries:

---

### 📊 Panel 1: Attack Timeline

**Query:**
```spl
index="main" sourcetype="Attacker"
| timechart span=1m count
```

**Purpose:** Shows when the attack took place and activity spikes across time.

📎 Screenshot: `dashboard_screenshots/timeline.png`

---

### 📊 Panel 2: Login Attempt Result

**Query:**
```spl
index="main" sourcetype="Attacker"
| eval result=if(match(_raw, "Success"), "Success", "Failed")
| stats count by result
```

**Purpose:** Separates successful and failed attempts.

📎 Screenshot: `dashboard_screenshots/success_vs_failed.png`

---

### 📊 Panel 3: Top Passwords Attempted

**Query:**
```spl
index="main" sourcetype="Attacker"
| rex "'vagrant:(?<password>[^']+)'"
| stats count by password
```

**Purpose:** Extracts passwords that were attempted during the brute-force.

📎 Screenshot: `dashboard_screenshots/passwords_attempted.png`

---

### 📊 Panel 4: Password Attempts by Result

**Query:**
```spl
index="main" sourcetype="Attacker"
| rex "'vagrant:(?<password>[^']+)'"
| eval result=if(match(_raw, "Success"), "Success", "Failed")
| stats count by password, result
```

**Purpose:** Identifies which passwords failed and which one succeeded.

📎 Screenshot: `dashboard_screenshots/passwords_attempted.png`

---

### 📊 Panel 5: Username Frequency

**Query:**
```spl
index="main" sourcetype="Attacker"
| rex "USERNAME\s*=>\s*(?<username>\w+)"
| stats count by username
```

**Purpose:** Shows usernames that were targeted during the attack.

📎 Screenshot: `dashboard_screenshots/username_frequency.png`

---

### 📊 Panel 6: File Upload Detection

**Query:**
```spl
index="main" sourcetype="Attacker"
| search "upload finished"
```

**Purpose:** Proves that the attacker uploaded a file (`attackedByGroup2.txt`) after gaining access.

📎 Screenshot: `dashboard_screenshots/file_upload.png`

---

## 5. Summary of Findings

| Category               | Observation                                                  |
|------------------------|--------------------------------------------------------------|
| Username targeted      | `vagrant` (only username used during the attack)             |
| Number of passwords    | 20+ tried; only `vagrant:vagrant` was successful             |
| Successful login time  | 2025-04-18 12:54 (visible in logs and timechart)             |
| Method used            | Metasploit SSH brute-force module                            |
| Post-exploitation      | `attackedByGroup2.txt` uploaded to victim's home directory   |

---

## 6. Conclusion

The visual dashboard provided immediate insight into the timeline, nature, and success of the SSH brute-force attack. The ability to extract usernames, passwords, and file operations through search queries allowed us to present clear forensic evidence of the compromise.

This phase fulfills the objectives of SIEM-based analysis using Splunk, in accordance with the course project requirements.

---

## 👤 Contributor for Phase 2

- **Name:** Omar
- **ID:** 202XXXXX
- **Role:** Handled all Phase 2 activities including Splunk installation, log ingestion, dashboard creation, and documentation.
