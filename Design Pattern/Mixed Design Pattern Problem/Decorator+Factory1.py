
"""
 Decorator + Factory
 we Have to create Message system which can send message through using Email/SMS system
 And we have to add HighLight and Link in each sending message
"""

from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def sendMessage(self,message):
        pass
class EmailSender(Notification):
    def sendMessage(self, message):
        print(f"Email: {message}")
class SMSSender(Notification):
    def sendMessage(self, message):
        print(f"SMS: {message}")
        
class NotificationFactory:
    @staticmethod
    def getSender(type):
        if type == "email":
            return EmailSender()
        elif type == "sms":
            return SMSSender()
        else:
            raise Exception("Invalid notification type")
        
class NotificationDecorator(Notification):
      def __init__(self,sender):
          self.sender = sender
      def sendMessage(self, message):
          return self.sender.sendMessage(message)     
                    
class  AddHighLightDecorator(NotificationDecorator):
    def __init__(self,sender):
        super().__init__(sender)
    def sendMessage(self, message):
        return   self.sender.sendMessage(f"<b>{message}</b>")
    
class AddLinkDecorator(NotificationDecorator):
    def __init__(self,sender):
        super().__init__(sender)
    def sendMessage(self, message):
        return self.sender.sendMessage(f"<a>{message}</a>")
if __name__ == "__main__":
    sender = NotificationFactory.getSender("email")
    sender.sendMessage("Hello World")
    sender = AddHighLightDecorator(sender)
    sender.sendMessage("Hello World")
    sender = AddLinkDecorator(sender)
    sender.sendMessage("Hello World")
                