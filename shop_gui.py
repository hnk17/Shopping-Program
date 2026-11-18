from tkinter import *  # import tkinter
from shop_class import App, Cart  # import App and Cart class from CLASS file
from functools import partial
import random, string  # used in random receipt no function


class MyFrame(Frame):
    def __init__(self, root):
        """Constructor method"""
        Frame.__init__(self, root)  # Frame class initialization
        self.init_container()  # initialize all widget containers
        self.cart = Cart()  # initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.welcome()  # start the application
        self.data = StringVar(self, 'Subtotal: 0.0')  # Associated with subtotal label 

    def init_container(self):
        """Initialize widget containers"""
        self.states = []  # holds state if selected/not i-th list item holds selection for i-th item

    def clear_frame(self):
        """Clears the previous frame"""
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        """Exits the program"""
        root.destroy()

    def welcome(self):
        """Welcome window - refer spec file for details"""
        self.clear_frame()
        Label(self, text='****Welcome to AppsCart!****', background="gray70").grid(row=0, column=0)
        # Select by category: Button – command = shop_by_apps_category
        select_by_category_btn = Button(self, text='Select by Category', command=self.shop_by_apps_category)
        select_by_category_btn.grid(row=1, column=0)

        # Select by rating: Button - command = shop_by_apps_ratings
        select_by_rating_btn = Button(self, text='Select by Ratings', command=self.shop_by_ratings)
        select_by_rating_btn.grid(row=2, column=0)

        # Select by Price: Button - command = shop_by_apps_price
        select_by_apps_price_btn = Button(self, text='Select by Price', command=self.shop_by_apps_price)
        select_by_apps_price_btn.grid(row=3, column=0)

        # Exit Application: Button – exit the program, command = exit_application
        exit_application_btn = Button(self, text='Exit Application', command=self.exit_application)
        exit_application_btn.grid(row=4, column=0)

    def shop_by_apps_category(self):
        """2. Widget to display different category of apps - refer spec file for details"""
        self.clear_frame()
        self.init_container()
        Label(self, text='Choose Apps Category').grid(row=0)

        # widget creation for key list of category_dict
        row = 1
        for category in App.category_dict.keys():
            b = Button(self, text=category, command=partial(self.start, App.category_dict[category]))
            b.grid(row=row)
            row += 1

        # Go Back: Button – command = welcome
        go_back_btn = Button(self, text='Go Back', command=self.welcome)
        go_back_btn.grid(row=row)

    # define def shop_by_apps_ratings(self)
    def shop_by_ratings(self):
        self.clear_frame()
        self.init_container()
        Label(self, text='Choose Apps Ratings').grid(row=0)

        # widget creation for key list of rating_dict
        row = 1
        for rating in App.rating_dict.keys():
            b = Button(self, text=rating * '*' + ' & up', command=partial(self.start, App.rating_dict[rating]))
            b.grid(row=row)
            row += 1

        # Go Back: Button – command = welcome
        go_back_btn = Button(self, text='Go Back', command=self.welcome)
        go_back_btn.grid(row=row)

    # define shop_by_apps_price(self)
    def shop_by_apps_price(self):
        self.clear_frame()
        self.init_container()
        Label(self, text='Choose Apps Pricing').grid(row=0)

        # widget creation for key list of price_dict
        row = 1
        for price in App.price_dict.keys():
            if price == 0:
                b = Button(self, text='$0.00 - $1.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            elif price == 1:
                b = Button(self, text='$1.00 - $2.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            elif price == 2:
                b = Button(self, text='$2.00 - $3.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            elif price == 3:
                b = Button(self, text='$3.00 - $4.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            elif price == 4:
                b = Button(self, text='$4.00 - $5.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            elif price == 5:
                b = Button(self, text='$5.00 - $6.00', command=partial(self.start, App.price_dict[price]))
                b.grid(row=row)
            row += 1

        # Go Back: Button – command = welcome
        go_back_btn = Button(self, text='Go Back', command=self.welcome)
        go_back_btn.grid(row=row)

    def start(self, current_items):
        """'3. Start ordering from selected category,
        list passed by command will be used as current_items"""
        self.clear_frame()
        self.init_container()

        # creating widgets for items using a for loop
        # iterative over each item of current apps and
        # create that many checkbutton, price, ID, rating and category label
        row = 0
        for item in current_items:
            self.states.append(IntVar())  # keeps track if an item is selected
            checkbutton = Checkbutton(self, text=item.get_name(), variable=self.states[row])  # create check buttons
            checkbutton.grid(row=row, column=0)

            # create and layout a price label, set text to item.get_price()
            if item.get_price() == 0.0:
                price_label = Label(self, text='Free')
                price_label.grid(row=row, column=1)
            else:
                price_label = Label(self, text='$' + str(item.get_price()))
                price_label.grid(row=row, column=1)

            # create and layout id label and set text to item.get_id() method
            id_label = Label(self, text=str(item.get_ID()))
            id_label.grid(row=row, column=2)

            # create and layout developer label
            developer_label = Label(self, text=str(item.get_developer()))
            developer_label.grid(row=row, column=3)

            # create and layout rating
            rating_label = Label(self, text=str(item.get_rating()))
            rating_label.grid(row=row, column=4)

            # create and layout category label
            category_label = Label(self, text=str(item.get_category()))
            category_label.grid(row=row, column=5)
            row += 1

        # create and layout subtotal label, set textvariable = self.data so it changes
        subtotal_label = Label(self, text='Subtotal', textvariable=self.data)
        subtotal_label.grid(row=row, column=0)

        # create and layout main Menu button, command = welcome
        main_menu_btn = Button(self, text='Main Menu', command=self.welcome)
        main_menu_btn.grid(row=row, column=1)

        # create and layout add_to_cart_button, command = partial(self.add_to_cart, current_items)
        add_to_cart_btn = Button(self, text='Add to Cart', command=partial(self.add_to_cart, current_items))
        add_to_cart_btn.grid(row=row, column=2)

        # create and layout button: checkout, command = self.checkout
        checkout_btn = Button(self, text='Checkout', command=self.checkout)
        checkout_btn.grid(row=row, column=3)

    def add_to_cart(self, current_items):
        """3. Added to cart, displays subtotal - see spec file for details layout"""
        # get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
        # if item is selected: add app item object to self.cart list

        for i in current_items:
            current_index = current_items.index(i)
            if self.states[current_index].get() == 1:
                # self.tempCart.append(i)
                self.cart.append(i)

        # set the StringVar to be the current subtotal
        self.data.set('Subtotal: ' + str('{:.2f}'.format(self.cart.subtotal())))

    def get_receipt_number(self):
        """Generate random receipt number"""
        return ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=10))

    def checkout(self):
        """4. Check out window """
        self.clear_frame()

        # Your e-order: Label
        Label(self, text='Your e-order').grid(row=0, column=2)

        # e-Order Number: Label - Randomly generated by program - text = get_receipt_number()
        e_order_number = Label(self, text='e-Order Number: ' + self.get_receipt_number() + '\n**********')
        e_order_number.grid(row=1, column=2)

        # Name Price Rating Category: Header Label
        name_header_label = Label(self, text='name')
        name_header_label.grid(row=2, column=0)

        price_header_label = Label(self, text='price')
        price_header_label.grid(row=2, column=1)

        rating_header_label = Label(self, text='rating')
        rating_header_label.grid(row=2, column=2)

        genre_header_label = Label(self, text='genre')
        genre_header_label.grid(row=2, column=3)

        # Iterate over apps items from cart list and create labels of name, price, rating, category and layout
        row = 3
        for app in self.cart:
            name_label = Label(self, text=app.get_name())
            name_label.grid(row=row, column=0)

            price_label = Label(self, text='$' + str(app.get_price()))
            price_label.grid(row=row, column=1)

            rating_label = Label(self, text=app.get_rating())
            rating_label.grid(row=row, column=2)

            genre_label = Label(self, text=app.get_category())
            genre_label.grid(row=row, column=3)
            row += 1

        # Subtotal: Label - get self.cart subtotal - new label
        subtotal_label = Label(self, text='Subtotal:$ ' + str(self.cart.subtotal()))
        subtotal_label.grid(column=2)

        # Tax: Label - 4.3%
        tax_label = Label(self, text='Tax: 4.3%')
        tax_label.grid(column=2)

        # Total: Label - subtotal + tax
        total_calculation = self.cart.subtotal() + self.cart.subtotal() * 0.043
        total_label = Label(self, text='Total: ' + str('{:.2f}'.format(total_calculation)))
        total_label.grid(column=2)

        # ‘Thank you’ message: Label
        thank_you_label = Label(self, text='Thanks for using Apps Cart!\n**********')
        thank_you_label.grid(column=2)

        # Exit application: Button – exit the program - command = exit_application
        exit_app_btn = Button(self, text='Exit Application', command=self.exit_application)
        exit_app_btn.grid(column=2)


root = Tk()                 # main driver code
root.title('Apps Cart')     # create root window and set window title
root.geometry('700x500')    # window sizing
frame = MyFrame(root)       # create a myframe object and layout
frame.grid()
root.mainloop()             # call mainloop
