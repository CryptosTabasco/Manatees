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
        self.balance = self.api.balances().mxn.available
        return self.balance

    def spei_withdrawal(self):
        if self.get_balance_available() > 100:
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