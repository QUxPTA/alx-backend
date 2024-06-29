import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;
  let consoleLogStub;
  let consoleErrorStub;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
    consoleLogStub = sinon.stub(console, 'log');
    consoleErrorStub = sinon.stub(console, 'error');
  });

  afterEach(() => {
    queue.testMode.exit();
    queue.removeAllListeners();
    consoleLogStub.restore();
    consoleErrorStub.restore();
  });

  it('should add jobs to the queue with the correct type', () => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Test message' }];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification');
  });

  it('should log a success message when a job is created', () => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Test message' }];
    createPushNotificationsJobs(jobs, queue);
    sinon.assert.calledWith(consoleLogStub, 'Notification job created: 2');
  });

  it('should log an error message when a job creation fails', () => {
    const jobs = [{ phoneNumber: '1234567890', message: 'Test message' }];
    const error = new Error('Job creation failed');
    sinon.stub(queue, 'create').throws(error);
    createPushNotificationsJobs(jobs, queue);
    sinon.assert.calledWith(consoleErrorStub, `Error creating job: ${error}`);
  });
});
