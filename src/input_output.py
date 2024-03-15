#libraries 
import requests 
import logging 
import json 
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

class input_output():
    """
    Implementation for retrieval of data from source and 
    load data into cloud storage. 
    """

    def __init__(self):
        """
        Generator function
        """
        with open('terraform/terraform.tfstate','r') as f:
            outputs = json.load(f)['outputs']
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=outputs['vault_uri']['value'],credential=credential)
        self.api_key = client.get_secret(outputs['secret_511ny_name']['value']).value

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