import bitso
import pycron

import config


class BotBistoPy:

    def __init__(self):
        self.api_key = config.API_KEY
        self.api_secret = config.API_SECRET
        self.api = bitso.Api(self.api_key, self.api_secret)
        self.balance = self.get_balance_available()

    def get_balance_available(self):
        # currency = bch,btc,eth,ltc,tusd,xrp,mxn
        return self.api.balances()

    def spei_withdrawal(self):
        self.trade_cryptos()
        if self.balance.mxn.available > 100:
            # pycron L-V 9-17
            if pycron.is_now('*/15 09-17 * * 1,2,3,4,5'):
                self.api.spei_withdrawal(
                    amount=self.balance.mxn.available,
                    first_names=config.FIRST_NAMES,
                    last_names=config.LAST_NAMES,
                    clabe=config.CLABE,
                    notes_ref=config.NOTES_REF,
                    numeric_ref=config.NUMERIC_REF
                )

    def trade_cryptos(self):
        # books = self.api.available_books()

        # obtener las cantidad de cryptos que hay
        btc = self.balance.btc.available
        eth = self.balance.eth.available
        xrp = self.balance.xrp.available
        ltc = self.balance.ltc.available
        bch = self.balance.bch.available
        tusd = self.balance.tusd.available

        # checar a cuanto es el precio de compra de la crypto
        btc_price = self.api.ticker('btc_mxn').last
        eth_price = self.api.ticker('eth_mxn').last
        xrp_price = self.api.ticker('xrp_mxn').last
        ltc_price = self.api.ticker('ltc_mxn').last
        bch_price = self.api.ticker('bch_mxn').last
        tusd_price = self.api.ticker('tusd_mxn').last

        # obtener el precio en mxn de las cryptos que hay
        btc_mxn = btc * btc_price
        eth_mxn = eth * eth_price
        xrp_mxn = xrp * xrp_price
        ltc_mxn = ltc * ltc_price
        bch_mxn = bch * bch_price
        tusd_mxn = tusd * tusd_price

        # validar si equivale a mas de 100 mxn vender
        if btc_mxn > 100:
            # vender
            pass
        if eth_mxn > 100:
            # vender
            pass
        if xrp_mxn > 100:
            # vender
            pass
        if xrp_mxn > 100:
            # vender
            pass
        if ltc_mxn > 100:
            # vender
            pass
        if bch_mxn > 100:
            # vender
            pass
        if tusd_mxn > 100:
            # vender
            pass


bot = BotBistoPy()
#print bot.balance
