class Pizza:   
    #base parent pizza class  
    def __init__(self):
        self.name =""
        self.dough =""
        self.sauce =""
        self.toppings =[]
    def prepare(self):
        print(f"Preparing {self.name}")
        print(f"Tossing dough...")
        print(f"Adding sauce...")
        print(f"Adding toppings:")
        for topping in self.toppings:
            print(f"    {topping}")
    def bake(self):
        print(f"Bake for 25 minutes at 350")
    def cut(self):
        print(f"Cutting the pizza into diagonal slices")    
    def boxing(self):
        print(f"Place pizza in official PizzaStore box")    
        
class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings =["Fresh Mozzarella","Parmesan","Tomatoes"]
class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Veggie Pizza"
        self.dough = "Thin Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings =["Fresh Mozzarella","Parmesan","Tomatoes","Spinach","Olives"]
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Regular Crust"
        self.sauce = "Marinara Pizza Sauce"
        self.toppings =["Fresh Mozzarella","Parmesan","Pepperoni","Tomatoes"]        
 
# class PizzaFactory:
#     @staticmethod
#     def create_pizza(pizza_type):
#         pizza_types={
#             "cheese": CheesePizzaFactory().create_pizza(),
#             "veggie": VeggiePizzaFactory().create_pizza(),
#             "pepperoni": PepperoniPizzaFactory().create_pizza()
#         }
#         return pizza_types.get(pizza_type.lower())
    
class CheesePizzaFactory:
    def create_pizza(self):
        return CheesePizza()
class VeggiePizzaFactory:
    def create_pizza(self):
        return VeggiePizza()
class PepperoniPizzaFactory:
    def create_pizza(self):
        return PepperoniPizza()        
        
   
class FactoryRegistry:
    instance = None
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = FactoryRegistry()
            cls.instance.factories = {}
        return cls.instance
    def register_factory(self,pizza_type,factory):
        self.factories[pizza_type] = factory    
    def get_factory(self,pizza_type):
        return self.factories.get(pizza_type)
class PizzaStore:
    
    def __init__(self):
       
        self.registry = FactoryRegistry.get_instance()
        self.registry.register_factory("cheese",CheesePizzaFactory())
        self.registry.register_factory("veggie",VeggiePizzaFactory())
        self.registry.register_factory("pepperoni",PepperoniPizzaFactory())
    def order_pizza(self,pizza_type):
        factory = self.registry.get_factory(pizza_type)
        if factory:
           pizza = factory.create_pizza()   
           if  pizza:
               pizza.prepare()
               pizza.bake()
               pizza.cut()
               pizza.boxing()
               return pizza
        else :
            print(f"Sorry we don't have {pizza_type} pizza")
            return None

if __name__ == "__main__":
  
    store = PizzaStore() 
    store.order_pizza("cheese")
    print("\n")
    store.order_pizza("veggie")
    print("\n")
    store.order_pizza("pepperoni")
    print("\n")
    store.order_pizza("meat")
    
    
    
    