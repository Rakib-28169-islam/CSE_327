import os
from datetime import datetime
 
 #cloud storage class
class CloudStorage:
     def store_file(self,file_name,data):
         with open(file_name,"a") as f:
             f.write(data)
             f.write("\n")
         print("File stored in cloud")   
     def read_file(self,file_name):
         if os.path.exists(file_name):
             with open(file_name ,"r")as f:
                 data = f.read()
             print("File read from cloud\n",data)      
             
class ProxyCloudStorage: 
    def __init__(self,user_role,cloudStorage=None):
        self._user_role =   user_role     
        self._cloudStorage = cloudStorage
    def store_file(self,file_name,data):
        if self._user_role == "admin":
            self._cloudStorage.store_file(file_name,data)
        else:
            print("Access denied")    
    def read_file(self,file_name):
        self._cloudStorage.read_file(file_name)        
                
class FileDecorator(CloudStorage):
       def __init__(self,cloudStorage):
           self._cloudStorage = cloudStorage
       def store_file(self,file_name,data):
           self._cloudStorage.store_file(file_name,data)
    #    def read_file(self,file_name):
    #        self._cloudStorage.read_file(file_name)
class UpperCaseDecorator(FileDecorator):
     def  __init__(self,cloudStorage):
         super().__init__(cloudStorage)
     def store_file(self,file_name,data):
         data = data.upper()
         self._cloudStorage.store_file(file_name,data)
     
class TimeStampDecorator(FileDecorator):
     def  __init__(self,cloudStorage):
         super().__init__(cloudStorage)
     def store_file(self,file_name,data):
         timeStamp = f"Time Stamp : {datetime.now()}\n"
         data = timeStamp + data
         self._cloudStorage.store_file(file_name,data)   
         
if __name__ == "__main__":
   
    decorateFile = UpperCaseDecorator(CloudStorage())
    decorateFile = TimeStampDecorator(decorateFile)
    adminProxy = ProxyCloudStorage("admin",decorateFile)
    adminProxy.store_file("test.txt","Update File")
    adminProxy.read_file("test.txt")
    userProxy = ProxyCloudStorage("user",decorateFile)
    userProxy.store_file("test.txt","Update File")#Access denied
                         
                    