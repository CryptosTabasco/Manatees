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
        books = self.api.available_books()

        crypto_quantity = {}
        crypto_price = {}

        cryptos = self.balance.__dict__

        # obtener las cantidad de cryptos que hay
        for data in self.balance.currencies:
            crypto_quantity.update({data: cryptos[data].available})

        # obtener el precio actual de cada crypto
        for book in books.books:
            if book.endswith('mxn'):
                crypto_price.update({book: self.api.ticker(book).last})

        # obtener el precio en mxn de las cryptos que hay
        btc_mxn = crypto_quantity['btc'] * crypto_price['btc_mxn']
        eth_mxn = crypto_quantity['eth'] * crypto_price['eth_mxn']
        xrp_mxn = crypto_quantity['xrp'] * crypto_price['xrp_mxn']
        ltc_mxn = crypto_quantity['ltc'] * crypto_price['ltc_mxn']
        bch_mxn = crypto_quantity['bch'] * crypto_price['bch_mxn']
        tusd_mxn = crypto_quantity['tusd'] * crypto_price['tusd_mxn']

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
bot.trade_cryptos()
# print bot.balance
