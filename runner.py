import random
import string

import requests

session = requests.session()


def get(url):
    return session.get(url)


def post(url, params=None, data=None):
    return session.post(url, params=params, data=data)


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class Rizon:
    def __init__(self) -> None:
        self.baseDomaine = "qchat.rizon.net"

    def t0(self) -> requests.models.Response:
        id = id_generator(32)
        params = (
            ("r", id),
            ("t", "0"),
        )

        data = {"nick": "testname", "authtype": "None", "authvalue": ""}

        response = post(f"https://{self.baseDomaine}/e/n", params=params, data=data)
        return response


def main():
    test = Rizon()
    print(test.t0().json())


if __name__ == "__main__":
    main()
