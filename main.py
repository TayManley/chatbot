from fuzzywuzzy import process
import random

# Keywords for different topics
topics = {
    'auditing': ['audit', 'auditor', 'financial', 'records'],
    'data_science': ['data', 'analytics', 'machine_learning', 'statistics'],
    'government_consulting': ['government', 'public sector', 'strategy', 'operations'],
    'information_technology': ['IT', 'tech', 'networking', 'cybersecurity'],
    'python': ['python', 'coding', 'programming', 'language', 'learn'],
    'federal_financial_management': ['federal', 'budget', 'financial_management', 'performance', 'accountability'],
    'information_systems': ['information_systems', 'IT_infrastructure', 'database', 'cloud_computing'],
    'project_management': ['project management', 'project planning', 'project execution', 'project control'],
    'business_analysis': ['business analysis', 'business requirements', 'business processes', 'requirements gathering'],
    'marketing': ['marketing', 'advertising', 'branding', 'product promotion'],
    'human_resources': ["talent acquisition", "employee engagement", "performance management", "leadership development", "compensation and benefits", "organizational design", "succession planning", "HR strategy", "diversity and inclusion", "HR technology"]
}

# Responses for each topic
auditing_responses = ['Auditing is the process of evaluating a company or organization’s financial records to ensure that they are accurate and comply with relevant laws and regulations.', 'The goal of auditing is to provide an objective assessment of the financial health and performance of a company or organization.', 'Auditing is the process of examining financial records and other important documents to ensure accuracy and compliance with relevant laws and regulations.', 'Auditing is the practice of verifying and validating information or processes to ensure that they conform to established standards, guidelines, or best practices.']
data_science_responses = ['Data science is an interdisciplinary field that involves using scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.', 'Data scientists analyze data to uncover patterns, trends, and relationships that can be used to inform business decisions and drive innovation.']
government_consulting_responses = ['Government consulting involves working with public sector clients to help them improve their operations, achieve their strategic goals, and navigate complex regulatory environments.', 'Government consultants often provide expertise in areas such as policy analysis, program management, and technology implementation.']
information_technology_responses = ['Information technology (IT) refers to the use of computers, software, and networks to store, process, and transmit data.', 'IT professionals design, develop, and maintain computer systems, networks, and software applications to meet the needs of organizations and individuals.']
python_responses = ['Python is a high-level programming language that is used for a wide range of applications, from web development and scientific computing to machine learning and data analysis.', 'Python is known for its simplicity, readability, and versatility, making it a popular choice for both beginners and experienced programmers. If you want to learn Python, you can start by reading online tutorials, taking courses, or practicing with coding challenges.']
federal_financial_management_responses = ['Federal financial management involves managing financial resources at the federal level to ensure accountability, transparency, and effective use of public funds.', 'FFM professionals play a critical role in developing and executing budgets, monitoring performance, and providing financial analysis to support decision-making.', 'FFM policies and procedures are designed to comply with federal laws, regulations, and guidance, and to promote best practices in financial management.']
information_systems_responses = ['Information systems refer to the combination of people, processes, and technology used to collect, store, process, and disseminate information in an organization.', 'IS professionals design, implement, and manage IT systems such as databases, networks, and cloud infrastructure to support business operations and decision-making.']
project_management_responses = ['Project management is the practice of initiating, planning, executing, controlling, and closing the work of a team to achieve specific goals and meet specific success criteria at the specified time.', 'Project managers are responsible for ensuring that projects are completed on time, within budget, and to the satisfaction of stakeholders.']
business_analysis_responses = ['Business analysis is the process of identifying business needs and finding solutions to meet those needs through a combination of technology, processes, and policies.', 'Business analysis involves analyzing data and other information to help organizations make informed decisions and improve their operations and processes.', 'Business analysis is a set of techniques and tools used to understand business processes, identify areas for improvement, and recommend solutions to achieve business goals.']
marketing_responses = ['Marketing is the process of creating, communicating, delivering, and exchanging offerings that have value for customers, clients, partners, and society at large.', 'Marketing is the art and science of identifying, creating, and delivering value to satisfy the needs of a target market at a profit.', 'Marketing is the process of understanding, creating, and delivering value to customers and for managing customer relationships in ways that benefit the organization and its stakeholders.']
human_resources_responses = ['HR consulting involves providing expert advice and support to organizations on all aspects of human resource management, including recruitment, retention, performance management, compensation and benefits, and employee relations. The goal is to help organizations optimize their workforce and create a positive and productive workplace culture.', 'HR consulting is a specialized form of management consulting that focuses on the people side of the business. Consultants work with clients to design and implement HR policies and programs that align with business objectives and promote organizational effectiveness.', 'HR consulting provides organizations with guidance and support on a range of HR issues, such as compliance with labor laws and regulations, diversity and inclusion, employee engagement and well-being, and talent management. Consultants may also provide training and development programs to enhance employee skills and knowledge.']

# Main function to handle user input and provide responses
def chatbot():
    print("Hi, I'm a chatbot! What would you like to know? I can answer questions about auditing, data science, government consulting, information technology, Python, federal financial management, and information systems.")
    while True:
        user_input = input().lower()
        topic_match = process.extractOne(user_input, topics.keys())
        if topic_match[1] > 80:
            print(random.choice(globals()[f'{topic_match[0]}_responses']))
        elif 'bye' in user_input:
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I don't understand. Please ask me about auditing, data science, government consulting, information")
chatbot()