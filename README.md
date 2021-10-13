# GVE_DevNet_CUCM_Phone_Name_Change_User_Portal
User portal that helps CUCM users pull their Cisco Device information and change their line's text description.


## Contacts
* Max Acquatella

## Solution Components
* cucm
* axl
* python
* flask

## Installation/Configuration

Before installing: Please make sure that you have created an AXL Application user in CUCM. 
If you don't know how to create an AXL Application user, please see the following:

https://www.youtube.com/watch?v=wtnDzPQVdRE&t=248s

Once you have created an AXL Application user, create a virtual environment, and install requirements.txt

Creating Python Virtual Environments:

https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2018/pdf/DEVNET-3602.pdf (Slide 36)

Install requirements.txt

https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2018/pdf/DEVNET-3602.pdf (Slide 32)

For more basic Python you can see this Cisco Live Devnet presentation (requires login):

https://www.ciscolive.com/global/on-demand-library.html?search=3602&search=3602#/video/1533847968086001MNxd

After creating your vitual environment, modify the credentials in the credentials.py script: 

```python

cucm = 'xxx.xxx.xxx.xxx' # IP Address of your CUCM
axl_username = 'exampleusername' # AXL API Username - Set in CUCM Applications users
password = 'examplepassword' # add the AXL username password
version = '12.5' # Current version of CUCM - input as shown

```
## Usage

Once the installation is complete, use a command line to launch the app_text script:


    $ python3 app_text.py

Launch the main (or home, or / ) screen, input the username of a CUCM registered user. The username is the user ID of a registered CUCM User as shown in he following image:

Registered User in CUCM:

![/IMAGES/register_user.png](/IMAGES/register_user.png)

(This is only relevant to the CUCM administrator, the user won't see the previous screen anywhere in this code - shown only as a reference).

The following list the 3 steps that the users have to fllowin in order to change their line text: 

Step 1:

Input username in the following screen:

![/IMAGES/Step_1.png](/IMAGES/Step_1.png)

Once the user logs in, the next screen should show the username and registered device (in this case SEP + Mac address):

Step 2:

![/IMAGES/Step_2.png](/IMAGES/Step_2.png)

With this validation, proceed to add the desired text in the provided text box and click Change Text.

Step 3:

The next screen will confirm that the change has been processed by the CUCM:

![/IMAGES/Step_3.png](/IMAGES/Step_3.png)

# Screenshots

![/IMAGES/workflow.png](/IMAGES/workflow.png)

NOTES:

 *** THIS CODE DOES NOT PROVIDE ANY ERROR OR EXCEPTIONS HANDLING ***

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
