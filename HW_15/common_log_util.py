import logging

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='hw_15.txt', filemode='w', format=FORMAT, style='{', level=logging.NOTSET)
common_log = logging.getLogger()

if __name__ == '__main__':
    print("Not for separate use")