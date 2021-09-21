import datetime


def info(message):
    print("{} [INFO] {}".format(datetime.datetime.now(), message))


def log(message):
    print("{} [LOG] {}".format(datetime.datetime.now(), message))


def error(message):
    print("{} [ERROR] {}".format(datetime.datetime.now(), message))
