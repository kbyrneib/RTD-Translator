import time
from ibapi.client import *
from ibapi.wrapper import *
from rtd import RTD
import sys

class RTDApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, wrapper=self)

    def nextValidId(self, orderId):
        self.orderId = orderId
        self.start()

    def nextId(self):
        self.orderId += 1
        return self.orderId

    def start(self):
        # Requesting contract details
        contract_id = input("Enter contract ID (or type 'exit' to end the program): ")

        # Exiting if enter 'exit' or 'Exit' or 'EXIT' etc..
        if contract_id.lower().strip() == "exit":
            self.disconnect()

        contract = Contract()
        contract.conId = contract_id
        self.reqContractDetails(self.nextId(), contract)

    def contractDetails(self, reqId, contractDetails):
        RTD(contractDetails.contract, topic="Close", connection="paper")
        self.start()

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson=""):
        # Dictionary of relevant error strings
        error_codes = {200 : "\nNo security definition found - enter a valid contract ID.\n", 
                       320 : "\nUnable to parse the provided contract ID.\n", 
                       321: "\nYou did not input anything.\n"}

        if errorCode in [200, 320, 321]:
            print(error_codes[errorCode])
            self.start()

# Required args for connectivity
host = "localhost"
port = 7497
clientId = 0

# Creating, connecting and running app
app = RTDApp()
app.connect(host, port, clientId)
app.run()