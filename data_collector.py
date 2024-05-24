
from roboflow import Roboflow
import os
from dotenv import load_dotenv

load_dotenv(".env_file")


rf = Roboflow(api_key=os.environ['api_key'])
project = rf.workspace("david-lee-d0rhs").project("american-sign-language-letters")
version = project.version(1)
dataset = version.download("yolov5")

