from flask import Flask, request, jsonify
import base64
import rsa
from util import load_public_key

app = Flask(__name__)

user2_public_key = load_public_key('user2_public_key')

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json['message'].encode('utf-8')
    encrypted_message = rsa.encrypt(message, user2_public_key)
   
    return {"message": base64.b64encode(encrypted_message).decode()}

if __name__ == '__main__':
    app.run(port=5001)
