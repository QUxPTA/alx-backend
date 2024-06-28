import kue from 'kue';

// Create Kue queue
const queue = kue.createQueue();

// Create a job data object
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (err) {
    console.log(`Notification job failed: ${err}`);
    return;
  }
  console.log(`Notification job created: ${job.id}`);
});

// Event listeners for the job
job
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', (err) => {
    console.log(`Notification job failed: ${err}`);
  });
