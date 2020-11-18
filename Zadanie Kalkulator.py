import logging

def count(a, b):


if __name__ == "__main__":
    action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    if action > 5:
        exit(1)
    a = input("Podaj składnik 1:")
    b = input("Podaj składnik 2:")
    if action == 1:
        logging.info("Dodaję %s i %s" % (a, b))
    elif action == 2:
        logging.info("Odejmuję %s od %s" % (b, a))
    elif action == 3:
        logging.info("Mnożę %s przez %s" % (a, b))
    elif action == 4:
        logging.info("Dzielę %s przez %s" % (a, b))
    else:
        logging.info("Podano błędną liczbę")
        exit(1)
    count(a, b)