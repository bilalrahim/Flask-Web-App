from PaymentGateway import PaymentProvider

#Tests

# Checking Extreams
def test_1():
    assert PaymentProvider(100000000).getPaymentProvider() == "PremiumPaymentGateway"
    assert PaymentProvider(0).getPaymentProvider() == 0
# Checking for decimal values

def test_2():
    assert PaymentProvider(1000.01212).getPaymentProvider() == "PremiumPaymentGateway"

# Checking each payment provider individually

# < 20 is CheapPaymentGateway
def test_3():
    assert PaymentProvider(15).getPaymentProvider() == "CheapPaymentGateway"

# 25-500 is ExpensivePaymentGateway
def test_4():
    assert PaymentProvider(300).getPaymentProvider() == "ExpensivePaymentGateway"

# > 500 is PremiumPaymentGateway
def test_5():
    assert PaymentProvider(1000).getPaymentProvider() == "PremiumPaymentGateway"