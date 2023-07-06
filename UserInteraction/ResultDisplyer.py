from Enums.GameResultEnum import GameResultEnum
from Figures.Figure import Figure


class ResultDisplayer:
    def __init__(self, user_decision: Figure, opponent_decision: Figure, result: GameResultEnum):
        self.user_decision = user_decision
        self.opponent_decision = opponent_decision
        self.result = result

    def display(self):
        if self.result == GameResultEnum.WIN:
            print(f"You won choosing {self.user_decision.name} "
                  f"against {self.opponent_decision.name}.")
        elif self.result == GameResultEnum.TIE:
            print(f"You tied choosing {self.user_decision.name} "
                  f"against {self.opponent_decision.name}.")
        else:
            # self.result == GameResultEnum.LOSS
            print(f"You lost choosing {self.user_decision.name} "
                  f"against {self.opponent_decision.name}.")
