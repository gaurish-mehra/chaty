import jsonlines
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QInputDialog
from PyQt5.QtCore import Qt


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load data from JSONL file
        self.file_path = 'data.jsonl'
        self.data = self.load_data()

        # Create GUI window
        self.setWindowTitle('Chatbot')

        # Create question label and entry field
        question_label = QLabel('What is your question?', self)
        question_label.setAlignment(Qt.AlignCenter)
        question_label.setGeometry(10, 10, 280, 20)

        self.question_entry = QLineEdit(self)
        self.question_entry.setGeometry(10, 35, 280, 30)
        self.question_entry.returnPressed.connect(self.submit_question)

        # Create answer label and text field
        answer_label = QLabel('Answer:', self)
        answer_label.setAlignment(Qt.AlignCenter)
        answer_label.setGeometry(10, 75, 280, 20)

        self.answer_text = QTextEdit(self)
        self.answer_text.setReadOnly(True)
        self.answer_text.setGeometry(10, 100, 280, 100)

        # Create submit button
        submit_button = QPushButton('Submit', self)
        submit_button.setGeometry(110, 210, 80, 30)
        submit_button.clicked.connect(self.submit_question)

        # Create status label
        self.status_label = QLabel('', self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setGeometry(10, 250, 280, 20)

    # Load data from JSONL file
    def load_data(self):
        with jsonlines.open(self.file_path) as reader:
            data = [line for line in reader]
        return data

    # Save data to JSONL file
    def save_data(self, data):
        with jsonlines.open(self.file_path, mode='a') as writer:
            writer.write(data)

    # Train the AI with provided data
    def train(self, data):
        # Add your training code here
        pass

    # Use the trained AI to answer questions
    def answer_question(self, question):
        # Add your answer code here
        pass

    # Callback function for submit button
    def submit_question(self):
        # Get the user's question
        question = self.question_entry.text()

        # Check if user wants to exit
        if question.lower() == 'exit':
            self.close()
            return

        # Check if the question is in the stored data
        for entry in self.data:
            if entry['question'].lower() == question.lower():
                self.answer_text.setPlainText(entry['answer'])
                break
        else:
            # If question is not in the stored data, ask for answer and save to file
            answer, ok = QInputDialog.getText(self, 'Provide an answer', 'I do not know the answer. Please provide an answer:')
            if ok:
                new_entry = {'question': question, 'answer': answer}
                self.save_data(new_entry)
                self.data.append(new_entry)
                self.answer_text.setPlainText(answer)
                self.status_label.setText('Thank you for teaching me!')
def main():
    app = QApplication([])
    chatbot_window = ChatbotWindow()
    chatbot_window.setGeometry(100, 100, 300, 280)
    chatbot_window.show()
    app.exec_()
if __name__ == '__main__':
    main()