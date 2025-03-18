from enum import Enum

#enum foodType
class FoodType(Enum):
    PIZZA = "Pizza"
    PASTA = "Pasta"
#abstract Product 
class FoodItem:
    def prepare(self):
        pass 
    
#concrete Product    
class CheesePizza(FoodItem):
    def prepare(self):
        print("Cheese Pizza prepared")
class PepperoniPizza(FoodItem):
    def prepare(self):
        print("Pepperoni Pizza prepared")
class Pasta(FoodItem):
    def prepare(self):
        print("Pasta prepared")

#Concrete Factories
class CheesePizzaFactory:
    def create_food(self):
        return CheesePizza()
class PepperoniPizzaFactory:
    def create_food(self):
        return PepperoniPizza()
class PastaFactory:
    def create_food(self):
        return Pasta()   
    
#Singleton Factory Registry
class FactoryRegistry:
    _instance = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance =  FactoryRegistry()
            cls._instance.factories = {}    
        return cls._instance     
    def register_factory(self,foodType,factory):
        self.factories[foodType] = factory
    def get_factory(self,foodType):
        return self.factories.get(foodType)   
    
if __name__ == "__main__":
    registry = FactoryRegistry.get_instance() 
    registry.register_factory(FoodType.PIZZA,PepperoniPizzaFactory())   
    registry.register_factory(FoodType.PASTA,PastaFactory())
    
    order =  [FoodType.PIZZA,FoodType.PASTA]
    for item in order:
        factory = registry.get_factory(item)
        if factory:
            food = factory.create_food()
            food.prepare()
        else:
            print("No factory registered for",item)        