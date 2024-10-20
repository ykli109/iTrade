from sqlalchemy import BIGINT, DATE, FLOAT, SmallInteger
from sqlalchemy.dialects.mysql import BIT


def get_field_type_name(col_type):
    if col_type == DATE:
        return "datetime"
    elif col_type == FLOAT or col_type == BIGINT or col_type == SmallInteger or col_type == BIT:
        return "numeric"
    else:
        return "string"
