from flask import Flask, request
import base64
import requests
from util import load_public_key, RSA_encryption

app = Flask(__name__)

user2_public_key = load_public_key('user2_public_key')

@app.route('/proxy', methods=['POST'])
def proxy_message():
    encrypted_message = request.json['message']

    re_encrypted_message = RSA_encryption(encrypted_message, user2_public_key)
    re_encoded_message = base64.b64encode(re_encrypted_message).decode()

    receiver_response = requests.post('http://localhost:5003/receive', json={"message": re_encoded_message})

    return receiver_response.json()

if __name__ == '__main__':
    app.run(port=5002)
