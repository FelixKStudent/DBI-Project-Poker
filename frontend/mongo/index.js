const express = require('express');
const path = require('path');
const ejs = require('ejs');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
const port = 3000;

// Connect to MongoDB
const mongoUrl = 'mongodb://root:mypass@localhost:27017/';
const dbName = 'pokerDb';

let client;

async function connectToDatabase() {
    if (!client) {
        client = new MongoClient(mongoUrl, { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();
    }

    return client.db(dbName);
}

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'public')));

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.get('/', async (req, res) => {
    try {
        const db = await connectToDatabase();
        const sessionsCollection = db.collection('sessions');
        const sessions = await sessionsCollection.find({}).toArray();
        console.log(sessions);
        res.render('sessions', { sessions });
    } catch (error) {
        console.error('Error fetching session dates:', error);
        res.status(500).send('Internal Server Error');
    }
}); 

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
