import os
import sys

def unify_cwd(root_identifier = ".git"):
  """
  cd into the project root folder

  Argments:
  - root_identifier: str folder or file path in the root directory used for identification

  Returns:
  - None
  """
  cwd = os.getcwd()

  while(not os.path.exists(os.path.join(cwd, root_identifier))):
    if(cwd == os.path.dirname(cwd)):
      raise Exception(f"Could not find project root containing <{root_identifier}>.")

    cwd = os.path.dirname(cwd)
  
  # change cwd to this directory
  os.chdir(cwd)

def get_df_size(df):
  """
  Print the size of a pandas DataFrame in memory
  
  Arguments:
  - df: pd.DataFrame

  Returns:
  - None
  """

  print(f"{sys.getsizeof(df)/1024/1024/1024:.1f} GB")
  # df Grösse nach Spalte
  for column in df.columns:
      print(f"{column}: {sys.getsizeof(df[[column]])/1024/1024:.1f} MB")
    

