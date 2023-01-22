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
      'question': 'What is the AWS feature that enables fast, easy and secure transfers of files over long distances between your client and your Amazon S3 bucket?',
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
      'question': 'A business analyst would like to move away from creating complex database queries and static spreadsheets when generating regular reports for high-level management. They would like to publish insightful, graphically appealing reports with interactive dashboards. Which service can they use to accomplish this?',
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
      'question': 'What best describes the “Principle of Least Privilege”? Choose the correct answer from the options given below.',
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
      'question': 'A web administrator maintains several public and private web-based resources for an organisation. Which service can they use to keep track of the expiry dates of SSL/TLS certificates as well as updating and renewal?',
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
      'question': 'Which of the following is the responsibility of the customer to ensure the availability and backup of the EBS volumes?',
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
      'question': 'Your design team is planning to design an application that will be hosted on the AWS Cloud. One of their main non-functional requirements is given below:  Reduce inter-dependencies so failures do not impact other components.  Which of the following concepts does this requirement relate to?',
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
      'question': 'A manufacturing firm has recently migrated their application servers to the Amazon EC2 instance. The IT Manager is looking for the details of upcoming scheduled maintenance activities which AWS would be performing on AWS resources, that may impact the services on these EC2 instances.',
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
      'question': 'Which of the following AWS services can be used to retrieve configuration changes made to AWS resources causing operational issues?',
      'correct_answer': 'AWS Config', 
      'incorrect_answers': [
          'Amazon Inspector', 
          'AWS CloudFormation', 
          'AWS Trusted Advisor'
          ]
      },
      # 12
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'An organization runs several EC2 instances inside a VPC using three subnets, one for Development, one for Test, and one for Production. The Security team has some concerns about the VPC configuration. It requires restricting communication across the EC2 instances using Security Groups. Which of the following options is true for Security Groups related to the scenario?',
      'correct_answer': 'You can change a Security Group associated with an instance if the instance is in the running state.', 
      'incorrect_answers': [
          'You can change a Security Group associated with an instance if the instance is in the hibernate state.', 
          'You can change a Security Group only if there are no instances associated to it.', 
          'The only Security Group you can change is the Default Security Group.'
          ]
      },
      # 13
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following features of Amazon RDS allows for better availability of databases? Choose the answer from the options given below.',
      'correct_answer': 'Multi-AZ', 
      'incorrect_answers': [
          'VPC Peering', 
          'Read Replicas', 
          'Data encryption'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Your company wants to move an existing Oracle database to the AWS Cloud. Which of the following services can help facilitate this move?',
      'correct_answer': 'AWS Database Migration Service', 
      'incorrect_answers': [
          'AWS Inspector', 
          'AWS VM Migration Service', 
          'AWS Trusted Advisor'
          ]
      },
      # 15
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following services allows you to analyze EC2 Instances against pre-defined security templates to check for vulnerabilities?',
      'correct_answer': 'AWS Inspector', 
      'incorrect_answers': [
          'AWS Trusted Advisor', 
          'AWS WAF', 
          'AWS Shield'
          ]
      },
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A website for an international sport governing body would like to serve its content to viewers from different parts of the world in their vernacular language. Which of the following services provide location-based web personalization using geolocation headers?',
      'correct_answer': 'Amazon CloudFront', 
      'incorrect_answers': [
          'Amazon EC2 Instance', 
          'Amazon Lightsail', 
          'Amazon Route 53'
          ]
      },
      # 17
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following can be used to protect against DDoS attacks? 2 answers from the options given below are correct.',
      'correct_answer': 'AWS Shield',
      'correct_answer': 'AWS Shield Advanced', 
      'incorrect_answers': [
          'AWS EC2', 
          'AWS RDS'
          ]
      },
      # 18
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following are the recommended resources to be deployed in the  Amazon VPC private subnet?',
      'correct_answer': 'Database Servers', 
      'incorrect_answers': [
          'NAT Gateways', 
          'Bastion Hosts', 
          'Internet Gateways'
          ]
      },
      # 19
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A company wants to utilize AWS storage. For them, low storage cost is paramount. The data is rarely retrieved and a data retrieval time of 13-14 hours is acceptable for them. What is the best storage option to use?',
      'correct_answer': 'S3 Glacier Deep Archive', 
      'incorrect_answers': [
          'Amazon S3 Glacier', 
          'Amazon EBS volumes', 
          'AWS CloudFront'
          ]
      },
      # 20
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
      'question': 'Which AWS service provides a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability?',
      'correct_answer': 'DynamoDB', 
      'incorrect_answers': [
          'AWS RDS', 
          'Oracle RDS', 
          'Elastic Map Reduce'
          ]
      },
      # 21
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
