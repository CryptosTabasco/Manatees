import bitso
API_KEY = "xxxxx"
API_SECRET = "XXXXXXXXXXXXXXXXXXX"
api = bitso.Api(API_KEY, API_SECRET)
CLABE = "000000000000000000"
WALLET_AUTOMATIC_SELL = "ABCXXXXXXXXXXXXXXXXX"
FIRST_NAMES = "xxxxx"
LAST_NAMES = "xxxxx"
NOTES_REF = "xx1"
NUMERIC_REF = "1234"

#Flow for transfer api

#get the balances
foundation_balance = api.balances()

#print foundation_balance.mxn.available
#print foundation_balance.btc.available

if foundation_balance.mxn.available > 100:
 print api.spei_withdrawal(amount=foundation_balance.mxn.available, first_names=FIRST_NAMES, last_names=LAST_NAMES, clabe=CLABE, notes_ref=NOTES_REF, numeric_ref=NUMERIC_REF)

#moving to btc automatic sell wallet address
#print api.btc_withdrawal(str(foundation_balance.btc.available), WALLET_AUTOMATIC_SELL)
