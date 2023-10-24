# CoinbaseTradingBot
A fun full stack project for Python users looking to learn asynchronous connection and websockets for trading on Coinbase (cbpro and copra).

## Basic Concept
<p>Using API key, secret and passphrase (provided via .env file), connect to Coinbase for stable pair trading on WBTC-BTC. Stable pair trading on Coinbase is without maker fees. An established websocket connection is used to perform real-time trading. It could easily be implemented for real-time analysis and trading for technical indicators.</p>

<p>This is a base concept that would need to be re-worked for another user. The concepts of the build are in a single file (main.py). Orders are monitored via a JSON file. This is done in case the connection is monetarily lost. Re-running the bot would not require placing new orders.</p>

<p>ALL INITIAL ORDERS NEED TO BE PLACED VIA COINBASE. Users should make any price alterations, run the bot, log in to Coinbase and place orders. The bot will begin monitoring the new orders.</p>

## Implementation
There are tasks that will need to be performed by an end user to utilize the trading bot.

- Coinbase API key, secret and passphrase (.env)
- Built for WBTC-BTC stable pair trading at a specific range. User will need to alter this pair/range for their own use
- Environment variables file is not provided (.env). There are only three variables.

```
p = os.getenv('passphrase')
API_S = os.getenv('API_S')
API_K = os.getenv('API_K')
```

### Install
Environment is built in Python 3.11. A requirements.txt file has been provided for downloading of files. The file was generated from a Windows station, but the program is meant to be run on Linux. You may need to make slight alterations for a Linux.

```
pip install -r requirements.txt
```
## Contributing
Please ask if you'd like to contribute. I will NOT be adding to the repository.

## Contact
Please feel free to contact me! I am open to offers.

[Telegram Channel](https://t.me/parcaeio) <br>
[Telegram Contact](https://t.me/c1im4cu5) <br>
