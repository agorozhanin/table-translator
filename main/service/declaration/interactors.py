import datetime

from main.models import Declaration
from main.service.currency.use_cases import convert_dollars_to_roubles


def insert_declaration(order_num, price_in_dollars, delivery_time, course) -> None:
    price_in_roubles = convert_dollars_to_roubles(value_in_dollars=price_in_dollars, course_roubles_to_dollars=course)
    delivery_datetime = datetime.datetime.strptime(delivery_time, '%d.%m.%Y').date().strftime('%Y-%m-%d')
    Declaration.objects.create(order_num=order_num, price_in_dollars=price_in_dollars,
                               price_in_roubles=price_in_roubles,
                               delivery_time=delivery_datetime)
