# Copyright (c) 2020 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample Code License, Version 1.1 (the "License"). You may obtain a copy of the License at
#
#            https://developer.cisco.com/docs/licenses
# All use of the material herein must be in accordance with the terms of the License. All rights not expressly granted by the License are reserved. Unless required by applicable law or agreed to separately in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


from ciscoaxl import axl
import requests
import base64
from requests.auth import HTTPBasicAuth
from credentials import *

# Base 64 conversion of axl_username and password
userpass = axl_username + ':' + password
encoded_u = base64.b64encode(userpass. encode()).decode()
#print(encoded_u)


# Get information from CUCM User
def get_user_info(_axl_username, _password, _cucm, _version, _username):
    ucm = axl(username=_axl_username, password=_password, cucm=_cucm, cucm_version=_version)
    user = ucm.get_user(_username)
    #print(user)
    # print(user['associatedDevices']['device'][0])
    device_user = str(user['associatedDevices']['device'][0])
    # print(user['primaryExtension']['pattern'])
    pattern_user = str(user['primaryExtension']['pattern'])
    return device_user, pattern_user

# user_info = get_user_info('axlapiuser', 'cciecollab', '192.168.2.50', '12.5','macquate')
# device_user, pattern_user = user_info
# print(device_user)
# print(pattern_user)

# Set username's phone text line
def phone_text_line_setter(_device, _pattern, _text):
    url = "https://192.168.2.50:8443/axl/"
    payload = f'''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/12.5">
   <soapenv:Header/>
   <soapenv:Body>
      <ns:updatePhone sequence="?">
          <name>{_device}</name>
               <lines>
                  <line>
                     <index>1</index>
                     <label>{_text}</label>
                     <dirn>
                        <pattern>{_pattern}</pattern>
                        <routePartitionName/>
                     </dirn>
                  </line>
               </lines>
      </ns:updatePhone>
   </soapenv:Body>
</soapenv:Envelope>

'''
    headers = {
    'Authorization': f'Basic {encoded_u}',
    'Content-Type': 'text/plain'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    # print(response.text)
    return response


# phone_text_line_setter('SEP58BC2775EE8F', 1001, "Hello There")