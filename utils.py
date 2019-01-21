import os

DATA_DIR = os.path.join(os.getcwd(), 'data')


def get_data(filename):
    return open(os.path.join(DATA_DIR, filename), 'r')
