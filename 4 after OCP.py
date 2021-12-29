'''
Open/Closed Principle:
        This principle states that
        “software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification”
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
    Now if we add any other payment method we don't need to change
    MedicalStore and PaymentProcess classes.
    We have added Paytm payment.
    '''
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
    New payment process added.
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
