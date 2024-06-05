from flask import Flask, request, jsonify
import base64
import rsa
from util import load_public_key

app = Flask(__name__)


user2_public_key = load_public_key('user2_public_key')

@app.route('/proxy', methods=['POST'])
def proxy_message():
    encoded_message = request.json['message']
    encrypted_message = base64.b64decode(encoded_message)
    chunks = [encrypted_message[i:i+245] for i in range(0, len(encrypted_message), 245)]

    re_encrypted_chunks = [rsa.encrypt(chunk, user2_public_key) for chunk in chunks]

    re_encrypted_message = b''.join(re_encrypted_chunks)

    encoded_re_encrypted_message = base64.b64encode(re_encrypted_message).decode('utf-8')

    return jsonify({"message": encoded_re_encrypted_message})

if __name__ == '__main__':
    app.run(port=5002)
