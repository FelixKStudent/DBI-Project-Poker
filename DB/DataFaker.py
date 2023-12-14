from datetime import datetime, timedelta
from faker import Faker
import random

class DataFaker():
    def __init__(self, numsSites, numFormats, numSessions, numTournaments, formatsPerTournament, tournamentsPerSession, numTransactions):
        self.fake = Faker()

        self.numSites = numsSites
        self.numFormats = numFormats
        self.numSessions = numSessions
        self.numTournaments = numTournaments
        self.formatsPerTournament = formatsPerTournament
        self.tournamentsPerSession = tournamentsPerSession
        self.numTransactions = numTransactions

        self.si_sites_data = [(self.fake.word(),) for _ in range(self.numSites)]
        self.f_formats_data = [(self.fake.word(),) for _ in range(self.numFormats)]

        current_date = datetime.now().date()
        self.s_sessions_data = [(date, random.randint(1, 5)) for date in self.generate_unique_dates(current_date, self.numSessions)]

        self.t_tournaments_data = [
            (self.fake.word(), random.randint(1, 100), random.randint(0, 10000), random.randint(1, self.numSites))
            for _ in range(self.numTournaments)
        ]

        formats_shuffled = random.sample(range(1, self.numFormats + 1), self.numFormats)

        self.tournament_formats_mapping = {
            x + 1: self.generate_random_number_of_items(formats_shuffled, self.formatsPerTournament)
            for x in range(self.numTournaments)
        }

        tournaments_shuffled = random.sample(range(1, self.numTournaments + 1), self.numTournaments)
        self.session_tournaments_mapping = {
            x + 1: self.generate_random_number_of_items(tournaments_shuffled, self.tournamentsPerSession)
            for x in range(self.numSessions)
        }

        self.tr_transactions_data = [
            (random.randint(1, self.numSites), random.randint(-1000, 1000), date)
            for date in self.generate_unique_dates(current_date, self.numTransactions)
        ]

    def generate_unique_dates(self, end_date, num_dates):
        date_set = set()
        dates = []
        while len(dates) < num_dates:
            current_date = self.fake.date_between_dates(datetime.now().date() - timedelta(days=30 * 365), end_date)
            if current_date not in date_set:
                date_set.add(current_date)
                dates.append(current_date)
        return dates

    def generate_random_number_of_items(self, items, max_count):
        count = random.randint(1, max_count)
        return random.sample(items, min(count, len(items)))


