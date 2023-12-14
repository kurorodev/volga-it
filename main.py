from dataset import temprature as t
from dataset import home_specific as hs
from dataset import temprature_size as ts
from model import model 

def main():
    hs.homeSpecific()
    print("<-------------------------------------------------------->")
    model.compile_and_fit()


if __name__ == "__main__":
    main()