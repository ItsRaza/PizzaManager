import json


def makeJson(info):
    with open("info.json", 'w') as f:
        json.dump(info, f)


def retriveJson():
    with open("record.json") as f:
        info = json.load(f)
    print(info)


info = {}

if __name__ == "__main__":
    ch = 'y'
    while ch != 'q':
        size = input("Enter Size:")
        price = input("Enter Price:")
        info.update({size: price})
        ch = input("Press 'q' to quit and any other key to continue..")

    print(info)
    makeJson(info)
