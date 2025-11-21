import hashlib, getpass

pin = getpass.getpass("Enter PIN to hash: ")
hash_val = hashlib.sha256(pin.encode()).hexdigest()

with open("hashes.txt", "w") as f:
    f.write(f"labuser:{hash_val}\n")

print("Saved hashes.txt")
