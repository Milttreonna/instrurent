import datetime

information=[["acoustic-guitar","10","439.99","57.20" ],
["trumpets","10","2438.99","317.07"],
["clarinets","10","1171.99","152.36"],
["pianos","10","1700.99","221.13"],
["violins","10","699.99","91.00"],
["saxophones","10","3153.99","410.02"],
["electric-guitars","10","899.99","117.00"],
["drums","10","910.00","118.30"],
["banjos","10","439.00","62.27"],
["congas","10","269.99", "35.10"]]
now = datetime.datetime.now()
userInfo_lst = []
date_dict = {}
option_dict = {}
item_dict = {}
week_dict = {}
total_dict = {}
return_dict = {}
revenue_dict = {}


with open("employee.txt", "r") as revenueFile:
    revenue = revenueFile.read()
    revenue = float(revenue[:-1])

with open("emails.txt", "r") as emailFile:
    emails = emailFile.read().split()
with open("inventory.txt", 'r') as inventoryFile:
    inventory = inventoryFile.read().split()
    dict = {inventory[line]: inventory[line + 1]
            for line in range(0, len(inventory), 2)}
    quantity = inventory[1::2]
    instruments = inventory[2::2]
with open("transactions.txt", 'r') as transactionFile:
    trans_file = transactionFile.readlines()
    # transactionhistory = transactionFile.read()
    # transactionline = transactionhistory.splitlines()
with open("clarinet.txt", 'r') as clarinetFile:
    clarinet = clarinetFile.read()
with open("drums.txt", 'r') as drumFile:
    drums = drumFile.read()
with open("piano.txt", 'r') as pianoFile:
    piano = pianoFile.read()
with open("violin.txt", 'r') as violinFile:
    violin = violinFile.read()
with open("eguitar.txt", 'r') as eguitarFile:
    electricguitar = eguitarFile.read()
with open("aguitar.txt", 'r') as aguitarFile:
    acousticguitar = aguitarFile.read()
with open("banjo.txt", 'r') as banjoFile:
    banjo = banjoFile.read()
with open("trumpet.txt", 'r') as trumpetFile:
    trumpet = trumpetFile.read()
with open("sax.txt", 'r') as saxFile:
    sax = saxFile.read()
with open("conga.txt", 'r') as congaFile:
    conga = congaFile.read()
