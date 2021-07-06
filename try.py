import string
import random

import pandas as pd
import openpyxl as oxl

df = pd.read_excel('emailx.xlsx')


xfile = oxl.load_workbook('emailx.xlsx')

sheet = xfile.get_sheet_by_name('Sheet1')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


sheet = xfile.get_sheet_by_name('Sheet1')
sheet['D1'] = 'hello world'


                        


                    
            

        


