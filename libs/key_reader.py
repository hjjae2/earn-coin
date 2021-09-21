from config import config


def get_access_key():
    f = open(config.default['access_key_path'], 'r')
    access_key = f.read()
    f.close()

    return access_key.strip()


def get_secret_key():
    f = open(config.default['secret_key_path'], 'r')
    secret_key = f.read()
    f.close()

    return secret_key.strip()
