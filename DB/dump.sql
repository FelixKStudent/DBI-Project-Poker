    DROP TABLE IF EXISTS s_sessions CASCADE;
    DROP TABLE IF EXISTS f_formats CASCADE;
    DROP TABLE IF EXISTS t_tournaments CASCADE;
    DROP TABLE IF EXISTS hf_hasFormat CASCADE;
    DROP TABLE IF EXISTS ht_hasTournament CASCADE;
    DROP TABLE IF EXISTS si_sites CASCADE;
    DROP TABLE IF EXISTS tr_transactions CASCADE;
    DROP TABLE IF EXISTS b_balanceLog CASCADE;

    CREATE TABLE s_sessions
    (
      s_id SERIAL PRIMARY KEY,
      s_date DATE,
      s_length INTEGER
    );

    CREATE TABLE si_sites
    (
        si_id SERIAL PRIMARY KEY,
        si_name VARCHAR(50)
    );

    CREATE TABLE f_formats
    (
        f_id SERIAL PRIMARY KEY,
        f_name VARCHAR(100)
    );

    CREATE TABLE t_tournaments
    (
        t_id SERIAL PRIMARY KEY,
        t_name VARCHAR(50),
        t_buyIn INTEGER NOT NULL,
        t_guarantee INTEGER,
        t_si_site INTEGER NOT NULL REFERENCES si_sites(si_id)
    );

    CREATE TABLE hf_hasFormat
    (
      hf_f_id INTEGER NOT NULL,
      hf_t_id INTEGER NOT NULL,
      PRIMARY KEY (hf_f_id, hf_t_id),
      FOREIGN KEY (hf_f_id) REFERENCES f_formats (f_id),
      FOREIGN KEY (hf_t_id) REFERENCES t_tournaments (t_id)
    );

    CREATE TABLE ht_hasTournament
    (
        ht_s_id INTEGER NOT NULL,
        ht_t_id INTEGER NOT NULL,
        ht_winnings INTEGER NOT NULL,
        ht_position INTEGER NOT NULL,
        PRIMARY KEY (ht_s_id, ht_t_id),
        FOREIGN KEY (ht_s_id) REFERENCES s_sessions (s_id),
        FOREIGN KEY (ht_t_id) REFERENCES t_tournaments (t_id)
    );

    CREATE TABLE tr_transactions
    (
        tr_id SERIAL PRIMARY KEY,
        tr_si_id INTEGER NOT NULL REFERENCES si_sites(si_id),
        tr_amount INTEGER NOT NULL,
        tr_date DATE NOT NULL
    );
