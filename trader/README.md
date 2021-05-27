### TRADER

`trader.py` : Abstract trader class. It has below abstract methods.

- `buy()` : Buy coins
- `sell()` : Sell coins
- `init_target_buy_price()` : Init(Set) target price to buy
- `init_target_sell_price()` : Init(Set) target price to sell
- `get_target_buy_price()` : Get target price to buy
- `get_target_sell_price()` : Get target price to sell

Implementation classes can be created with the following format names : `{coin}_trader.py`

<br>

`doge_trader.py` : Trader class for doge coin

`account_trader.py` : Class for my account
