import sys

hash = sys.argv[1]
decrypted_hash = ""
for i in range(0, len(hash)):
    decrypted_hash = decrypted_hash + chr(ord(hash[i]) - i)
print(decrypted_hash)
