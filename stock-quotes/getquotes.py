import stockquotes
import pymongo
import os

class GetQuotes:
    def __init__(self):
        self.mongo = pymongo.MongoClient(
                           host=os.environ['MHOST'],
                           port=int(os.environ['MPORT']),
                           username=os.environ['MUSER'],
                           password=os.environ['MPASS'],
                           authSource="admin") 
        self.db = self.mongo[os.environ['MDB']]
        self.symbols = self._get_symbols_list()

    def _add_base_object(self,symbol):
        collection = self.db['quotes']
        doc = {'symbol':symbol,'quotes':[]}
        collection.insert_one(doc)

    def _symbol_in_quotes_collection(self,symbol):
        collection = self.db['quotes']
        result = [ s['symbol'] for s in list(collection.find({"symbol":symbol},{"_id":0,"symbol":1})) ]
        return len(result) > 0

    def _get_symbols_list(self):
        collection = self.db['symbols']
        return [ s['symbol'] for s in list(collection.find({},{"_id":0,"symbol":1})) ]

    def __call__(self):
        collection = self.db['quotes']
        for symbol in self.symbols:
            print(symbol)
            if not self._symbol_in_quotes_collection(symbol):
                self._add_base_object(symbol)

            for quote in stockquotes.Stock(symbol).historical:
                collection.update( {"symbol":symbol}, {"$addToSet": {"quotes": quote }} )
            


if __name__ == '__main__':
    GetQuotes()()

