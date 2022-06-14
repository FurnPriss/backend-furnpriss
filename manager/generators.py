from datetime import date
import nanoid


def get_default_date():
    return date.today()


def get_default_id():
    return nanoid.generate(size=32)
