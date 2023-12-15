import random

from DataFaker import DataFaker

from typing import List
from datetime import datetime
import pymongo
from faker import Faker
from modelRef import Site, Format, Tournament, Session, SessionStats
from bson.dbref import DBRef


class MongoUtilsRef:
    def __init__(self, faker: Faker):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myclient["pokerDb"]
        self.mycol_sessions = self.mydb["sessionsRef"]
        self.faker = faker

    def convert_to_mongo_documents(self):
        mongo_documents = []
        tournament_instances = []  # List to store tournament instances
        format_instances = []  # List to store format instances
        site_instances = []  # List to store site instances
        # Convert Sites
        site_documents = [{'name': site_data[0]} for site_data in self.faker.si_sites_data]
        result = self.mydb["sitesRef"].insert_many(site_documents)
        site_instances = result.inserted_ids

        # Convert Formats
        format_documents = [{'name': format_data[0]} for format_data in self.faker.f_formats_data]
        result = self.mydb["formatsRef"].insert_many(format_documents)
        format_instances = result.inserted_ids

        # Convert Tournaments
        tournament_documents = []
        for tournament_index, format_data in self.faker.tournament_formats_mapping.items():
            tournament_data = self.faker.t_tournaments_data[tournament_index - 1]
            site_instance = site_instances[tournament_data[3] - 1]
            single_format_instances = [format_instances[x - 1] for x in format_data]

            tournament_documents.append({
                'name': tournament_data[0],
                'buyin': tournament_data[1],
                'guarantee': tournament_data[2],
                'site': DBRef(collection='sitesRef', id=site_instance),
                'formats': single_format_instances
            })

        result = self.mydb["tournamentsRef"].insert_many(tournament_documents)
        tournament_instances = result.inserted_ids

        sessions = []
        for session in self.faker.s_sessions_data:
            session_date = datetime.combine(session[0], datetime.min.time())
            session_instance = Session(date=session_date, length=session[1])
            sessions.append(session_instance)

        result = self.mydb["sessionsRef"].insert_many(sessions)
        session_instances = result.inserted_ids

        session_stats_documents = []
        for session_index, tournament_data in self.faker.session_tournaments_mapping.items():
            session_data = self.faker.s_sessions_data[session_index - 1]
            for x in tournament_data:
                tournament_instance = tournament_instances[x - 1]
                session_instance = session_instances[session_index - 1]

                session_stats_documents.append({
                    'winnings': random.randint(0, 1000),
                    'position': random.randint(0, 1000),
                    'session': DBRef(collection='sessionsRef', id=session_instance),
                    'tournament': DBRef(collection='tournamentsRef', id=tournament_instance)
                })

        self.mydb["sessionStatsRef"].insert_many(session_stats_documents)

    def insert_documents(self):
        self.convert_to_mongo_documents()

    def clean_database(self):
        self.mydb["sessionStatsRef"].delete_many({})
        self.mydb["sessionsRef"].delete_many({})
        self.mydb["tournamentsRef"].delete_many({})
        self.mydb["formatsRef"].delete_many({})
        self.mydb["sitesRef"].delete_many({})

    def find_all(self):
        pipeline = [
            {"$lookup": {
                "from": "tournamentsRef",  # Replace with the actual name of the tournaments collection
                "localField": "stats.tournament.$id",
                "foreignField": "_id",
                "as": "tournament"
            }},
            {"$lookup": {
                "from": "sessionsRef",  # Replace with the actual name of the sessions collection
                "localField": "stats.session.$id",
                "foreignField": "_id",
                "as": "session"
            }},
            {"$project": {"_id": 0, "date": 1, "length": 1, "stats.winnings": 1, "tournament.name": 1, "session.length": 1}}
        ]

        result = list(self.mycol_sessions.aggregate(pipeline))
        return result

    def find_by_session_length(self, length):
        pipeline = [
            {"$match": {"length": length}},
            {"$lookup": {
                "from": "tournamentsRef",  # Replace with the actual name of the tournaments collection
                "localField": "stats.tournament.$id",
                "foreignField": "_id",
                "as": "tournament"
            }},
            {"$lookup": {
                "from": "sessionsRef",  # Replace with the actual name of the sessions collection
                "localField": "stats.session.$id",
                "foreignField": "_id",
                "as": "session"
            }},
            {"$project": {"_id": 0, "date": 1, "length": 1, "stats.winnings": 1, "tournament.name": 1, "session.length": 1}}
        ]

        result = list(self.mycol_sessions.aggregate(pipeline))
        return result

    def update_session_length(self):
        self.mycol_sessions.update_many({}, {"$inc": {"length": 1}})

    def update_session_length_by_length(self, length,):
        self.mycol.update_one({"length": length}, {"$inc": {"length": 1}})
