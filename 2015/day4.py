import hashlib

# Calculate the hash of the secret key
secret_key = 'iwrupvqb'

# Generate a sequence of numbers
for i in range(100000, 10000000):

    # Add decimal to the key
    updated_key = secret_key + str(i)
    
    # Check MD5 hash of each combination
    md5_hash = hashlib.md5(updated_key.encode()).hexdigest()

    # Part 1
    # Check if the MD5 hash starts with 00000
    if md5_hash.startswith('00000'):
        print("MD5 hash of {} is {}".format(updated_key, md5_hash))

    # Part 2
    # Check if the MD5 hash starts with 00000
    if md5_hash.startswith('000000'):
        print("MD5 hash of {} is {}".format(updated_key, md5_hash))


