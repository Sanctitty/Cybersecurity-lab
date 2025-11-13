# Termux Password Cracking Lab — README

**Purpose**
A short, safe, hands‑on lab for beginners to learn basic password cracking concepts on **Termux (Android)** using local files and simple Python scripts. For learning only — do **not** target real systems.

---

## What’s included
- `make_hash.py` — create a SHA‑256 test hash from a password you enter
- `wordlist.txt` — small example wordlist for dictionary attacks
- `dict_crack.py` — dictionary attack script (checks wordlist against the hash)
- `pin_bruteforce.py` — brute‑force script (tries 0000–9999)
- `README.md` — this file
- `commands.txt` — (optional) saved command history / notes

---

## Quick setup (Termux)
1. Update & install required packages:
```bash
pkg update -y
pkg upgrade -y
pkg install -y python git openssh curl
```

2. Create lab folder and files (if not already present):
```bash
mkdir -p ~/pw_lab
cd ~/pw_lab
# copy or create the provided files here
```

---

## How to run the lab (steps)
1. Create the test hash:
```bash
python make_hash.py
# enter a password when prompted (lab-only)
cat hashes.txt  # shows labuser:<hex-hash>
```

2. Dictionary attack:
```bash
python dict_crack.py
# prints "FOUND: <password>" if matched
```

3. Brute-force 4-digit PIN:
```bash
python pin_bruteforce.py
# prints "FOUND PIN: 1234" if matched
```

---

## Push to GitHub (short)
1. Create a repo on GitHub (e.g., `termux-pw-lab`).
2. Push from Termux:
```bash
git init
git add .
git commit -m "Termux password cracking lab"
git remote add origin https://github.com/USERNAME/termux-pw-lab.git
git branch -M main
git push -u origin main  # use PAT as password or set up SSH
```

---

## Safety & notes
- Only use on devices/accounts you own.
- This lab uses unsalted SHA‑256 for teaching; real systems use salts and stronger hashing (bcrypt, sha512crypt).
- Strong defense: long unique passphrases, salts, rate limiting, and MFA.

---

## Author
Created for teaching by Nwachukwu samuel


