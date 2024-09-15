# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
print("Verificando os dados do env:")
print(os.getenv('DBUSER'))
print(os.getenv('PASSWORD'))
print(os.getenv('HOST'))
print(os.getenv('PORT'))
print(os.getenv('DATABASE'))


class Config:
    DATABASE_CONFIG = {
        'user': os.getenv('DBUSER'),
        'password': os.getenv('PASSWORD'),
        'host': os.getenv('HOST'),
        'port': os.getenv('PORT'),
        'database': os.getenv('DATABASE'),
    }
