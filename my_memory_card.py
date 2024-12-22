from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QRadioButton
from random import shuffle 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')

question = QLabel('Самый сложный вопрос в мире: какой национальности не существует?')
ans = QPushButton('Ответить')

AnsGroupBox = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('Вариант1')
rbtn2 = QRadioButton('Вариант2')
rbtn3 = QRadioButton('Вариант3')
rbtn4 = QRadioButton('Вариант4')

answers = [rbtn1, rbtn2, rbtn3, rbtn4]



answer_layout = QVBoxLayout()
answer_layout.addWidget(rbtn1)
answer_layout.addWidget(rbtn2)
answer_layout.addWidget(rbtn3)
answer_layout.addWidget(rbtn4)
AnsGroupBox.setLayout(answer_layout)

RadioGroupBox = QGroupBox('Результат теста')
res = QLabel('Правильно/Неправильно')
res2 = QLabel('Правильный ответ')

result_layout = QVBoxLayout()
result_layout.addWidget(res)
result_layout.addWidget(res2)
RadioGroupBox.setLayout(result_layout)

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_main.addWidget(AnsGroupBox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_main.addWidget(RadioGroupBox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_main.addWidget(ans, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

RadioGroupBox.hide()



def ask(q: Question):
    question = QLabel('Какой самый большой материк на земле?')
    right_answer = QLabel('Евразия')
    wrong1 = QLabel('Африка')
    wrong2 = QLabel('Антарктида')
    wrong3 = QLabel('Северная Америка')


def buttons():
    RadioGroupBox.show() 
    check_answer()
    ask(w)


def ask(q: Question):
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    res2.setText(f'Правильный вариант ответа: {q.right_answer}')

def show_correct(result):
    res.setText(result)

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')

w = Question('Какой национальности не существует?','Смурфы','Энцы','Алеуты','Чулымцы')
ask(w)

        

ans.clicked.connect(buttons)

main_win.setLayout(layout_main)

main_win.show()
app.exec_()