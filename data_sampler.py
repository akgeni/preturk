import pandas as pd

from gensim.models import FastText
from gensim.utils import simple_preprocess
import numpy as np
import pandas as pd
from pathlib import Path
pd.set_option("display.max_colwidth", 500)

class TextDataReader():
 def __init__(self, data_path, data_field):
  """
  data_field: Text
  """
  self.data_path = Path(data_path)
  self.data_field = data_field
  self.df = self.read_all_data()
  
  
 def read_all_data(self):
  """Reads all csv from given path"""
  df = pd.DataFrame()

  for file in path.glob("*.csv"):
      temp = pd.read_csv(file)
      concept_df = concept_df.append(temp)
  df.dropna(subset=[self.data_field], inplace=True)
  return df

def print_statistics(self):
  """Print Text  data statistics"""
  print(f"Size of data: {self.df.shape}")
  print(f"{self.data_field} statistics\n")
  data_len_statistics = self.self.df[self.data_field].apply(len).describe()
  print("\t", data_len_statistics)
  


  
    
    
