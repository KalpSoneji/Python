class Mail:

    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.pwd = pwd

    def display(self):
        info = {
            "username": self.username,
            "email": self.email,
            "pwd": self.pwd
        }
        print(info)

data = {
    "username": "DavidGaucho",
    "email": "kalpsoneji5@gmail.com",
    "pwd": "haha_gotcha"
}

# Google = Mail(**data)
Google = Mail(data["username"], data["email"], data["pwd"])
Google.display()