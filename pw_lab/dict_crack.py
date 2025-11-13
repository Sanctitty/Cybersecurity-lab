import hashlib
target = open("hashes.txt").read().strip().split(":",1)[1]
with open("wordlist.txt") as w:
    for line in w:
        pw = line.strip()
        if not pw: continue
        if hashlib.sha256(pw.encode()).hexdigest() == target:
            print("FOUND:", pw)
            break
    else:
        print("Not found in wordlist.")
