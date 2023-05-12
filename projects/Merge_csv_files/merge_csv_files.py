import glob
import pandas as pd

extension = 'csv'
all_filenames = list(glob.glob(f'*.{extension}'))

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
