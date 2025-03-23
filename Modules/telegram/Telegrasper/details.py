import os
from dotenv import load_dotenv

load_dotenv()

apiID = os.environ["TELEGRAM_API_ID"]
apiHash = os.environ["TELEGRAM_API_HASH"]
number = os.environ["PHONE_NUMBER"]
