from main.models import Declaration
from main.service.currency.interactors import get_course_roubles_to_dollars
from main.service.declaration.interactors import insert_declaration


def insert_declaration_to_table(table_as_list: list) -> None:
    table_as_list.remove(table_as_list[0])
    course = get_course_roubles_to_dollars()
    Declaration.objects.all().delete()
    for row in table_as_list:
        insert_declaration(order_num=row[1], price_in_dollars=row[2], delivery_time=row[3], course=course)

