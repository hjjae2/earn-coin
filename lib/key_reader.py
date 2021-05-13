import os


class KeyReader:
    def __init__(self) -> None:
        super().__init__()
        self.__access_key_path = os.path.abspath(os.curdir) + '/access.key'
        self.__secret_key_path = os.path.abspath(os.curdir) + '/secret.key'

    def get_access_key(self):
        f = open(self.__access_key_path, 'r')
        access_key = f.read()
        f.close()

        return access_key.strip()

    def get_secret_key(self):
        f = open(self.__secret_key_path, 'r')
        secret_key = f.read()
        f.close()

        return secret_key.strip()
