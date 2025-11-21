import hashlib
target = open("hashes.txt").read().strip().split(":",1)[1]
for i in range(0,10000):           # 0000 → 9999
    pin = f"{i:04d}"
    if hashlib.sha256(pin.encode()).hexdigest() == target:
        print("FOUND PIN:", pin)
        break
else:
    print("PIN not found in 0000-9999")
