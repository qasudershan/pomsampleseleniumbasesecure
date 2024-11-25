import keyring

#In following three lines replace with your desired values and run this file with python
SERVICE_NAME = "prezent_ai"  # Identifier for the service
LOGIN_EMAIL = "test@mail."
LOGIN_PASSWORD = "testpassword"

# Enable following two lines prior executing the file
# keyring.set_password(SERVICE_NAME, "LOGIN_EMAIL", LOGIN_EMAIL)
# keyring.set_password(SERVICE_NAME, "LOGIN_PASSWORD", LOGIN_PASSWORD)

print("Credentials saved successfully!")
