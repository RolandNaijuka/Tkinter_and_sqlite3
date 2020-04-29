from tkinter import *
import requests
import json


pycrypto = Tk()
pycrypto.title("My Crypto Portifolio")
pycrypto.iconbitmap('favicon.png')


def my_portfolio():


    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=330bb561-9e22-45c0-8f8e-9a00c2aab64f")
    api = json.loads(api_request.content)

    coins =[
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":7767.42
        },
        {
            "symbol":"XRP",
            "amount_owned":100,
            "price_per_coin":0.20
        },
        {
            "symbol":"ETH",
            "amount_owned":5,
            "price_per_coin":208.27
        },
        {
            "symbol":"EOS",
            "amount_owned":100,
            "price_per_coin":2.87
        },
        {
            "symbol":"XLM",
            "amount_owned":10000,
            "price_per_coin":0.07
        },
        {
            "symbol":"LEO",
            "amount_owned":1000,
            "price_per_coin":1.05
        },
        {
            "symbol":"TRX",
            "amount_owned":50000,
            "price_per_coin":0.0156
        }
    ]


    total_pl = 0
    coin_row = 1
    for i in range(300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"]*coin["price_per_coin"]
                current_value = coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_per_coin*coin["amount_owned"]

                total_pl = total_pl + pl_per_coin



                name =  Label(pycrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=0,sticky=N+S+E+W)

                name =  Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=1,sticky=N+S+E+W)

                name =  Label(pycrypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=2,sticky=N+S+E+W)

                name =  Label(pycrypto, text="${0:.2f}".format(total_paid), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=3,sticky=N+S+E+W)

                name =  Label(pycrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=4,sticky=N+S+E+W)

                name =  Label(pycrypto, text="${0:.2f}".format(pl_per_coin), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=5,sticky=N+S+E+W)

                name =  Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=6,sticky=N+S+E+W)

                coin_row = coin_row+1



name =  Label(pycrypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=0,sticky=N+S+E+W)

name =  Label(pycrypto, text="price", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=1,sticky=N+S+E+W)

name =  Label(pycrypto, text="Coin Owned", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=2,sticky=N+S+E+W)

name =  Label(pycrypto, text="Total Amout paid", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=3,sticky=N+S+E+W)

name =  Label(pycrypto, text="Current Value", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=4,sticky=N+S+E+W)

name =  Label(pycrypto, text="P/L Per Coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=5,sticky=N+S+E+W)

name =  Label(pycrypto, text="Total P/L with Coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
name.grid(row=0, column=6,sticky=N+S+E+W)


my_portfolio()

pycrypto.mainloop()

print("Program completed")