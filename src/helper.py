#This is the file for any helper functions that could be used throughout the code
import hashlib

#hash password 
def hash_pass(hashing):
    hash_value = hashlib.sha256(hashing.encode('utf-8')).hexdigest()
    return hash_value


