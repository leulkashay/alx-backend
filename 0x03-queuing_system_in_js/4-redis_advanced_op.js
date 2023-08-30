#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient();
client.on('connect', (error) => {
  console.error('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const hashUpdate = (name, fieldName, value) => client.hset(name, fieldName, value, print);

const printHash = (name) => client.hgetall(name, (_err, reply) => console.log(reply));

hashUpdate('HolbertonSchools', 'Portland', 50);
hashUpdate('HolbertonSchools', 'Seattle', 80);
hashUpdate('HolbertonSchools', 'New York', 20);
hashUpdate('HolbertonSchools', 'Bogota', 20);
hashUpdate('HolbertonSchools', 'Cali', 40);
hashUpdate('HolbertonSchools', 'Paris', 2);
printHash('HolbertonSchools');
