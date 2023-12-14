from model import *
import pymongo
import random
from DataFaker import DataFaker

class MongoUtils():
    def __init__(self, faker):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["pokerDb"]
        self.mycol = mydb["sessions"]
        self.faker = faker

        self.documents = self.convert_to_mongo_documents()

    def convert_to_mongo_documents(self) -> List[dict]:
        mongo_documents = []
        tournament_instances = []  # List to store tournament instances
        format_instances = []  # List to store format instances
        site_instances = []  # List to store site instances
        # Convert Sites
        for site_data in self.faker.si_sites_data:
            site_instances.append(Site(name=site_data[0]))
            # mongo_documents.append(site_instance)

        # Convert Formats
        for format_data in self.faker.f_formats_data:
            format_instances.append(Format(name=format_data[0]))
            # mongo_documents.append(format_instance)

        # Convert Tournaments
        for tournament_index, format_data in self.faker.tournament_formats_mapping.items():
            #print(tournament_index)
            #print(format_data)
            tournament_data = self.faker.t_tournaments_data[tournament_index-1]
            site_instance = site_instances[tournament_data[3]-1]
            single_format_instances = [
                format_instances[x-1] for x in format_data
            ]

            tournament_instance = Tournament(
                name=tournament_data[0],
                buyin=tournament_data[1],
                guarantee=tournament_data[2],
                site=site_instance,
                formats=single_format_instances
            )
            tournament_instances.append(tournament_instance)  # Add to the list
            # mongo_documents.append(tournament_instance)

        # Convert Sessions
        for session_index, tournament_data in self.faker.session_tournaments_mapping.items():
            session_data = self.faker.s_sessions_data[session_index-1]
            session_date = datetime.combine(session_data[0], datetime.min.time())
            session_instance = Session(
                date=session_date,
                length=session_data[1],
                stats=[tournament_instances[x-1] for x in tournament_data]
            )
            mongo_documents.append(session_instance)
        return mongo_documents

    def insert_documents(self):
        self.mycol.insert_many(self.documents)

    def clean_database(self):
        self.mycol.delete_many({})

    def find_all(self):
        result = list(self.mycol.find({}))
        return result

    def find_by_session_length(self, length):
        result = list(self.mycol.find({"length": length}))
        return result

    def find_by_session_length_projection(self, length):
        return list(self.mycol.find({"length": length},{"_id": 0, "date": 1, "stats.winnings": 1}))

    def find_by_session_length_projection_sort(self, length):
        return list(self.mycol.find({"length": length},{"_id": 0, "date": 1, "stats.winnings": 1}).sort("date", pymongo.DESCENDING))

    def update_session_length(self):
        self.mycol.update_many({}, {"$inc": {"length": 1}})

    def update_session_length_by_length(self, length,):
        self.mycol.update_one({"length": length}, {"$inc": {"length": 1}})

    def delete_all(self):
        self.mycol.delete_many({})

    def aggregate(self):
        return list(self.mycol.aggregate([{"$unwind": "$stats"}, {"$group": {"_id": "$stats.tournament.name", "total": {"$sum": "$stats.winnings"}}}]))


from model import *
import pymongo

faker = DataFaker(5, 10, 10000, 100, 2, 5, 10)

mongoFaker = MongoUtils(faker)

mongoFaker.clean_database()

mongoFaker.insert_documents()