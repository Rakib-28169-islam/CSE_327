from abc import ABC,abstractmethod
class Image(ABC):
    @abstractmethod
    def display(self):
        pass
    
#RealImage
class RealImage(Image):
    def __init__(self,fileName):
        self.fileName = fileName  
    def __load_from_disk(self):
        print(f"Loading {self.fileName} Image from disk")
    def display(self):
        self.__load_from_disk()
        print(f"Displaying {self.fileName} Image")   
#ProxyImage
class ProxyImage(Image):
    __filename = None
    __realImage = None
    
    def __init__(self,fileName):
        self.__filename = fileName
        self.__realImage = None
    def display(self):
        if self.__realImage is None:
            self.__realImage = RealImage(self.__filename)
            print("Image Proxy created and Loaded")
        self.__realImage.display() 
        
        
if __name__ == "__main__":
    image = ProxyImage("test.jpg")
    image.display()
    print("\n")
    image.display()
    del image
    