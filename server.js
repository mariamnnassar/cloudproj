import express from 'express';
import cors from 'cors';
import admin from 'firebase-admin';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';
dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const serviceAccount = JSON.parse(process.env.GOOGLE_CREDENTIALS_JSON);

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

const app = express();
const port = process.env.PORT || 3000;

// Serve static files (like index.html)
app.use(express.static(path.join(__dirname, 'public')));

app.use(cors());

app.get('/api/transactions', async (req, res) => {
  try {
    const transactionsRef = db.collection('transactions');
    const snapshot = await transactionsRef.orderBy('timestamp', 'desc').get();

    const transactions = [];
    snapshot.forEach(doc => {
      const data = doc.data();
      if (data.timestamp && data.timestamp.toDate) {
        data.timestamp = data.timestamp.toDate().toISOString();
      }
      transactions.push(data);
    });

    res.json(transactions);
  } catch (error) {
    console.error('Error fetching transactions:', error);  // سجل الخطأ هنا
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on http://localhost:${port}`);
});
