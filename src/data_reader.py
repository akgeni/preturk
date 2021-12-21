## read all the files in given data path

import pandas as pd

from gensim.models import FastText
from gensim.utils import simple_preprocess
import numpy as np
import pandas as pd
from pathlib import Path
pd.set_option("display.max_colwidth", 500)

class TextDataReader():
 def __init__(self, data_path, data_field, label_field):
  """
  data_field: Text
  """
  self.data_path = Path(data_path)
  self.data_field = data_field
  self.df = self._read_all_data()
  self.label_field = label_field

  self.label_wightes = self.df[self.label_field].value_counts(normalize=True)

  
  
 def _read_all_data(self):
  """Reads all csv from given path"""
  df = pd.DataFrame()

  for file in self.data_path.glob("*.csv"):
      temp = pd.read_csv(file)
      df = df.append(temp)
      break
  df.dropna(subset=[self.data_field], inplace=True)
  return df
 def print_statistics(self):
   """Print Text  data statistics"""
   print(f"Size of data: {self.df.shape}")
   print(f"\n\n{self.data_field} statistics\n")
   data_len_statistics = self.df[self.data_field].apply(len).describe()
   print()
   print(data_len_statistics)
    
   print("\n\nLabel Statistics\n")
   print(self.label_wightes)
