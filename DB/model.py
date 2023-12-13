from typing import TypedDict, NotRequired
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

class Site(TypedDict):
    name: str

class Transaction(TypedDict):
    amount: int
    date: datetime
    site: Site

class Format(TypedDict):
    name: str

class Tournament(TypedDict):
    name: str
    buyin: int
    guarantee: int
    site: Site
    formats: list[Format]

class SessionStats(TypedDict):
    winnings: int
    position: int
    tournaments: Tournament

class Session(TypedDict):
    date: datetime
    length: int
    stats: list[SessionStats] # Makes Session : Tournament technically 1 : N and cause duplication of tournaments and problems on update if not all occurences are changed accordingly. Referencing is inherently required for n:m to work but this is the frontend optimized version - so frontend optimal at all cost!