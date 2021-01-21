# Coding Exercise for Upwork Client.
# Built a basic front end to get a better view.
# Used logging for debugging.
# Used pytest for testing.
# All test cases in test_.py.

import logging
logging.basicConfig(level=logging.DEBUG, filename='payment.log')
from flask import Flask, render_template, request
from PaymentGateway import PaymentProvider

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def ProcessPayment():

    if request.method == "POST":
        
        # Mandotary fields checks are implemented on the front-end on input field.
        
        logging.info("Got request from front-end")

        CreditCardNumber = request.form["CreditCardNumber"]
        CardHolder = request.form["CardHolder"]
        ExpirationDate = request.form['ExpirationDate']

        # Incase security code is empty we will simply skip it.
        try:
            SecurityCode = request.form['SecurityCode']
            logging.info("Recieved Security Code.")
        except KeyError:
            logging.info("Security field empty.")
            exit
        
        Amount = request.form['Amount']
        provider = PaymentProvider(int(Amount)).getPaymentProvider()
        
        return render_template("payment.html" , provider = provider)

    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 3000)