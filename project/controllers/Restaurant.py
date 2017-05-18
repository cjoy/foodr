class Restaurant:
    def __init__(self, name, lng, lat, dietary, deals, alcohol, wheelchair, wifi):
        self.name = name
        self.dietary = dietary
        self.deals = deals
        # long and lat date for seach and images
        self.lng = lng
        self.lat = lat

        if alcohol == "true":
            self.alcohol = True
        else:
            self.alcohol = False
        if wheelchair == "true":
            self.wheelchair = True
        else:
            self.wheelchair = False
        if wifi == "true":
            self.wifi = True
        else:
            self.wifi = False


    def get_field(self, field):
        if field == "name":
            return self.name
        if field == "dietary":
            return self.dietary
        if field == "deals":
            return self.deals
        if field == "lng":
            return self.lng
        if field == "lat":
            return self.lat
        if field == "alcohol":
            return self.alcohol
        if field == "wheelchair":
            return self.wheelchair
        if field == "wifi":
            return self.wifi

    def to_string(self):
        return "name: %s, dietary: %s, deals: %s, alcohol: %s, wheel: %s, wifi: %s" % (self.name, self.dietary, self.deals, self.alcohol, self.wheelchair, self.wifi)