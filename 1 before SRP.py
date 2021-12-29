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

    def Pay(self,payment_type,security_code):
        '''
        This method is used for payment.
        Problem : It violates SRP principle as the class should have only one Responsibility.
        Solution : So to solve we will make a different class PaymentProcess
        '''
        if payment_type == 'credit':
            print(f'Verifying security code : {security_code}')
            print('Payment Done using credit')
            status = 'paid'
        elif payment_type == 'debit':
            print(f'Verifying security code : {security_code}')
            print('Payment Done using debit')
            status = 'paid'
        else:
            print("INVALID PAYMENT METHOD!!!")

MyStore = MedicalStore()
MyStore.buy_medicine('Dolo 650',1,90)
MyStore.buy_medicine('Dart',2,320)
MyStore.buy_medicine('combiflam',1,150)
MyStore.totalPrice()
MyStore.Pay('debit','93u9e')
