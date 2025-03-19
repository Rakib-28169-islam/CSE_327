import logging
from enum import Enum
from datetime import datetime

class TransitionType(Enum):
    
    WITHDRAW = "Withdraw"
    DEPOSIT = "Deposit"
    TRANSFER = "Transfer"
    

logging.basicConfig(
    filename = "bank.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%d-%m-%Y %H:%M:%S"
)

class BankService:
    
    def __init__(self):
        self.accounts = accounts = {
        '123456': 1000,
        '234567': 2000,
        '345678': 3000
    }
        
    def verifyingFunds(self,account_number,amount):
        tmp = self.get_balance(account_number)
        if tmp - amount < 0:
            return False
        else:
            return True
    def verifying_account(self,account_number):
        if account_number in self.accounts:
            return True
        else:
            return False
    def get_balance(self,account_number):
        return self.accounts[account_number]
    def withdraw_money(self,account_number,amount):
        tmp = self.get_balance(account_number)
        if tmp - amount < 0:
            return False 
        else:
            self.accounts[account_number] = tmp - amount
        
            if tmp > self.accounts[account_number]:
               return True    
    def  transfer_money(self,from_account,to_account,amount):
        if not self.verifyingFunds(from_account,amount):
            return False
        else:
            if not self.withdraw_money(from_account,amount):
               return False
            else:
                self.accounts[to_account] = self.accounts[to_account] + amount
                return True
    def deposit_money(self,account_number,amount):
        self.accounts[account_number] = self.accounts[account_number] + amount
        return True
 
class FraudDetector:
    def send_fraud_alert(self,account_number,message):
        print(f"Fraud Alert: {account_number} -> {message}")
        
class NotificationService:
    def send_notification(self,account_number,message):
        print(f"Notification for Customer: {account_number} -> {message}")
class TransitionLogger:
    def log_transition(self,account_number,transition_type,amount):
        log_message = f"Account: {account_number} --{transition_type}-- {amount} on {datetime.now()}"
        print(log_message)
        logging.info(log_message)
        
        
        
class PaymentFacade:
    __bank_service = BankService()
    __fraud_detector = FraudDetector()
    __notification_service = NotificationService()
    __transition_logger = TransitionLogger()

    def processPayment(self, transition_type, account_number, amount, to_account=None):
        if not self.__bank_service.verifying_account(account_number):
            self.__fraud_detector.send_fraud_alert(account_number, "Invalid Account")
            return
        
        def withdraw():
            if self.__bank_service.verifyingFunds(account_number, amount):
                if self.__bank_service.withdraw_money(account_number, amount):
                    return True, f"withdrawn from {account_number}"
            return False, "Insufficient funds"

        def deposit():
            self.__bank_service.deposit_money(account_number, amount)
            return True, f"deposited to {account_number}"

        def transfer():
            if self.__bank_service.verifying_account(to_account) and self.__bank_service.verifyingFunds(account_number, amount):
                if self.__bank_service.transfer_money(account_number, to_account, amount):
                    return True, f"transferred to {to_account}"
            return False, "Insufficient funds or invalid transfer account"

        # Switch-case equivalent using a dictionary
        operations = {
            TransitionType.WITHDRAW: withdraw,
            TransitionType.DEPOSIT: deposit,
            TransitionType.TRANSFER: transfer
        }

        success, message = operations.get(transition_type, lambda: (False, "Invalid transaction type"))()

        if success:
            self.__notification_service.send_notification(account_number, f"Amount {amount} was successfully {message}")
            self.__transition_logger.log_transition(account_number, transition_type, amount)
        else:
            self.__fraud_detector.send_fraud_alert(account_number, message)


if __name__ == "__main__":
    payment_facade = PaymentFacade()
    payment_facade.processPayment(TransitionType.DEPOSIT,"123456",1000)
    payment_facade.processPayment(TransitionType.TRANSFER,"123456",1000,"234567")