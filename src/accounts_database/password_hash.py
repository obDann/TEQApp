from passlib.hash import pbkdf2_sha256

def hash_password(password):
    '''
    (string) -> string

    Returns a hashed password using sha256. Given package creates a random
    salt for the password and creates a hash.
    '''
    hash = pbkdf2_sha256.hash(password)
    return hash

def verify_password(password, hash):
    '''
    (string) -> Bool

    Returns True if the given password is verified to compute the same hash as
    stored in the database.
    '''
    verification = pbkdf2_sha256.verify(password, hash)
    return verification
