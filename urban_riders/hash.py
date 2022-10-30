import hashlib

email = 'email@example.com'
password = 'my_password'

pwd_encode = password.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

print(pwd_encode)
print(pwd_hash)