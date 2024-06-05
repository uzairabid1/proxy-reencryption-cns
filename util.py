import boto3
import os
import rsa
from dotenv import load_dotenv

load_dotenv()

secrets_manager_access_key = os.getenv('secrets_manager_access_key')
secrets_manager_secret_key = os.getenv('secrets_manager_secret_key')

secrets_client = boto3.client('secretsmanager', aws_access_key_id=secrets_manager_access_key, aws_secret_access_key=secrets_manager_secret_key, region_name='us-east-2')

def load_private_key(secret_name):
    response = secrets_client.get_secret_value(SecretId=secret_name)
    key = response['SecretString']
    private_key = rsa.PrivateKey.load_pkcs1(key.encode('utf-8'))
    return private_key

def load_public_key(secret_name):
    response = secrets_client.get_secret_value(SecretId=secret_name)
    key = response['SecretString']
    public_key = rsa.PublicKey.load_pkcs1(key.encode('utf-8'))
    return public_key
