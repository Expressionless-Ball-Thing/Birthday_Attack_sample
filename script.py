import hashlib
from typing import List

hashtable = {}

def gen_true_hashtable(textarray: List[str]):
    """Generates variants of the text by adding/removing spaces at the end of lines."""

    num_lines = len(textarray)

    for i in range(2**num_lines):
        binary_representation = format(i, f"0{num_lines}b")
        variant_lines = [
            textarray[j] + " " if binary_representation[j] == "1" else textarray[j]
            for j in range(num_lines)
        ]
        hashtable[hashlib.sha256("\n".join(variant_lines).encode()).hexdigest()] = binary_representation

def compare_hash(truehash: str, fakehash: str):
    temp1 = truehash[::-1]
    temp2 = fakehash[::-1]
    
    for i in range(len(temp1)):
        if (temp1[i] != temp2[i]):
            return i

    return len(temp1)

real = open('real.txt', 'r')
fake = open('fake.txt', 'r')

realarray = real.read().split('\n')
fakearray = fake.read().split('\n')

gen_true_hashtable(realarray)

print("start comparing")

num_lines = len(fakearray)

current_peak = 0

for i in range(2**(num_lines)):
    binary_representation = format(i, f"0{num_lines}b")
    variant_lines = [
        fakearray[j] + " " if binary_representation[j] == "1" else fakearray[j]
        for j in range(num_lines)
    ]
    
    fakehash = hashlib.sha256("\n".join(variant_lines).encode()).hexdigest()
    
    for truehash in hashtable.keys():
        matches = compare_hash(truehash, fakehash)
        if matches > current_peak:
            print(f"Found a new one:\n Fake: {fakehash}\n representation: {binary_representation} \n Real: {truehash}\n representation: {hashtable[truehash]} \n matched {matches} characters")
            current_peak = matches



realarray.copy()

real.close()
fake.close()