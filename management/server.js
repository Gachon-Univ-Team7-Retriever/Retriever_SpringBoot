const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();

app.use(express.json());
app.use(express.static(__dirname)); // Serve the HTML and JS files

app.post('/copy-database', async (req, res) => {
    const { sourceDb, targetDb } = req.body;
    const sourceUri = `mongodb://admin:sherlocked@localhost:27017/${sourceDb}?authSource=admin`;
    const targetUri = `mongodb://admin:sherlocked@localhost:27017/${targetDb}?authSource=admin`;

    const sourceClient = new MongoClient(sourceUri);
    const targetClient = new MongoClient(targetUri);

    try {
        await sourceClient.connect();
        await targetClient.connect();

        const sourceDatabase = sourceClient.db(sourceDb);
        const targetDatabase = targetClient.db(targetDb);

        const collections = await sourceDatabase.listCollections().toArray();

        for (const collection of collections) {
            const data = await sourceDatabase.collection(collection.name).find().toArray();

            if (data.length > 0) {
                await targetDatabase.collection(collection.name).insertMany(data);
                console.log(`Collection '${collection.name}' copied successfully.`);
            } else {
                console.log(`Collection '${collection.name}' is empty.`);
            }
        }

        res.json({ message: `All collections from '${sourceDb}' copied to '${targetDb}'.` });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ message: error.message });
    } finally {
        await sourceClient.close();
        await targetClient.close();
    }
});

const PORT = 4000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
