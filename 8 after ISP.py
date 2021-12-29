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

    @abstractmethod
    def pay(self,store):
        pass

class PaymentProcessSMS(PaymentProcess):
    '''
    We have shift sms_auth method to this class.
    '''
    @abstractmethod
    def sms_auth(self,code):
        pass

class CreditPaymentProcess(PaymentProcess):
    '''
    Now we don't need to implement sms_auth method in this class.
    '''
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using credit')
        store.status = 'paid'

class DebitPaymentProcess(PaymentProcessSMS):
    def __init__(self,security_code):
        self.security_code = security_code

    def sms_auth(self,code):
        print(f'Verifying sms code {code}')

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using debit')
        store.status = 'paid'

class PaytmPaymentProcess(PaymentProcessSMS):
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
MyPay = DebitPaymentProcess('1234567890')
MyPay.sms_auth('1231')
MyPay.pay(MyStore)
