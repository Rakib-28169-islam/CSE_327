class Internet:
    def connect(self):
        pass
class RealInternet(Internet):
    def connect(self,site):
        print(f"Connecting to {site}")
        
class InternetProxy(Internet):
    def __init__(self):
        self.banned_site ={'cnn.com','fox.com',"badsite.com"}
        self.internet = RealInternet()
    def connect(self,site):
        if site.lower() in self.banned_site:
            print(f"Access Denied for {site}")
        else:
            self.internet.connect(site)
            
if __name__ == "__main__":
    proxy = InternetProxy()
    proxy.connect('cnn.com')
    proxy.connect('google.com')
    proxy.connect('badsite.com')
    proxy.connect('fox.com')
            