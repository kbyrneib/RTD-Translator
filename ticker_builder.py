class TickerBuilder:
    """Builds a Ticker"""

    # Define dictionary of possible values in ticker
    ticker_fields = {
        "conId": "conid=",
        "symbol" : "sym=",
        "secType" : "sec=",
        "lastTradeDateOrContractMonth" : "exp=",
        "strike" : "strike=",
        "right" : "right=",
        "multiplier" : "mult=",
        "exchange" : "exch=",
        "primaryExchange" : "prim=",
        "currency" : "cur=",
        "localSymbol" : "loc=",
        "tradingClass" : "tc=",
    }

    # Build dictionary containing required ticket fields for each security type
    requirements = dict.fromkeys(["STK", "FUND", "IND", "BOND", "CFD", "CMDTY", "CASH", "CRYPTO"], ["symbol", "secType", "exchange", "currency"])
    requirements.update(dict.fromkeys(["FUT"], requirements["STK"] + ["multiplier", "lastTradeDateOrContractMonth"]))
    requirements.update(dict.fromkeys(["OPT", "FOP", "WAR"], requirements["FUT"] + ["strike", "right"]))

    def __init__(self, contract):
        self.security_type = contract.secType
        self.contract = contract
        self.build_ticker()

    def build_ticker(self):
        """Function to build ticker based on secType requirements"""
        ticker = []

        try:
            for ticker_field in self.requirements[self.security_type]:
                ticker.append(f'"{self.ticker_fields[ticker_field]}{getattr(self.contract, ticker_field)}"')
        except KeyError:
            return False

        return ",".join(ticker)