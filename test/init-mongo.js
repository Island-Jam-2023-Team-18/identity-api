db = db.getSiblingDB('SCORES');

db.HIGH_SCORES.insertMany([
  { name: 'John', score: 100 },
  { name: 'Jane', score: 200 },
  { name: 'Bob', score: 50 }
]);