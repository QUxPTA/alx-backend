// Function to create push notification jobs

export default function createPushNotificationsJobs (jobs, queue) {
  jobs.forEach((job) => {
    try {
      const newJob = queue.create('push_notification', job);
      newJob.save((err) => {
        if (err) {
          console.error(`Error creating job: ${err}`);
        } else {
          console.log(`Notification job created: ${newJob.id}`);
        }
      });
    } catch (error) {
      console.error(`Error creating job: ${error}`);
    }
  });
}
