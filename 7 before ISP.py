'''
Interface Segregation Principle:
        According to this principle
        “Many client-specific interfaces are better than one general-purpose interface.”
'''

from abc import ABC,abstractmethod

class MedicalStore:
    medicines = []
    quantities = []
    prices = []
    status = 'unpaid'

    def buy_medicine(self,name,quantity,price):
        self.medicines.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def totalPrice(self):
        total_price = 0
        for i in range(len(self.medicines)):
            total_price += (self.quantities[i] * self.prices[i])
        print(total_price)

class PaymentProcess(ABC):
    '''
    Problem : Let's say we have another method sms_auth (as you can see below)
              which authenticate the sms code.but credit payment don't need
              sms code verification.
              This violates ISP as PaymentProcess class enforce CreditPaymentProcess
              class to implement an interface which is irrelevant to it.
    Solution : To solve this problem we will create another class PaymentProcessSMS
               and add sms_auth method from PaymentProcess class.
               Extend this class to only those Payment class who have sms authentication.

    '''
    @abstractmethod
    def pay(self,store):
        pass

    #This new abstractmethod is added here.
    @abstractmethod
    def sms_auth(self,code):
        pass

class CreditPaymentProcess(PaymentProcess):
    def __init__(self,security_code):
        self.security_code = security_code

    def sms_auth(self,code):
        #We have to implement it because This class is subclass of abstract class
        raise Exception('sms authentication is not supported in credit.')

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using credit')
        store.status = 'paid'

class DebitPaymentProcess(PaymentProcess):
    def __init__(self,security_code):
        self.security_code = security_code

    def sms_auth(self,code):
        print(f'Verifying sms code {code}')

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using debit')
        store.status = 'paid'

class PaytmPaymentProcess(PaymentProcess):
    def __init__(self,mobileno):
        self.mobileno = mobileno

    def sms_auth(self,code):
        print(f'Verifying sms code {code}')

    def pay(self,store):
        print(f'Verifying Mobile Number : {self.mobileno}')
        print('Payment Done using Paytm')
        store.status = 'paid'

MyStore = MedicalStore()
MyStore.buy_medicine('Dolo 650',1,90)
MyStore.buy_medicine('Dart',2,320)
MyStore.buy_medicine('combiflam',1,150)
MyStore.totalPrice()
MyPay = CreditPaymentProcess('1234567890')
MyPay.sms_auth('1231')          #This will raise error
MyPay.pay(MyStore)
