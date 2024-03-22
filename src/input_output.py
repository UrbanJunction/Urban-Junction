#libraries 
import requests 
import logging 
import json 
import boto3 
from botocore.exceptions import ClientError

class input_output():
    """
    Implementation for retrieval of data from source and 
    load data into cloud storage. 
    """

    def __init__(self):
        """
        Generator function
        """
        #retrieve name of secret and aws region
        with open('terraform/terraform.tfstate','r') as f:
            outputs = json.load(f)['outputs']
        secret_name = outputs['secret_name_511ny']['value']
        region_name = outputs['region']['value']

        #create secret manager client 
        session = boto3.session.Session()
        client = session.client(service_name='secretsmanager',region_name=region_name)

        #attempt to retrieve secret value 
        try:
            self.api_key = client.get_secret_value(SecretId=secret_name)['SecretString']
        except ClientError as e:
            raise e
        

    def get(self,url):
        """
        Request data from source using defined API endpoint, API dev key, and format 

        Args:
            url (string): API endpoint

        Returns:
            list: list of data 
        """
        try:
            #request event information 
            r = requests.get(url)
            #retrieve data and map to dictionary
            data = json.loads(r.text)
        except Exception as e:
            logging.error(e)
        return data

    def GETEVENTS(self,format='json'):
        """
        Retrieve Events data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of events data
        """
        return self.get(f'https://511ny.org/api/getevents?key={self.api_key}&format={format}')
    
    def GETROADWAYS(self,format='json'):
        """
        Retrieve roadways data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of roadways data
        """
        return self.get(f'https://511ny.org/api/getroadways?key={self.api_key}&format={format}')
    
    def GETCAMERAS(self,format='json'):
        """
        Retrieve camera data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of camera data
        """
        return self.get(f'https://511ny.org/api/getcameras?key={self.api_key}&format={format}')
    
    def GETMESSAGESIGNS(self,format='json'):
        """
        Retrieve message sign data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of message sign data
        """
        return self.get(f'https://511ny.org/api/getmessagesigns?key={self.api_key}&format={format}')
    
    def GETALERTS(self,format='json'):
        """
        Retrieve alerts sign data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of alerts data
        """
        return self.get(f'https://511ny.org/api/getalerts?key={self.api_key}&format={format}')
    

    def GETWINTERROADCONDITIONS(self,format='json'):
        """
        Retrieve winter road conditions sign data from source

        Args:
            format (str): str or xml 

        Returns:
            list: list of winter road conditions data
        """
        return self.get(f'https://511ny.org/api/getwinterroadconditions?key={self.api_key}&format={format}')

if __name__ == '__main__':
    test = input_output()
    data = test.GETEVENTS()
    print(data)
    pass