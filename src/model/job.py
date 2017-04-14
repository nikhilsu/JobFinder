class Job:
    def __init__(self, description, location, web_link):
        self.web_link = web_link
        self.location = location
        self.description = description

    def to_string_array(self):
        return [self.description, self.location, self.web_link]
