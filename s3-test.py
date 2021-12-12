import os
import pandas as pd
from smart_open import smart_open

from cadence import Cadence

cadence = Cadence()

s3_uri = f"s3://{os.environ['AWS_ACCESS_KEY_ID']}:{os.environ['AWS_SECRET_ACCESS_KEY']}@{os.environ['WEIGHT_HISTORY_URN']}"
#df_in = pd.read_csv_s3(smart_open(s3_uri))
df_in = pd.read_csv('data/Weight History.csv')

#print(df_in['Cadence'])
#df_out = pd.DataFrame(data=df_in['Cadence'], columns=['Notation'])
#print(df_out)

for notation in df_in['Cadence']:
    cadence.clear_notes()
    series_cadence = cadence.get_cadence(notation)
    print(series_cadence, cadence.print_notes())