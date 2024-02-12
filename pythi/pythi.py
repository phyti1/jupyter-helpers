import os

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
    

