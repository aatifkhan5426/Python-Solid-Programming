'''
Open/Closed Principle:
        This principle states that
        “software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification”
'''

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

class PaymentProcess:
    '''
    Problem : If we want to add any other payment method, we have to change
              PaymentProcess class and this violates OCP principle.
    Solution : To solve it we will turn this class into abstract class and
               extend each payment process class from it.

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
