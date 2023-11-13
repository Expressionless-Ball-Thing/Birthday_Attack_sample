import hashlib

real = open('real.txt', 'r')
fake = open('fake.txt', 'r')

print(hashlib.sha256(real.read().encode()).hexdigest())
print(hashlib.sha256(fake.read().encode()).hexdigest())

real.close()
fake.close()