
"""
 This problem is a mix of singleton and proxy pattern
 We Have to create Logger system(singleton)  using Proxy pattern
"""
class Logger:
    _instance = None
    
    @classmethod
    def getInstance(cls):
        if cls._instance  is None:
            cls._instance = cls()
            cls._instance.log_file = "logfile.txt"
            print("Logger instance created")
        return cls._instance    
    def write(self,msg):
        with open(self._instance.log_file,"a") as f:
            f.write(msg)
            f.write("\n")
            
        
        
class LoggerProxy:
    def __init__(self):
       self.logger = Logger.getInstance()
    def write(self,msg):
        self.logger.write(msg)    
        
if __name__ == "__main__":
    Logger = LoggerProxy()
    Logger.write("Hello, world!")