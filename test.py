from dotenv import load_dotenv
import os
load_dotenv(".env_file")

print(os.environ['api_key'])