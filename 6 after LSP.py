'''
Liskov’s Substitution Principle:
        According to this principle
        “Derived or child classes must be substitutable for their base or parent classes“.
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
    We have removed security_code parameter from pay method.
    and we have added constructor to each class.
    Even if something other than security_code is required to process.
    We don't have to change PaymentProcess class.
    '''
    @abstractmethod
    def pay(self,store):
        pass

class CreditPaymentProcess(PaymentProcess):
    '''
    Constructor Added Here
    '''
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using credit')
        store.status = 'paid'

class DebitPaymentProcess(PaymentProcess):
    '''
    Constructor Added Here
    '''
    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,store):
        print(f'Verifying security code : {self.security_code}')
        print('Payment Done using debit')
        store.status = 'paid'

class PaytmPaymentProcess(PaymentProcess):
    '''
    Constructor Added Here
    '''
    def __init__(self,mobileno):
        self.mobileno = mobileno

    def pay(self,store):
        print(f'Verifying Mobile Number : {self.mobileno}')
        print('Payment Done using Paytm')
        store.status = 'paid'

MyStore = MedicalStore()
MyStore.buy_medicine('Dolo 650',1,90)
MyStore.buy_medicine('Dart',2,320)
MyStore.buy_medicine('combiflam',1,150)
MyStore.totalPrice()
MyPay = PaytmPaymentProcess('1234567890')
MyPay.pay(MyStore)
