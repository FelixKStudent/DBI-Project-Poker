from typing import TypedDict
from datetime import datetime
from typing import List

class Site(TypedDict):
    name: str

class Format(TypedDict):
    name: str

class Tournament(TypedDict):
    name: str
    buyin: int
    guarantee: int
    site: Site
    formats: List[Format]

class Session(TypedDict):
    date: datetime
    length: int

class SessionStats(TypedDict):
    winnings: int
    position: int

    session: Session
    tournament: Tournament