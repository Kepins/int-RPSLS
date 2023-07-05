class AnswerOption:
    def __init__(self, matching_inputs: list[str], return_value):
        # if user input is one of strings in matching_inputs
        # then option return_value will be returned
        self.matching_inputs = matching_inputs
        self.return_value = return_value
