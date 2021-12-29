'''
Single Responsibility Principle:
            This principle states that “a class should have only one reason to change”
'''

class MedicalStore:
    medicines = []
    quantities = []
    prices = []
    status = 'unpaid'

    def buy_medicine(self,name,quantity,price):
        '''
        This method is use to buy medicines.
        This method should be the part of MedicalStore class.
        '''
        self.medicines.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def totalPrice(self):
        '''
        This method print total price.
        This method should also be the part of MedicalStore class
        '''
        total_price = 0
        for i in range(len(self.medicines)):
            total_price += (self.quantities[i] * self.prices[i])
        print(total_price)

class PaymentProcess:
    '''
    Now this class take the responsibility of payment.
    If we need to change anything regarding payment
    the MedicalStore class won't need to change
    '''
    def CreditPayment(self,store,security_code):
        print(f'Verifying security code : {security_code}')
        print('Payment Done using credit')
        store.status = 'paid'
    def DebitPayment(self,store,security_code):
        print(f'Verifying security code : {security_code}')
        print('Payment Done using debit')
        store.status = 'paid'


MyStore = MedicalStore()
MyStore.buy_medicine('Dolo 650',1,90)
MyStore.buy_medicine('Dart',2,320)
MyStore.buy_medicine('combiflam',1,150)
MyStore.totalPrice()
MyPay = PaymentProcess()
MyPay.CreditPayment(MyStore,'93ufb')
