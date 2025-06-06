class Mail:

    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def display(self):
        print(f"Username: {self.username}\nEmail: {self.email}\nPassword: {self.pwd}")

Google = Mail("DavidGaucho", "kalpsoneji5@gmail.com", "haha_gotcha")
Google.display()