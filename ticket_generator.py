import random


class TicketGenerator:
    def __init__(self, students_file, questions_file):
        self.students = self.read_students(students_file)
        self.questions = self.read_questions(questions_file)

    def read_students(self, file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    def read_questions(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            questions = {}
            current_topic = None
            for line in lines:
                line = line.strip()
                if line.startswith('Тема:'):
                    current_topic = line[6:].strip()
                    questions[current_topic] = []
                elif line:
                    questions[current_topic].append(line)
            return questions

    def generate_tickets(self):
        tickets = []
        for student in self.students:
            ticket = self.generate_ticket()
            tickets.append((student, ticket))
        return tickets

    def generate_ticket(self):
        ticket = {}
        for topic, questions in self.questions.items():
            ticket[topic] = self.generate_questions(questions)
        return ticket

    def generate_questions(self, questions):
        num_questions = random.randint(1, len(questions))
        selected_questions = random.sample(questions, num_questions)
        return selected_questions

    def write_tickets(self, tickets, output_file):
        with open(output_file, 'w') as file:
            for student, ticket in tickets:
                file.write(f'{student} [\n')
                for topic, questions in ticket.items():
                    file.write(f'    {topic}: {", ".join(questions)}\n')
                file.write(']\n')


if __name__ == "__main__":
    students_file = input("Введите путь к файлу со студентами: ")
    questions_file = input("Введите путь к файлу с вопросами: ")
    output_file = input("Введите путь к файлу для сохранения билетов: ")

    generator = TicketGenerator(students_file, questions_file)
    tickets = generator.generate_tickets()
    generator.write_tickets(tickets, output_file)
    print("Билеты успешно сгенерированы и сохранены в файле.")
