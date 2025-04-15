class Comment:
    def __init__(self, name, date, summary):
        self.name = name
        self.date = date
        self.summary = summary
        self.approved = 0
        self.edited = 0

    def get_author(self):
        return f"{self.name}"

    def get_date(self):
        return f"{self.date.split()[0]}"

    def get_time(self):
        return f"{self.date.split()[-1]}"

    def get_text(self):
        return f"{self.summary}"

    def approve(self):
        self.approved = 1

    def is_approved(self):
        return self.approved == 1

    def set_text(self, text):
        self.summary = text
        self.edited = 1
        self.approved = 0

    def is_edited(self):
        return self.edited == 1

    def __repr__(self):
        return f"{self.summary}\n[{self.name} ({self.date})]\n"
