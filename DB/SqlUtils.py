from DataFaker import DataFaker
import random
import psycopg2
class SqlUtils():
    def __init__(self, faker):
        self.faker = faker

        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="obama")
        self.cur = self.conn.cursor()


    def clean_database(this):
        this.cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = this.cur.fetchall()
        for table in tables:
            this.cur.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE;")
        this.conn.commit()

        with open('dump.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        # Execute the SQL script to create tables
        this.cur.execute(sql_script)

        # Commit the changes to apply the table creations
        this.conn.commit()

    def insert_faker_data(this):
        for i in this.faker.si_sites_data:
            sql = """INSERT INTO si_sites(si_name) VALUES(%s)"""
            this.cur.execute(sql, i)

        for i in this.faker.f_formats_data:
            sql = """INSERT INTO f_formats(f_name)
                     VALUES(%s);"""
            this.cur.execute(sql, i)

        for i in this.faker.s_sessions_data:
            sql = """INSERT INTO s_sessions(s_date, s_length)
                     VALUES(%s, %s);"""
            this.cur.execute(sql, i)

        for i in this.faker.t_tournaments_data:
            sql = """INSERT INTO t_tournaments(t_name, t_buyIn, t_guarantee, t_si_site)
                     VALUES(%s, %s, %s, %s);"""
            this.cur.execute(sql, i)

        for tournament, formats in this.faker.tournament_formats_mapping.items():
            for f_id in formats:
                sql = """INSERT INTO hf_hasFormat(hf_f_id, hf_t_id)
                         VALUES(%s, %s);"""
                this.cur.execute(sql, (f_id, tournament))

        for session, tournaments in this.faker.session_tournaments_mapping.items():
            for t_id in tournaments:
                sql = """INSERT INTO ht_hasTournament(ht_s_id, ht_t_id, ht_winnings, ht_position)
                         VALUES(%s, %s, %s, %s);"""
                this.cur.execute(sql, (session, t_id, random.randint(0, 10000), random.randint(1, 500)))

        for i in this.faker.tr_transactions_data:
            sql = """INSERT INTO tr_transactions(tr_si_id, tr_amount, tr_date)
                     VALUES(%s, %s, %s);"""
            this.cur.execute(sql, i)
        this.conn.commit()


    def find_all(this):
        this.cur.execute("SELECT * FROM s_sessions s JOIN ht_hasTournament ht ON s.s_id = ht.ht_s_id JOIN t_tournaments t ON ht.ht_t_id = t.t_id JOIN hf_hasFormat hf ON t.t_id = hf.hf_t_id JOIN f_formats f ON hf.hf_f_id = f.f_id JOIN si_sites si ON t.t_si_site = si.si_id;")
        return this.cur.fetchall()

    def find_all_by_session_length(this, length):
        this.cur.execute(f"SELECT * FROM s_sessions s JOIN ht_hasTournament ht ON s.s_id = ht.ht_s_id JOIN t_tournaments t ON ht.ht_t_id = t.t_id JOIN hf_hasFormat hf ON t.t_id = hf.hf_t_id JOIN f_formats f ON hf.hf_f_id = f.f_id JOIN si_sites si ON t.t_si_site = si.si_id WHERE s_length = {length};")
        return this.cur.fetchall()

    def find_by_session_length_projection(self, length):
        self.cur.execute(f"SELECT s_date, ht.ht_winnings FROM s_sessions s inner join ht_hasTournament ht on s.s_id = ht.ht_s_id WHERE s_length = {length};")
        return self.cur.fetchall()

    def find_by_session_length_projection_sort(self, length):
        self.cur.execute(f"SELECT s_date, ht.ht_winnings FROM s_sessions s inner join ht_hasTournament ht on s.s_id = ht.ht_s_id WHERE s_length = {length} ORDER BY s_date ASC;")
        return self.cur.fetchall()

    def update_session_length(self):
        self.cur.execute(f"UPDATE s_sessions SET s_length = s_length + 1;")
        self.conn.commit()

    def update_session_length_by_length(self, length):
        self.cur.execute(f"UPDATE s_sessions SET s_length = s_length + 1 WHERE s_length = {length};")
        self.conn.commit()

    def delete_all(self):
        self.cur.execute(f"DELETE FROM hf_hasFormat;")
        self.cur.execute(f"DELETE FROM ht_hasTournament;")
        self.cur.execute(f"DELETE FROM t_tournaments;")
        self.cur.execute(f"DELETE FROM tr_transactions;")
        self.cur.execute(f"DELETE FROM si_sites;")
        self.cur.execute(f"DELETE FROM f_formats;")
        self.cur.execute(f"DELETE FROM s_sessions;")
        self.conn.commit()

    def group_by(self):
        self.cur.execute(f"SELECT t_name, SUM(ht_winnings) FROM t_tournaments t JOIN ht_hasTournament ht ON t.t_id = ht.ht_t_id GROUP BY t_name;")
        return self.cur.fetchall()