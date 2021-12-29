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
    @abstractmethod
    def pay(self,store,security_code):
        pass

class CreditPaymentProcess(PaymentProcess):
    def pay(self,store,security_code):
        print(f'Verifying security code : {security_code}')
        print('Payment Done using credit')
        store.status = 'paid'

class DebitPaymentProcess(PaymentProcess):
    def pay(self,store,security_code):
        print(f'Verifying security code : {security_code}')
        print('Payment Done using debit')
        store.status = 'paid'

class PaytmPaymentProcess(PaymentProcess):
    '''
    Problem : Let's say paytm need mobile number instead of security code.
              so if we change parameter from security_code to mobileno
              we also need to change PaymentProcess class parameters and
              This violates LSP principle.
    Solution : To solve this in our example we can simply add a constructor
               to each class.
    '''
    def pay(self,store,security_code):
        print(f'Verifying security code : {security_code}')
        print('Payment Done using Paytm')
        store.status = 'paid'

MyStore = MedicalStore()
MyStore.buy_medicine('Dolo 650',1,90)
MyStore.buy_medicine('Dart',2,320)
MyStore.buy_medicine('combiflam',1,150)
MyStore.totalPrice()
MyPay = PaytmPaymentProcess()
MyPay.pay(MyStore,'93ufb')
