#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const jobData = {
  phoneNumber: '70127595',
  message: 'Account verified',
};
/* Queue creation */
const push_notification_code = createQueue();

/* Enqueuing a new job  */
const job = push_notification_code.create('push_notification_code', jobData).save((e) => !e && console.log(`Notification job created: ${job.id}`));
job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
