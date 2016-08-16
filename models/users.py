import datetime

class users:
    def __init__(self, user_name, email_address, password):

        self.user_id = ""
        self.user_name = user_name
        self.email_address = email_address
        self.password = password
        self.last_logged_in = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.is_pass_sequential = True
        self.violation_count = 0
        self.profile_pic_url = ""



