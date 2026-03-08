from gameElements.agent import Agent

class humanHugh(Agent):

    def choose_action(self, player, state, valid_actions):
        print(valid_actions)
        return input("Choose card: ")