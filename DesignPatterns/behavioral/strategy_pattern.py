from abc import ABC, abstractmethod


class SellStrategy(ABC):

    @abstractmethod
    def sell_crypto(self, balance: float, currency: float) -> dict:
        pass


class SellLitte(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        btc = balance * 0.9
        ustd = (balance * 0.1) * currency
        return {"btc": btc, "ustd": ustd}


class SellHalf(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        btc = balance / 2
        ustd = (balance * 0.5) * currency
        return {"btc": btc, "ustd": ustd}


class SellFull(SellStrategy):

    def sell_crypto(self, balance: float, currency: float) -> dict:
        btc = 0
        ustd = balance * currency
        return {"btc": btc, "ustd": ustd}


class TradingApp:
    assets = {"btc": 100, "ustd": 0}

    currency = 30000

    def sell_order(self,sell_decision: SellStrategy):
        self.assets =  sell_decision.sell_crypto()

