import random
import time
import sys

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class thrPtContestant:
    def __init__(self, name, age, team, threePointPercent, fgPercent, threePointersMade):
        self.name = name
        self.age = age
        self.team = team
        self.threePointPercent = threePointPercent
        self.fgPercent = fgPercent
        self.threePointersMade = threePointersMade
        self.made_shots = 0

    def calculate_three_point_rating(self):
        return (self.threePointersMade - self. fgPercent - self.threePointPercent) / 3

    def shoot_racks(self):
        total_made_shots = 0
        threePointRating = self.calculate_three_point_rating()

        for rack in range(5):
            made_shots = 0
            print(f"\n{self.name} is shooting on rack {rack + 1} now")
            made_this_rack = sum(1 for _ in range(5) if random.random() < threePointRating)
            total_made_shots += made_this_rack
            delay_print(f"Made {made_this_rack} shots this rack \n")

        self.made_shots = total_made_shots
        print(f"total made shots: {self.made_shots}")

    def contest(self, other_contestant):
        self.print_contestant_details()
        print("\n Vs")
        other_contestant.print_contestant_details()

        self.shoot_racks()
        other_contestant.shoot_racks()

        if self.made_shots > other_contestant.made_shots:
            print(f"{self.name} has won the 3pt contest!!")

        elif self.made_shots < other_contestant.made_shots:
            print(f"{other_contestant.name} has won the 3pt contest")

        else:
            print(f"it is a tie and we shall go again")
            self.shoot_racks()
            other_contestant.shoot_racks()

    def print_contestant_details(self):
        print(f"{self.name},")
        print(f"AGE: {self.age}")
        print(f"TEAM: {self.team}")
        print(f"3pt Percentage: {self.threePointPercent}")
        print(f"Field Goal Percentage: {self.fgPercent}")
        print(f"3-pointers Made this season: {self.threePointersMade}\n")


if __name__ == '__main__':
    contestant1 = thrPtContestant("Alice", 25, "Team A", 0.35, 0.45, 50)
    contestant2 = thrPtContestant("Bob", 28, "Team B", 0.32, 0.40, 45)

    contestant1.contest(contestant2)