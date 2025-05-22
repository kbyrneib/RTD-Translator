from ticker_builder import TickerBuilder

class RTD:
    """Model RTD Formula"""

    progId = '"Tws.TwsRtdServerCtrl"'

    def __init__(self, contract, topic="Last", connection=""):
        # Grabbing contract
        self.contract = contract

        # Build ticker
        builder = TickerBuilder(self.contract)
        self.ticker = builder.build_ticker()

        # Grab connection parameter
        self.connection = connection

        # Build topic
        self.topic = topic

        # Build overall formula
        if self.ticker != False:
            self.final_formula = self.build_final()
            print(f"\n{self.final_formula}\n")
        else:
            print(f"Security type not implemented for {self.contract.symbol} with conId {self.contract.conId}.")
    
    def build_final(self):
        """Function to build the final formula"""
        if self.connection == "":
            final_formula = f'RTD({self.progId},"",{self.ticker},"qt={self.topic}")'
        else:
            final_formula = f'=RTD({self.progId},"",{self.ticker},"qt={self.topic}","{self.connection}")'

        return final_formula