# Copyright (c) 2020 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample Code License, Version 1.1 (the "License"). You may obtain a copy of the License at
#
#            https://developer.cisco.com/docs/licenses
# All use of the material herein must be in accordance with the terms of the License. All rights not expressly granted by the License are reserved. Unless required by applicable law or agreed to separately in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.


from flask import Flask, render_template, request, session, redirect, url_for
from functions import get_user_info, phone_text_line_setter
from credentials import *


app_text = Flask(__name__)
app_text.config['SECRET_KEY'] = 'secret_key'


# User Login route, It validates the user in CUCM and gets Device and Line
@app_text.route('/', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username_login = request.form.get('username')
        user_info = get_user_info(_axl_username=axl_username, _password=password, _cucm=cucm, _version=version, _username=username_login)
        device, pattern = user_info
        print(username_login)
        print(device)
        print(pattern)
        session['device']= device
        session['pattern'] = pattern
        session['username_login'] = username_login
        return redirect(url_for('text_change'))
    return render_template('login.html')


# Route to set the Text for the line of the phone, I'm not passing any info via browser url (hence the session)
@app_text.route('/text_change', methods=['GET', 'POST'])
def text_change():
    username_text = session.get('username_login')
    device = session.get('device')
    pattern = session.get('pattern')
    if request.method == 'POST':
        text = request.form.get('text_phone')
        # print(text)
        phone_text = phone_text_line_setter(_device=device, _pattern=pattern, _text=text)
        # print(phone_text)
        return render_template('change_successful.html', pattern=pattern, device=device, text=text)
    return render_template('text_change.html', username=username_text, device=device, pattern=pattern)


@app_text.route('/change_successful', methods=['GET', 'POST'])
def change_successful():
    render_template('change_successful.html')


if __name__ == '__main__':
    app_text.run()
