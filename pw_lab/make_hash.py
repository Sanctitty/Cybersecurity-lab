import hashlib, getpass
pw = getpass.getpass("Enter password to hash (lab use only): ")
h = hashlib.sha256(pw.encode()).hexdigest()
with open("hashes.txt","w") as f:
    f.write(f"labuser:{h}\n")
print("Saved hashes.txt with SHA256 hash.")
