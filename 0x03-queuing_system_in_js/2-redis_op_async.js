#!/usr/bin/yarn dev
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.get = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => client.set(schoolName, value, print);

const displaySchoolValue = async (schoolName) => console.log(`${await client.get(schoolName)}`);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
