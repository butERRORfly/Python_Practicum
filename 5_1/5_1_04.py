class Programmer:
    def __init__(self, name, job_title):
        jobs_titles = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20,
        }
        self.name = name
        self.job_now = jobs_titles[job_title]
        self.total_time = 0
        self.salary = 0

    def work(self, time):
        self.total_time += time
        self.salary += self.job_now * time

    def info(self):
        return f'{self.name} {self.total_time}ч. {self.salary}тгр.'

    def rise(self):
        if self.job_now < 20:
            self.job_now += 5
        else:
            self.job_now += 1

