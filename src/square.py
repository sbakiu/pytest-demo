import logging
logging.basicConfig(level=logging.INFO)


def square(x):
    logging.info(f"Received input x: {x}.")
    sq = x*x
    logging.info(f"Returning square: {sq}.")
    return sq
