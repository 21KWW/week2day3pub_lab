class Pub:
    def __init__(self, init_name, init_cash, init_drinks, init_customers):
        self.name = init_name
        self.cash = init_cash
        self.drinks = init_drinks
        self.customers = init_customers

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
        
    def customer_buys_drink():
        pass