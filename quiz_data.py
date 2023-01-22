import requests

parameters = {
    "amount": 2,
    "type": "multiple"
}



question_data = [
  {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'According to AWS, what is the benefit of Elasticity?',
      'correct_answer': 'Create systems that scale to the required capacity based on changes in demand', 
      'incorrect_answers': [
          'Minimize storage requirements by reducing logging and auditing activities', 
          'Enable AWS to automatically select the most cost-effective services.', 
          'Accelerate the design process because recovery from failure is automated, reducing the need for testing'
          ]
  }, 
  {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'What is the AWS feature that enables fast, easy and secure transfers\n of files over long distances between your client and your Amazon S3 bucket?',
      'correct_answer': 'Amazon S3 Transfer Acceleration', 
      'incorrect_answers': [
          'File Transfer', 
          'HTTP Transfer', 
          'S3 Acceleration'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A business analyst would like to move away from creating complex\n database queries and static spreadsheets when generating regular reports for high-level management. They would like to publish insightful, graphically appealing reports with interactive dashboards. Which service can they use to accomplish this?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'What best describes the “Principle of Least Privilege”?\n Choose the correct answer from the options given below.',
      'correct_answer': 'Users should be granted permission to access only resources they need to do their assigned job.', 
      'incorrect_answers': [
          'All users should have the same baseline permissions granted to them to use basic AWS services.', 
          'Users should submit all access requests in written form so that\n there is a paper trail of who needs access to different AWS resources.', 
          'Users should always have a little more permission than they need.'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A web administrator maintains several public and private web-based\n resources for an organisation. Which service can they use to keep track of the expiry dates of SSL/TLS certificates as well as updating and renewal?',
      'correct_answer': 'AWS Certificate Manager', 
      'incorrect_answers': [
          'AWS Data Lifecycle Manager', 
          'AWS License Manager', 
          'AWS Firewall Manager'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following is the responsibility of the customer to ensure\n the availability and backup of the EBS volumes?',
      'correct_answer': 'Create EBS snapshots.', 
      'incorrect_answers': [
          'Delete the data and create a new EBS volume.', 
          'Attach new volumes to EC2 Instances.', 
          'Create copies of EBS Volumes.'
          ]
      },
      # 8
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following services can be used as an application firewall in AWS?',
      'correct_answer': 'AWS WAF', 
      'incorrect_answers': [
          'AWS Snowball', 
          'AWS Firewall', 
          'AWS Protection'
          ]
      },
      # 9
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Your design team is planning to design an application that will be hosted on the AWS Cloud.\n  One of their main non-functional requirements is given below:\n  Reduce inter-dependencies so failures do not impact other components. \n Which of the following concepts does this requirement relate to?',
      'correct_answer': 'Decoupling', 
      'incorrect_answers': [
          'Integration', 
          'Aggregation', 
          'Segregation'
          ]
      },
      # 10
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A manufacturing firm has recently migrated their application servers to the Amazon EC2 instance.\n The IT Manager is looking for the details of upcoming scheduled maintenance activities which AWS would be performing on AWS resources, that may impact the services on these EC2 instances.',
      'correct_answer': 'AWS Personal Health Dashboard', 
      'incorrect_answers': [
          'AWS Organizations', 
          'AWS Trusted Advisor', 
          'AWS Service Health Dashboard'
          ]
      },
      # 11
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following AWS services can be used to retrieve configuration changes\n made to AWS resources causing operational issues?',
      'correct_answer': 'AWS Config', 
      'incorrect_answers': [
          'Amazon Inspector', 
          'AWS CloudFormation', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which tool can you use to forecast your AWS spending?',
      'correct_answer': 'AWS Cost Explorer', 
      'incorrect_answers': [
          'AWS Organizations', 
          'Amazon Dev Pay', 
          'AWS Trusted Advisor'
          ]
      },
]
