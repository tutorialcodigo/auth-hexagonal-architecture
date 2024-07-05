import boto3 as boto
from botocore.config import Config 
from botocore.exceptions import ClientError

class CloudServices:
    def __init__(self, client):
        self.client = client 

    def conn(self):
        try:
            config  = Config(connect_timeout=5, read_timeout=5, retries = {"max_attempts": 1})
            conn = boto.client(self.client, region_name='us-east-1', config=config)
        except Exception as e:
            raise ClientError(f"Error connecting the service: {str(e)}")
        else:
            return conn
        


        