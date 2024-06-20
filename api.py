import requests


def get_gadgets():
    response = requests.get("https://www.jumia.com.ng/computing/")
    # with open("index.html", "w") as f:
    #     f.write(response.text)
    return response.text


if __name__ == "__main__":
    print(get_gadgets())
