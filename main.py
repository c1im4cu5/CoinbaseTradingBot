#Created by Climacus at https://github.com/c1im4cu5
#Open to Offers for Employment
#Email: thebrotherscain@gmail.com

#Check out ReadMe for more file details. 

import asyncio
from datetime import datetime
import json
import cbpro
from copra.websocket import Channel, Client

import sys, os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
p = os.getenv('passphrase')
API_S = os.getenv('API_S')
API_K = os.getenv('API_K')

KEY = API_S
SECRET = API_K
PASSPHRASE = p
loop = asyncio.get_event_loop()
channel = Channel(name='user', product_ids='WBTC-BTC')

auth_client = cbpro.AuthenticatedClient(KEY, SECRET, PASSPHRASE)

order_lst = []
p = os.path.dirname(os.path.abspath(__file__))

class Tick:
    def __init__(self, tick_dict):
        self.product_id = tick_dict['product_id']
        self.best_bid = float(tick_dict['best_bid'])
        self.best_ask = float(tick_dict['best_ask'])
        self.price = float(tick_dict['price'])
        self.side = tick_dict['side']
        self.size = float(tick_dict['last_size'])
        self.time = datetime.strptime(tick_dict['time'], '%Y-%m-%dT%H:%M:%S.%fZ')

    def spread(self):
        return self.best_ask - self.best_bid
    def __repr__(self):
        rep = "{}\t\t\t\t {}\n".format(self.product_id, self.time)
        rep += "=============================================================\n"
        rep += " Price: ${:.2f}\t Size: {:.8f}\t Side: {: >5}\n".format(self.price, self.size, self.side)
        rep += "Best ask: ${:.2f}\tBest bid: ${:.2f}\tSpread: ${:.2f}\n".format(self.best_ask, self.best_bid, self.spread)
        rep += "=============================================================\n"
        return rep

class Ticker(Client):

    def on_message(self, message):
        p_statement = ""
        order_lst=[]
        if message['type'] == 'subscriptions':
            p_statement = "\n==================== Active Subscription ====================\n"
            p_statement += "========== Bot created by @c1im4cu5 (Open to offers) ==========\n"
            print(p_statement)
        if message['type'] == 'received':
            p_statement = "====================================================\n"
            p_statement += "Type: " + message['type'] + "\n"
            p_statement += "Pair: " + message['product_id'] + "\n"
            p_statement += "Side: " + message['side'] + "\n"
            p_statement += "Size: " + message['size'] + "\n"
            p_statement += "RECIEVED\n"
            p_statement += "==================================================="
            print (p_statement)

            order_dict={
                    'order_id': message['order_id'],
                    'product_id': message['product_id'],
                    'side': message['side'],
                    'size': message['size'],
                    'price': message['price'],
                    'status': message['type'],
                    'time': message['type']
                    }
            orders_lst = load_orders()
            order_lst.append(order_dict)
            save_orders(order_lst)

        if message['type'] == "open":
            for i in range(len(order_lst)):
                if order_lst[i]['order_id'] == message['order_id']:
                    order_lst[i]['status'] == message['type']

                    p_statement += "============================================\n"
                    p_statement += "NEW ORDER GENERATED\n"
                    p_statement += "Order ID: " + order_lst[i]['status'] + "\n"
                    p_statement += "Product ID: " + order_lst[i]['product_id'] + "\n"
                    p_statement += "Size: " + order_lst[i]['size'] + "\n"
                    p_statement += "Side: " + order_lst[i]['side'] + "\n"
                    p_statement += "=============================================\n\n"

        if message['type'] == 'match':
            p_statement = "====================================================\n"
            p_statement += "Type: " + message['type'] + "\n"
            p_statement += "Pair: " + message['product_id'] + "\n"
            p_statement += "Side: " + message['side'] + "\n"
            p_statement += "Size: " + message['size'] + "\n"
            p_statement += "ORDER COMPLETE\n"
            p_statement += "==================================================="
            print (p_statement)

        if message['type'] == 'done':
            if message['reason'] == 'filled':
                order_lst = load_orders()
                p_statement = "====================================================\n"
                p_statement += "Type: " + message['type'] + "\n"
                p_statement += "Pair: " + message['product_id'] + "\n"
                p_statement += "Side: " + message['side'] + "\n"
                p_statement += "Size: " + message['size'] + "\n"
                p_statement += "ORDER FILLED\n"
                p_statement += "==================================================="
                print (p_statement)
                for i in range(len(order_lst)):
                    if order_lst[i]['order_id'] == message['order_id']:
                            order_lst[i]['status'] == 'filled'
                            place_order(order_lst[i])

def load_orders():
    orders=[]
    with open( p + r"/orders.json", "r") as read_file:
        orders = json.load(read_file)
    return orders

def delete_order(order):
    orders = load_orders()
    for i in range(len(orders)):
        if orders[i]['order_id'] == order['order_id']:
            del orders[i]
    with open(p + r'/orders.json', 'w') as fout:
        json.dump(orders , fout)

def save_orders(order):
    orders = load_orders()
    order=order
    orders.extend(order)
    with open(p + r'/orders.json', 'w') as fout:
        json.dump(orders , fout)

def place_order(order):
    if order['side']== 'sell':
        if order['price'] == "1.0009":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='buy', price="0.9994", size="0.25", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")
        elif order['price'] == "1.0011":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='buy', price="0.9992", size="0.25", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")
        elif order['price'] == "1.0013":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='buy', price="0.9989", size="0.4", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")

    elif order['side']== 'buy':
        if order['price'] == "0.9994":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='sell', price="1.0009", size="0.25", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")
        elif order['price'] == "0.9992":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='sell', price="1.0011", size="0.25", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")
        elif order['price'] == "0.9989":
            try:
                auth_client.place_limit_order(product_id='WBTC-BTC', side='sell', price="1.0013", size="0.4", post_only=True)
                delete_order(order)
            except:
                print("Unable to generate new order...will try again...")

    print("[+] Order Generated")

loop = asyncio.get_event_loop()
ws = Ticker(loop, channel, auth=True, key=KEY, secret=SECRET, passphrase=PASSPHRASE)
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(ws.close())
    loop.close()
