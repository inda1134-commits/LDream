from datetime import datetime
from dateutil.parser import parse


def parse_date(date_str: str) -> datetime:
    return parse(date_str)
