const express = require('express');
const path = require('path');
const ejs = require('ejs');
const { Pool } = require('pg');

const app = express();
const port = 3000;

// Set up PostgreSQL connection pool
const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'postgres',
    password: 'obama',
    port: 5432,
});

// Set the views directory and view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Middleware to parse JSON and urlencoded data
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Define route to render sessions page
app.get('/', async (req, res) => {
    try {
        // Fetch distinct session dates from the database
        const result = await pool.query('SELECT s_id, s_date FROM s_sessions ORDER BY s_date');
        const sessions = result.rows;
        
        // Render the sessions page with the session dates
        res.render('sessions', { sessions });
    } catch (error) {
        console.error('Error fetching session dates:', error);
        res.status(500).send('Internal Server Error');
    }
});

app.post('/tournaments', async (req, res) => {
    const selectedId = req.body.selectedId;

    try {
        // TODO: Revamp!
        const date = (await pool.query('SELECT s_date FROM s_sessions WHERE s_id = $1', [selectedId])).rows.pop().s_date;
        
        // Fetch tournaments for the selected session from the database
        const result = await pool.query(
            'SELECT t.t_name, ht.ht_position, ht.ht_winnings FROM t_tournaments t ' +
            'JOIN ht_hasTournament ht ON t.t_id = ht.ht_t_id ' +
            'WHERE ht.ht_s_id = $1',
            [selectedId]
        );

        const tournaments = result.rows;

        // Render the tournaments list with the selected session
        res.render('tournamentsList', { tournaments, selectedId, date });
    } catch (error) {
        console.error('Error fetching tournaments:', error);
        res.status(500).send('Internal Server Error');
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
