import boto3
import os
import rsa
from dotenv import load_dotenv

load_dotenv()

secrets_manager_access_key = os.getenv('secrets_manager_access_key')
secrets_manager_secret_key = os.getenv('secrets_manager_secret_key')

secrets_client = boto3.client('secretsmanager', aws_access_key_id=secrets_manager_access_key, aws_secret_access_key=secrets_manager_secret_key, region_name='us-east-2')

def generate_key_pair():
    public_key, private_key = rsa.newkeys(2048)
    return private_key, public_key

def save_key_to_secrets_manager(secret_name, key):
    key_bytes = key.save_pkcs1()
    key_str = key_bytes.decode('utf-8')
    response = secrets_client.create_secret(Name=secret_name, SecretString=key_str)
    return response

user1_private_key, user1_public_key = generate_key_pair()
user2_private_key, user2_public_key = generate_key_pair()
proxy_private_key, proxy_public_key = generate_key_pair()

save_key_to_secrets_manager('user1_private_key', user1_private_key)
save_key_to_secrets_manager('user1_public_key', user1_public_key)

save_key_to_secrets_manager('user2_private_key', user2_private_key)
save_key_to_secrets_manager('user2_public_key', user2_public_key)

save_key_to_secrets_manager('proxy_private_key', proxy_private_key)
save_key_to_secrets_manager('proxy_public_key', proxy_public_key)
