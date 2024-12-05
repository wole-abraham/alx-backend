import { createClient } from 'redis';

(async () => {
  // Create a Redis client
  const client = createClient();

  // Event listener for connection errors
  client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
  });

  try {
    // Connect to the Redis server
    await client.connect();
    console.log('Redis client connected to the server');
  } catch (err) {
    console.error(`Failed to connect: ${err.message}`);
  }
})();
