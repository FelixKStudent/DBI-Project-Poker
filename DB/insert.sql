--Sites
INSERT INTO si_sites (si_name) VALUES ('GG Poker');
INSERT INTO si_sites (si_name) VALUES ('Poker Stars');
INSERT INTO si_sites (si_name) VALUES ('ACR');

-- Initiate Balance Log

--Format
INSERT INTO f_formats (f_name) VALUES ('Turbo'); --1
INSERT INTO f_formats (f_name) VALUES ('Hyper'); --2
INSERT INTO f_formats (f_name) VALUES ('Bounty'); --3
INSERT INTO f_formats (f_name) VALUES ('Short Deck'); --4
INSERT INTO f_formats (f_name) VALUES ('Deep Stack'); --5
INSERT INTO f_formats (f_name) VALUES ('Satellite');
INSERT INTO f_formats (f_name) VALUES ('Rebuy');
INSERT INTO f_formats (f_name) VALUES ('Add-on');
INSERT INTO f_formats (f_name) VALUES ('Shootout');
INSERT INTO f_formats (f_name) VALUES ('PLO');

--Tournament
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Sunday Million', 215, 1000000, 1);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (9, 1);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Omaholic Bounty', 21.6, 2000, 1);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (3, 2);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Big Stack Bonanza', 55, 50000, 2);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (5, 3);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Sunday Warm-Up', 109, 250000, 1);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (6, 4);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (9, 4);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Friday Night Freeroll', 0, 1000, 2);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (6, 5);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Sunday Hyper', 100, 5000, 1);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (2, 6);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('High Roller Club', 1050, 500000, 2);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (5, 7);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('Deepstack Bounty', 21.6, 2000, 2);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (3, 8);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (5, 8);
INSERT INTO t_tournaments (t_name, t_buyIn, t_guarantee, t_si_site) VALUES ('PLO Bounty', 15, 1000, 1);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (3, 9);
Insert into hf_hasFormat (hf_f_id, hf_t_id) values (10, 9);


-- Create a session and associate it with tournaments
-- Session 1
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-05-29', 'YYYY-MM-DD'), 240);

-- Associate tournaments with Session 1
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (1, 1, 0, 100); -- Tournament 1 in Session 1

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (1, 3, 250, 55); -- Tournament 3 in Session 1

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (1, 5, 1000, 3); -- Tournament 5 in Session 1


-- Session 2
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-05-30', 'YYYY-MM-DD'), 180);

-- Associate tournaments with Session 2
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (2, 2, 120, 78); -- Tournament 2 in Session 2

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (2, 4, 2400, 3); -- Tournament 4 in Session 2


-- Session 3
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-05-31', 'YYYY-MM-DD'), 120);

-- Associate tournaments with Session 3
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (3, 1, 0, 130); -- Tournament 1 in Session 3

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (3, 3, 0, 79); -- Tournament 3 in Session 3

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (3, 5, 300, 3); -- Tournament 5 in Session 3

-- Session 4
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-01', 'YYYY-MM-DD'), 180);

-- Associate tournaments with Session 4
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (4, 7, 0, 20); -- Tournament 1 in Session 4

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (4, 9, 0, 18); -- Tournament 3 in Session 4

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (4, 5, 200, 10); -- Tournament 5 in Session 4

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (4, 6, 0, 30); -- Tournament 6 in Session 4

-- Session 5
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-02', 'YYYY-MM-DD'), 240);

-- Associate tournaments with Session 5
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (5, 2, 0, 15); -- Tournament 2 in Session 5

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (5, 4, 0, 22); -- Tournament 4 in Session 5

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (5, 7, 0, 25); -- Tournament 7 in Session 5


-- Session 6
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-03', 'YYYY-MM-DD'), 120);

-- Associate tournaments with Session 6
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (6, 1, 0, 16); -- Tournament 1 in Session 6

-- Session 7
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-04', 'YYYY-MM-DD'), 150);

-- Associate tournaments with Session 7
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (7, 2, 80, 42); -- Tournament 2 in Session 7

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (7, 3, 0, 95); -- Tournament 3 in Session 7

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (7, 6, 0, 80); -- Tournament 6 in Session 7


-- Session 8
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-05', 'YYYY-MM-DD'), 210);

-- Associate tournaments with Session 8
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (8, 1, 0, 40); -- Tournament 1 in Session 8

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (8, 4, 1800, 2); -- Tournament 4 in Session 8

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (8, 5, 500, 5); -- Tournament 5 in Session 8

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (8, 8, 0, 60); -- Tournament 6 in Session 8


-- Session 9
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-06', 'YYYY-MM-DD'), 180);

-- Associate tournaments with Session 9
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (9, 9, 0, 105); -- Tournament 3 in Session 9

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (9, 8, 400, 7); -- Tournament 5 in Session 9

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (9, 7, 0, 35); -- Tournament 7 in Session 9


-- Session 10
INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-07', 'YYYY-MM-DD'), 240);

-- Associate tournaments with Session 10
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 6, 0, 60); -- Tournament 1 in Session 10

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 2, 100, 30); -- Tournament 2 in Session 10

-- Associate tournaments with Session 10
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 3, 300, 60); -- Tournament 1 in Session 10

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 8, 90, 30); -- Tournament 2 in Session 10

-- Associate tournaments with Session 10
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 4, 0, 60); -- Tournament 1 in Session 10

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 1, 0, 30); -- Tournament 2 in Session 10

-- Associate tournaments with Session 10
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (10, 5, 80, 60); -- Tournament 1 in Session 10

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (9, 4, 220, 30); -- Tournament 2 in Session 10

INSERT INTO s_sessions (s_date, s_length)
VALUES (TO_DATE('2023-06-08', 'YYYY-MM-DD'), 240);

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (11, 8, 0, 30); -- Tournament 2 in Session 10

-- Associate tournaments with Session 10
INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (11, 4, 0, 60); -- Tournament 1 in Session 10

INSERT INTO ht_hasTournament (ht_s_id, ht_t_id, ht_winnings, ht_position)
VALUES (11, 6, 20, 60); -- Tournament 1 in Session 10