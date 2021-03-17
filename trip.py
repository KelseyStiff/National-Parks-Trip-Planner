
class Trip:
    def __init__(self, month, park_name, park_city, park_state, park_description, latitude, longitude, 
                 image_1=None, image_2=None, image_3=None, precipitation=None, avg_temp=None, max_temp=None, min_temp=None):
        self.month = month
        self.park_name = park_name
        self.park_city = park_city
        self.park_state = park_state
        self.park_description = park_description
        self.latitude = latitude
        self.longitude = longitude
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3
        self.precipitation = precipitation
        self.avg_temp = avg_temp
        self.max_temp = max_temp
        self.min_temp = min_temp
        


    def __str__(self):
        return f'{self.month}\n{self.park_name}\n{self.park_city}\n{self.park_state}\n{self.park_description}\n\
{self.latitude}\n{self.longitude}\n{self.image_1}\n{self.image_2}\n{self.image_3}\n\
{self.precipitation}%\n{self.avg_temp}\n{self.max_temp}\n{self.min_temp}\n\n'
