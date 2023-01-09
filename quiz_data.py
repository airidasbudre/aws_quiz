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
