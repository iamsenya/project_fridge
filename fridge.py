import datetime
from decimal import Decimal

goods = {}

date_format = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, '%Y-%m-%d').date()

    if title in items:
        items[title].append(
            {'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    value = note.split()
    values = value[-1].split('-')
    serator = ' '
    if '-' in value[-1]:
        expiration_date = value[-1]
        amount = Decimal(value[-2])
    else:
        expiration_date = None
        amount = Decimal(value[-1])
    if expiration_date == None:
        title = serator.join(value[:-1])
    else:
        title = serator.join(value[:-2])
    add(items, title, amount, expiration_date)


def find(items, needle):
    ret_value = []
    for keys in items:
        if needle.lower() in str.lower(keys):
            list.append(ret_value, keys)
    return ret_value


def amount(items, needle):
    result = 0
    name_products = find(items, needle)
    for name in name_products:
        one_product = items[name]
        for product in one_product:
            result += product['amount']
    return Decimal(result)


def expire(items, in_advance_days=0):
    expire = []
    today = datetime.date.today()
    date_of_delay = today + datetime.timedelta(days=in_advance_days)
    for product in items:
        amount = Decimal('0')
        for ware in items[product]:
            if ware['expiration_date'] != None:
                if date_of_delay <= ware['expiration_date']:
                    amount += ware['amount']
                    result = product, amount
        if amount > Decimal('0'):
            list.append(expire, result)
    return expire
