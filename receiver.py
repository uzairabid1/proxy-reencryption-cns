from flask import Flask, request, jsonify
import base64
import rsa
from util import load_private_key

app = Flask(__name__)

user2_private_key = load_private_key('user2_private_key')
print(user2_private_key)
@app.route('/receive', methods=['POST'])
def receive_message():
    re_encrypted_message = base64.b64decode(request.json['message'])
    chunks = [re_encrypted_message[i:i+245] for i in range(0, len(re_encrypted_message), 245)]
    decrypted_chunks = [rsa.decrypt(chunk, user2_private_key) for chunk in chunks]
    re_decrypted_message = b''.join(decrypted_chunks)

    print(re_decrypted_message)
    # first_decryption = rsa.decrypt(re_encrypted_message, user2_private_key)   
    # encoded_first_decryption = first_decryption.decode()
    encoded_first_decryption = base64.b64encode(re_decrypted_message).decode('utf-8')

    return jsonify({"message": encoded_first_decryption})

if __name__ == '__main__':
    app.run(port=5003)
