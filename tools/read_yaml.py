import yaml
from config import BasePath
import os

def read_yaml(file_name):
    file = BasePath+os.sep+"datas"+os.sep+file_name
    with open(file,encoding="utf8") as f:
        return yaml.load(f,Loader=yaml.FullLoader)


if __name__ == "__main__":
    file = "../datas/jd.yaml"
    d = read_yaml(file)
    print(d)