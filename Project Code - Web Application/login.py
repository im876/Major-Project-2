import streamlit as st
import streamlit_authenticator as stauth
import time


names = ['Admin', 'Ishan']
usernames = ['admin', 'ishan']
passwords = ['123', 'modi']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    
    st.write('Welcome *%s*' % (name))
    import subprocess

    subprocess.call("C:/Users/admin/app/app.py", shell=True)
    authenticator.logout('Logout', 'main')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')