import os

#to install the cloudmersive api before running code
os.system("cmd /c pip install cloudmersive-image-api-client")

import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException

#website referenced to help get started with Cloudmersive API: https://api.cloudmersive.com/python-client.asp
#used code for image recognition to set up API

api_instance = cloudmersive_image_api_client.FaceApi()
image_file = 'C:\\temp\\input.jpg' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = 'c6d225df-5c14-4a67-b606-a228f3a4c55d'

try:
    # Crop image to face (square)
    api_response = api_instance.face_crop_first(image_file)
    print(api_response)
except ApiException as e:
    print("Exception when calling FaceApi->face_crop_first: %s\n" % e)