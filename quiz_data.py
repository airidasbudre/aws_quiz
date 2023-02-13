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
      'question': 'For which of the following AWS resources, the Customer is responsible for the infrastructure-related security configurations?',
      'correct_answer': 'Amazon EC2', 
      'incorrect_answers': [
          'Amazon RDS', 
          'Amazon DynamoDB', 
          'AWS Fargate'
          ]
      },
      # 22
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'In the shared responsibility model for infrastructure services, such as Amazon Elastic Compute Cloud, which of the below are customers responsibility?',
      'correct_answer': 'Amazon Machine Images (AMIs)', 
      'incorrect_answers': [
          'Network infrastructure', 
          'Virtualization infrastructure', 
          'Physical security of hardware'
          ]
      },
      # 23
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'AWS offers two savings plans to enable more savings and flexibility for its customers, namely, compute saving plans and EC2 Instance Savings plans. Which of the below statement is FALSE regarding Saving Plans?',
      'correct_answer': 'Savings Plans are available for all the regions.', 
      'incorrect_answers': [
          'Capacity Reservations are not provided with Saving Plans.', 
          'Savings plans will apply on ‘On-Demand Capacity Reservations’ that customers can allocate for their needs.', 
          'The prices for Savings Plans do not change based on the amount of hourly commitment.'
          ]
      },
      # 24
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the below-listed services is a region-based AWS service?',
      'correct_answer': 'Amazon EFS', 
      'incorrect_answers': [
          'AWS IAM', 
          'Amazon Route 53', 
          'Amazon CloudFront'
          ]
      },
      # 25
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following LightSail Wizard allows the customers to “create a copy of the LightSail instance in EC2”?',
      'correct_answer': 'Upgrade to EC2', 
      'incorrect_answers': [
          'LightSail Backup', 
          'LightSail Copy', 
          'LightSail-EC2 snapshot'
          ]
      },
      # 26
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following features of Amazon Connect helps better customer engagement on AWS Cloud ?',
      'correct_answer': 'High Quality Audio', 
      'incorrect_answers': [
          'Push Notification', 
          'Mailbox Simulator', 
          'Reputation Dashboard'
          ]
      },
      # 27
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A large IT company is looking to enable its large user base to remotely access Linux desktops from any location. Which service can be used for this purpose ?',
      'correct_answer': 'Amazon WorkSpaces', 
      'incorrect_answers': [
          'Amazon Cognito', 
          'Amazon AppStream 2.0', 
          'Amazon WorkLink'
          ]
      },
      # 28
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Users in the Developer Team need to deploy a multi-tier web application. Which service can be used to create a customized portfolio that will help users for quick deployment?',
      'correct_answer': 'AWS Service Catalog', 
      'incorrect_answers': [
          'AWS Config', 
          'AWS Code Deploy', 
          'AWS Cloud Formation'
          ]
      },
      # 29
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A large Oil & gas company is planning to deploy a high-volume application on multiple Amazon EC2 instances.  Which of the following can help to reduce operational expenses?',
      'correct_answer': 'Deploy Amazon EC2 instance with Auto-scaling', 
      'incorrect_answers': [
          'Deploy Amazon EC2 instance in multiple AZ’s', 
          'Deploy Amazon EC2 instance with Amazon instance store-backed AMI', 
          'Deploy Amazon EC2 instance with Cluster placement group'
          ]
      },
      # 30
    {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following activity are within the scope of AWS Support?',
      'correct_answer': 'Troubleshooting API issues', 
      'incorrect_answers': [
          'Code Development', 
          'Debugging custom software', 
          'Database query tuning'
          ]
      },
      # 31
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A company is planning to run a global marketing application in the AWS Cloud. The application will feature videos that can be viewed by users. The company must ensure that all users can view these videos with low latency.',
      'correct_answer': ' Amazon CloudFront ', 
      'incorrect_answers': [
          'AWS Auto Scaling', 
          'Amazon Kinesis Video Streams', 
          'Elastic Load Balancing'
          ]
      },
      # 32
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which pillar of the AWS Well-Architected Framework refers to the ability of a system to recover from infrastructure or service disruptions and dynamically acquire computing resources to meet demand?',
      'correct_answer': 'Reliability ', 
      'incorrect_answers': [
          'Security', 
          'Performance efficiency', 
          'Cost optimization'
          ]
      },
      # 33
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which of the following are benefits of migrating to the AWS Cloud?',
      'correct_answer': 'Operational resilience ', 
      'correct_answer': 'Business agility  ', 
      'incorrect_answers': [
          'Discounts for products on Amazon.com', 
          'Business excellence', 
          'Increased staff retention'
          ]
      },
      # 34
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A company is planning to replace its physical on-premises compute servers with AWS serverless compute services. The company wants to be able to take advantage of advanced technologies quickly after the migration.Which pillar of the AWS Well-Architected Framework does this plan represent?',
      'correct_answer': 'Performance efficiency', 
      'incorrect_answers': [
          'Security', 
          'Operational excellence', 
          'Reliability'
          ]
      },
      # 35
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A large company has multiple departments. Each department has its own AWS account. Each department has purchased Amazon EC2 Reserved Instances.Some departments do not use all the Reserved Instances that they purchased, and other departments need more Reserved Instances than they purchased.The company needs to manage the AWS accounts for all the departments so that the departments can share the Reserved Instances.Which AWS service or tool should the company use to meet these requirements?',
      'correct_answer': 'AWS Organizations ', 
      'incorrect_answers': [
          'AWS Systems Manager', 
          'Cost Explorer', 
          'AWS Trusted Advisor'
          ]
      },
      # 36
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which component of the AWS global infrastructure is made up of one or more discrete data centers that have redundant power, networking, and connectivity?',
      'correct_answer': 'Availability Zone', 
      'incorrect_answers': [
          'AWS Region', 
          'Edge location', 
          'AWS Outposts'
          ]
      },
      # 37
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which duties are the responsibility of a company that is using AWS Lambda? (Choose two.)',
      'correct_answer': 'Security inside of code ', 
      'correct_answer': 'Writing and updating of code', 
      'incorrect_answers': [
          'Selection of CPU resources', 
          'Patching of operating system', 
          'Security of underlying infrastructure'
          ]
      },
      # 38
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'Which AWS services or features provide disaster recovery solutions for Amazon EC2 instances? (Choose two.)',
      'correct_answer': 'EC2 Amazon Machine Images (AMIs)', 
      'correct_answer': 'Amazon Elastic Block Store (Amazon EBS) snapshots', 
      'incorrect_answers': [
          '¡2 Reserved Instances', 
          'AWS Shield', 
          'Amazon GuardDuty'
          ]
      },
      # 39
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A company is migrating to the AWS Cloud instead of running its infrastructure on premises.Which of the following are advantages of this migration? (Choose two.)',
      'correct_answer': 'Increased global reach and agility', 
      'correct_answer': 'Ability to deploy globally in minutes', 
      'incorrect_answers': [
          'Elimination of the cost of IT staff members', 
          'Redundancy by default for all compute services', 
          'Elimination of the need to perform security auditing'
          ]
      },
      # 40
      {
      'category': 'AWS', 
      'type': 'multiple', 
      'difficulty': 'medium', 
      'question': 'A user is comparing purchase options for an application that runs on Amazon EC2 and Amazon RDS. The application cannot sustain any interruption. The application experiences a predictable amount of usage, including some seasonal spikes that last only a few weeks at a time. It is not possible to modify the application.Which purchase option meets these requirements MOST cost-effectively?',
      'correct_answer': 'Buy Reserved Instances for the predicted amount of usage throughout the year. Allow any seasonal usage to run at an On-Demand rate.', 
      'incorrect_answers': [
          'Review the AWS Marketplace and buy Partial Upfront Reserved Instances to cover the predicted and seasonal load.', 
          'Buy Reserved Instances for the predicted amount of usage throughout the year. Allow any seasonal usage to run on Spot Instances.', 
          'Buy Reserved Instances to cover all potential usage that results from the seasonal usage.'
          ]
      },
]
