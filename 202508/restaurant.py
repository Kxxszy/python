class RESTAURANT:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.restaurant_list = []

    def adv(self):
        print(f'Welcome to {self.name}!')

    def show_dish_list(self):
        if self.restaurant_list:
            print(f'this is the list:{self.restaurant_list}')
        else :
            print('this is the empty list')

    def add_dish(self,*dish):
        self.restaurant_list.append(dish)
        print(f'Added {dish} to the dish list.')

    def ask_type(self):
        print(f'this is a {self.cuisine_type} restaurant!')
