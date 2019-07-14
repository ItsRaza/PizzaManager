import json

info = {}


def makeJson(info):
    with open("info.json", 'w') as f:
        json.dump(info, f)


def retriveJson(file):
    with open(file) as f:
        info_l = json.load(f)
    print(info_l)
    return info_l


if __name__ == "__main__":
    try:
        file = input("Enter name of file:")
        info = retriveJson(file)
    except FileNotFoundError:
        print("No such file exist..")

    upch = input("Press 'u' to update your file:")
    if upch == 'u':
        ch = 'y'
        while ch != 'q':
            size = input("Enter Size:")
            price = input("Enter Price:")
            info.update({size: price})
            ch = input("Press 'q' to quit and any other key to continue..")

        makeJson(info)
    else:
        print(info)
