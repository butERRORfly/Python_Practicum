class Comment:
    def __init__(self, name, date, summary):
        self.name = name
        self.date = date
        self.summary = summary

    def get_author(self):
        return f"{self.name}"

    def get_date(self):
        return f"{self.date.split()[0]}"

    def get_time(self):
        return f"{self.date.split()[-1]}"

    def get_text(self):
        return f"{self.summary}"

    def __repr__(self):
        return f"{self.name} {self.date} {self.summary}"
