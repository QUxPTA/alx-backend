const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// Create Express app and Redis client
const app = express();
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Define the list of products
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

// Function to get item by ID
function getItemById(id) {
  return listProducts.find((product) => product.itemId === parseInt(id));
}

// Function to reserve stock by ID
async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

// Function to get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : 0;
}

// Route to get the list of products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get product details by ID
app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity =
    (await getCurrentReservedStockById(req.params.itemId)) ||
    item.initialAvailableQuantity;
  res.json({ ...item, currentQuantity });
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  let currentQuantity = await getCurrentReservedStockById(req.params.itemId);
  currentQuantity = currentQuantity || item.initialAvailableQuantity;

  if (currentQuantity <= 0) {
    return res.json({
      status: 'Not enough stock available',
      itemId: parseInt(req.params.itemId),
    });
  }

  await reserveStockById(req.params.itemId, currentQuantity - 1);
  res.json({
    status: 'Reservation confirmed',
    itemId: parseInt(req.params.itemId),
  });
});

const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
