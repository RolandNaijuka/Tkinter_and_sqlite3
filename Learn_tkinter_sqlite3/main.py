from tkinter import *
import requests, json, sqlite3


pycrypto = Tk()
pycrypto.title("My Crypto Portifolio")
pycrypto.iconbitmap('favicon.ico')

con = sqlite3.connect('coin.db')
cursorObj = con.cursor()

#create table if it does not exists
cursorObj.execute("CREATE TABLE IF NOT EXISTS coin(\
    id INTEGER PRIMARY KEY,\
        symbol TEXT, amount INTEGER, price REAL)")
con.commit()

#insert in our table for the database
def insert_coin(id, symbol,amount,price):
    cursorObj.execute("INSERT OR REPLACE INTO coin VALUES(?,?,?,?)",(id,symbol,amount,price))
    con.commit()

def fetch_all():
    cursorObj.execute("SELECT * FROM coin")
    return cursorObj.fetchall()


#portfolio for the app
def my_portfolio():
    
    def font_color(amount):
        return "green" if amount>=0 else "red"

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=330bb561-9e22-45c0-8f8e-9a00c2aab64f")
    api = json.loads(api_request.content)

    coins = fetch_all()

    #print(coins)

    total_pl = 0
    coin_row = 1
    total_current_value = 0
    total_amount_paid = 0


    for i in range(300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin[1]:
                total_paid = coin[2]*coin[3]
                current_value = coin[2]*api["data"][i]["quote"]["USD"]["price"]
                pl_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin[3]
                total_pl_coin = pl_per_coin*coin[2]

                total_pl += total_pl_coin
                total_current_value += current_value

                total_amount_paid+=total_paid


                portfolio_id =  Label(pycrypto, text=coin[0], bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                portfolio_id.grid(row=coin_row, column=0,sticky=N+S+E+W)

                name =  Label(pycrypto, text=api["data"][i]["symbol"], bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                name.grid(row=coin_row, column=1,sticky=N+S+E+W)

                price =  Label(pycrypto, text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                price.grid(row=coin_row, column=2,sticky=N+S+E+W)

                no_coins =  Label(pycrypto, text=coin[2], bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                no_coins.grid(row=coin_row, column=3,sticky=N+S+E+W)

                amount_paid =  Label(pycrypto, text="${0:.2f}".format(total_paid), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                amount_paid.grid(row=coin_row, column=4,sticky=N+S+E+W)

                current_val =  Label(pycrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                current_val.grid(row=coin_row, column=5,sticky=N+S+E+W)

                pl_coin =  Label(pycrypto, text="${0:.2f}".format(pl_per_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(pl_per_coin))), font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                pl_coin.grid(row=coin_row, column=6,sticky=N+S+E+W)

                totalpl =  Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
                totalpl.grid(row=coin_row, column=7,sticky=N+S+E+W)

                coin_row += 1
    totalap =  Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
    totalap.grid(row=coin_row, column=4,sticky=N+S+E+W)

    totalcv =  Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
    totalcv.grid(row=coin_row, column=5,sticky=N+S+E+W)
    
    totalpl =  Label(pycrypto, text="${0:.2f}".format(total_pl), bg="#F3F4F6", fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
    totalpl.grid(row=coin_row, column=7,sticky=N+S+E+W)

    del api
    refresh_button =  Button(pycrypto, command=my_portfolio, text="Refresh", bg="#F3F4F6", fg="black", font="Lato 12", padx="2",pady="2",borderwidth=2,relief="groove")
    refresh_button.grid(row=coin_row+1, column=7,sticky=N+S+E+W)



def app_header():
    portfolio_id =  Label(pycrypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    portfolio_id.grid(row=0, column=0,sticky=N+S+E+W)

    name =  Label(pycrypto, text="Coin Name", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=1,sticky=N+S+E+W)

    name =  Label(pycrypto, text="price", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=2,sticky=N+S+E+W)

    name =  Label(pycrypto, text="Coin Owned", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=3,sticky=N+S+E+W)

    name =  Label(pycrypto, text="Total Amout paid", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=4,sticky=N+S+E+W)

    name =  Label(pycrypto, text="Current Value", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=5,sticky=N+S+E+W)

    name =  Label(pycrypto, text="P/L Per Coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=6,sticky=N+S+E+W)

    name =  Label(pycrypto, text="Total P/L with Coin", bg="#142E54", fg="white", font="Lato 12 bold", padx="5",pady="5",borderwidth=2,relief="groove")
    name.grid(row=0, column=7,sticky=N+S+E+W)

app_header()
my_portfolio()

pycrypto.mainloop()
cursorObj.close()
con.close()
#To execute, run this in the terminal
#pyinstaller main.py --onefile --noconsole --icon=favicon.ico