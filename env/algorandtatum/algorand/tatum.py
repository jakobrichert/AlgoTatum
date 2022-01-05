import http.client
import json
import environ
from pathlib import Path
env = environ.Env()
environ.Env.read_env()



def createaccount():
    conn = http.client.HTTPSConnection("api-eu1.tatum.io")
    
    payload = "{\"currency\":\"ALGO\",\"xpub\":\"xpub6EsCk1uU6cJzqvP9CdsTiJwT2rF748YkPnhv5Qo8q44DG7nn2vbyt48YRsNSUYS44jFCW9gwvD9kLQu9AuqXpTpM1c5hgg9PsuBLdeNncid\",\"customer\":{\"accountingCurrency\":\"USD\",\"customerCountry\":\"US\",\"externalId\":\"123654\",\"providerCountry\":\"US\"},\"compliant\":false,\"accountCode\":\"AC_1011_B\",\"accountingCurrency\":\"USD\",\"accountNumber\":\"123456\"}"

    headers = {
        'content-type': "application/json",
        'x-api-key': "Your API KEY"
        }

    conn.request("POST", "/v3/ledger/account", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generatewallet():
    conn = http.client.HTTPSConnection("api-eu1.tatum.io")

    headers = { 'x-api-key': "Your API KEY" }

    conn.request("GET", "/v3/algorand/wallet?mnemonic=", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data.decode("utf-8")

    return json.loads(data)

def getifps():
    conn = http.client.HTTPSConnection("api-eu1.tatum.io")

    headers = { 'x-api-key': "Your API KEY" }

    conn.request("GET", "/v3/ipfs/{id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

