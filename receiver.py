from flask import Flask, request, jsonify
import base64
from util import load_private_key, RSA_decryption

app = Flask(__name__)

user2_private_key = load_private_key('user2_private_key')

@app.route('/receive', methods=['POST'])
def receive_message():
    re_encrypted_message = base64.b64decode(request.json['message'])

    decrypted_message = base64.b64decode(RSA_decryption(re_encrypted_message, user2_private_key))

    re_decrypted_message = RSA_decryption(decrypted_message, user2_private_key)

    print(re_decrypted_message)

    return jsonify({"message": re_decrypted_message})

if __name__ == '__main__':
    app.run(port=5003)
