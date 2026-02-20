import json
import polars as pl
from io import StringIO

# User should isolate all data before passing into transform
def IsolateFromJSON(json_path, to_find):
    with open(json_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)
        assert type(cfg) == list, to_find is not None
        to_return = cfg[0] 
        if len(cfg) > 1:
            _expr = iter([d for d in cfg\
                            if all(d.get(k) == v for k, v in to_find.items())
                        ])
            to_return = next(_expr, to_return)['data']
        to_return = pl.read_json(StringIO(to_return['data']))
        return to_return 

class DataSet:
    
    def __init__(self, input): 
        self.input = input
        
