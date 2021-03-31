#  Gustavo Sanchez PSID:1861118

class Team: #class name
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):  # get percentage of wins
        percentage = self.team_wins / (self.team_wins + self.team_losses)
        return percentage


if __name__ == "__main__": #main codes

    team = Team()

    team_name = input() #input name and wins and losses
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.8125: #check conditions
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')




