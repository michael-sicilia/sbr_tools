

class MetricScrub: 

    def __init__(self, _json_list): 
        self._json_list = _json_list
        self.input_columns = self.getColumns()
        
    
    def getColumns(self): 
        inp_cols = []
        for _dict in self._json_list:
            cols = list(_dict['data'].columns)
            inp_cols\
                .extend([col for col in cols 
                         if col not in inp_cols])
        return inp_cols

    def standardizeColumnNames(self): 

        assert self.input_columns is not None
        column_map = {}

        for col in self.input_columns:
            column_map[col] = col.strip()\
                                 .lower()\
                                 .translate(str.maketrans(colCharMap()))
        
        return column_map


def colCharMap(): 

    _dict = {
        ' ' : '_',
        '%' : '_pct',
        '-' : '_',
        '+' : '_plus',
        '/' : '_'
    }

    return _dict