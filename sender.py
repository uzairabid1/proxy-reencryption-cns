from flask import Flask, request
import base64
import requests
from util import load_public_key, RSA_encryption

app = Flask(__name__)

user2_public_key = load_public_key('user2_public_key')

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json['message']

    encrypted_message = RSA_encryption(message, user2_public_key)
    encoded_message = base64.b64encode(encrypted_message).decode()

    proxy_response = requests.post('http://localhost:5002/proxy', json={"message": encoded_message})

    return proxy_response.json()

if __name__ == '__main__':
    app.run(port=5001)
