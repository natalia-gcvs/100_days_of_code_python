from turtle import Screen


class Answer:
    def __init__(self, count):
        screen = Screen()
        self.answer_state = screen.textinput(f"{count}/50 States Correct", "What's another state's name?").split()

    def converter(self):
        answer_state_list = []
        for i in self.answer_state:
            i = i[0].upper() + i[1:].lower()
            answer_state_list.append(i)
        answer_state_str = ' '.join(answer_state_list)
        return answer_state_str
