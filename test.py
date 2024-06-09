import rsa
from util import load_private_key, load_public_key
import base64

message = "Hello World"

def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return private_key, public_key

user2_private_key, user2_public_key = generate_key_pair()

def RSA_encryption(txt):
    result = []
    for n in range(0,len(txt),245):
        part = txt[n:n+245]
        result.append( rsa.encrypt(part.encode("ascii"), user2_public_key) )
    print(len(result),len(result[0]))
    return b''.join(result)

def RSA_decryption(RSA_content):
    result = []
    for n in range(0,len(RSA_content),256):
        part = RSA_content[n:n+256]
        result.append( rsa.decrypt(part, user2_private_key).decode("ascii") )
    return result


encrypted_messasge = RSA_encryption(message)
# print(encrypted_messasge.decode())


pre_re_encrypted_message = base64.b64encode(encrypted_messasge).decode()
print(pre_re_encrypted_message)
re_encrypted_message = RSA_encryption(pre_re_encrypted_message)
# print(re_encrypted_message)

decrypted_message = RSA_decryption(re_encrypted_message)
decrypted_message = decrypted_message[0]+decrypted_message[1]
print(decrypted_message)

re_decrypted_message = RSA_decryption(encrypted_messasge)
print(re_decrypted_message)



