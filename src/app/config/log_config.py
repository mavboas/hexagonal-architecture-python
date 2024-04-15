import logging

logging.basicConfig(level=logging.INFO)


def logger(message, level=None):
    if level is None:
        logging.info(message)
    else:
        logging.log(level=level, msg=message)
