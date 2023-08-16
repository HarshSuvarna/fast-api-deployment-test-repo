import os
from dotenv import load_dotenv

load_dotenv()

print('env_var:', os.environ.get('SECRET'))