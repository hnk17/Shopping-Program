# -------------------------------------------------------------------------------
# Final Project
# Name: Kylie Hoang
# source code below
# -------------------------------------------------------------------------------
import csv

# class Cart - subclass of list class; returns subtotal from a Cart list object
class Cart(list):
    # define a subtotal function
    def subtotal(self):
        total = 0
        for app in self:
            total += float(app.get_price())
        return total


class App(object):
    """"App class defines an app item available in store. App object saved in category_dict per category
        and rating_dict per rating and price_dict per price """""
    category_dict = {}
    rating_dict = {}
    price_dict = {}
    temp_list = []

    def __init__(self, ID, name, developer, description, price, rating, review_count, category):
        """"Initialization method"""""
        # initialize name, developer, description, price, rating,
        # review_count, category as private attribute
        # populate dict by category - key = category and values = list of app objects
        self.__id = ID
        self.name = name
        self.developer = developer
        self.description = description
        self.price = price
        self.rating = rating
        self.__review_count = review_count
        self.__category = category
        App.temp_list.append(self)

        if self.__category in App.category_dict.keys():
            App.category_dict[self.__category].append(self)  # append object to current category
        else:
            App.category_dict[self.__category] = [self]

        # rating_dict creation
        for n in range(1, 6):
            App.rating_dict[n] = []

        for a in App.temp_list:
            if float(a.rating) >= 5.0:
                App.rating_dict[5].append(a)
            elif float(a.rating) >= 4.0:
                App.rating_dict[4].append(a)
            elif float(a.rating) >= 3.0:
                App.rating_dict[3].append(a)
            elif float(a.rating) >= 2.0:
                App.rating_dict[2].append(a)
            else:
                App.rating_dict[1].append(a)

        # price_dict creation
        for p in range(0, 6):
            App.price_dict[float(p)] = []

        for a in App.temp_list:
            if a.price == 'Free':
                App.price_dict[0].append(a)
            elif float(a.price) < 1:
                App.price_dict[0].append(a)
            elif 1 <= float(a.price) < 2:
                App.price_dict[1].append(a)
            elif 2 <= float(a.price) < 3:
                App.price_dict[2].append(a)
            elif 3 <= float(a.price) < 4:
                App.price_dict[3].append(a)
            elif 4 <= float(a.price) < 5:
                App.price_dict[4].append(a)
            elif float(a.price) >= 5:
                App.price_dict[5].append(a)

    # define get methods
    def get_ID(self):
        return self.__id

    def get_name(self):
        return self.name

    def get_developer(self):
        return self.developer

    def get_description(self):
        return self.description

    def get_price(self):
        if self.price == 'Free':
            return 0.0
        else:
            return self.price

    def get_rating(self):
        return self.rating

    def get_review_count(self):
        return self.__review_count

    def get_category(self):
        return self.__category

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} ".format(self.get_ID(), self.get_name(), self.get_developer(),
                                                               self.get_description(), self.get_price(),
                                                               self.get_rating(), self.get_review_count(),
                                                               self.get_category())



# process csv file and app creation
filename = 'Top50ShopifyApps.csv'
with open(filename) as fin:
    apps = csv.reader(fin, delimiter='\t')
    next(apps)
    for row in apps:
        ID, name, developer, description, price, rating, review_count, category = row
        App(ID, name, developer, description, price, rating, review_count, category)


'''Testing code to check object creating Items
Uncomment to test and then
Comment out when done'''
'''''
for k, v in App.category_dict.items():  # v is a list of all objects
    print(k, [(obj.get_name(), obj.get_rating()) for obj in v])
print('++++++++++')

for k, v in App.rating_dict.items():  # v is a list of all objects
    print(k, [obj.get_rating() for obj in v])
print('++++++++++')

for k, v in App.price_dict.items():  # v is a list of all objects
    print(k, [obj.get_price() for obj in v])
print('++++++++++')
'''''
