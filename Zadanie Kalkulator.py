import logging

logging.basicConfig(level=logging.INFO)


def calculate(a, b, action):
    if action == 1:
        logging.info("Dodaję %s i %s" % (first_number, second_number))
        return a + b,
    elif action == 2:
        logging.info("Odejmuję %s od %s" % (second_number, first_number))
        return a - b
    elif action == 3:
        logging.info("Mnożę %s przez %s" % (first_number, second_number))
        return a * b
    elif action == 4:
        logging.info("Dzielę %s przez %s" % (first_number, second_number))
        return a / b
    else:
        return ValueError



if __name__ == "__main__":
    action = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
    first_number = int(input("Podaj składnik 1:"))
    second_number = int(input("Podaj składnik 2:"))
    print(calculate(first_number, second_number, action))
