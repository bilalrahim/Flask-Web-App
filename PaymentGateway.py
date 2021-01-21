class PaymentProvider:
    """
    Takes in amount and returns the service provider that should be used
    """

    def __init__(self, amount):
        self.amount = amount
    
    def getPaymentProvider(self):

        if self.amount <= 0:
            return 0
        if self.amount < 20:
            return "CheapPaymentGateway"

        if self.amount >= 21 and self.amount <= 500:
            # Tries ExpensiveGateway, incase of an error tries cheapgateway once.
            # Returns 0 if both does not work
            try:
                return "ExpensivePaymentGateway"
            except:
                try:
                    return "CheapPayGateway"
                except:
                    return 0

        if self.amount > 500:
            # Tries Premium Payment Provider thrice.
            counter = 0
            while(counter <= 3):
                try:
                    return "PremiumPaymentGateway"
                except:
                    return 0
        else:
            return 0