class Pub:
    def __init__(self, init_name, init_cash, init_drinks, init_customers, init_foods):
        self.name = init_name
        self.cash = init_cash
        self.drinks = init_drinks
        self.customers = init_customers
        self.foods = init_foods

    def find_customer_by_name(self, n):
        for customer in self.customers:
            if customer.name == n:
                return customer
        return None

    def find_drink_by_name(self, d):
        for drink in self.drinks:
            if drink.name == d:
                return drink
        return None

    def find_food_by_name(self, f):
        for food in self.foods:
            if food.name == f:
                return food
        return None

    def customer_buys_drink(self, customer_name, drink_name):
        customer = self.find_customer_by_name(customer_name)
        drink = self.find_drink_by_name(drink_name)
        if customer.age < 18:
            print("Too young to drink")
        elif (customer.drunkenness < 15) and (customer.wallet >= drink.price) and (drink.stock > 0):
            self.cash += drink.price
            customer.wallet -= drink.price
            customer.drunkenness += drink.alcohol_level
            drink.stock -= 1
        else:
            print("You've had enough mate!")

    def customer_buys_food(self, customer_name, food_name):
        customer = self.find_customer_by_name(customer_name)
        food = self.find_food_by_name(food_name)
        self.cash += food.price
        customer.wallet -= food.price
        if customer.drunkenness >= food.rejuvination:
            customer.drunkenness -= food.rejuvination
        else:
            customer.drunkenness = 0

    def stock_value(self, drink_name):
        drink = self.find_drink_by_name(drink_name)
        return drink.price * drink.stock
