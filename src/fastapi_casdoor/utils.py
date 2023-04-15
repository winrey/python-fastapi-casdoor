from datetime import datetime

from dateutil import parser


def str2datetime(s: str | None) -> datetime | None:
    if not s:
        return None
    return parser.parse(s)
