class JobQueryParameters:
    def __init__(self, job_category, country, state, city):
        self.city = city
        self.state = state
        self.country = country
        self.job_category = job_category
