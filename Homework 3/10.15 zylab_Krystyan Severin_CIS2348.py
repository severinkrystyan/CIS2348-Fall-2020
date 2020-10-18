"""Name: Krystyan Severin
   PSID: 1916594"""


class Team:
    def __init__(self, name='none', wins=0, losses=0):
        self.team_name = name
        self.team_wins = wins
        self.team_losses = losses

    def get_win_percentage(self):
        if self.team_wins > self.team_losses:
            print(f'Congratulations, Team {self.team_name} has a winning average!')
        else:
            print(f'Team {self.team_name} has a losing average.')
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    # Takes user inputs
    team_name = input()
    team_wins = int(input())
    team_loses = int(input())
    # Creates instance of class Team
    team = Team(team_name, team_wins, team_loses)
    team.get_win_percentage()
