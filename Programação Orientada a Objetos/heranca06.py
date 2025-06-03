"""Herança"""

# Classe Pai (Super classe) - Generalista

class Game:
    total_games = 0
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
    
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("-- Dados do Jogo --")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"Avaliação do jogo: {self.note}\n")
    
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
    
    def average(self):
        print(f"A média do jogo: {self.name}: {self.totalEvaluation / self.evaluators}")

# Classe Derivada (Subclasse) - Especializada

class SinglePlayerGame(Game):
    def __init__(self, name="", yearLaunch=0, note=0, storyLine=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.storyLine = storyLine
        
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyLine}\n")

mult_game = Game("Call of Duty Black Ops II", 2012, True, 9.5)
mult_game.technical_sheet()

single_game = SinglePlayerGame("Blair Witch", 2017, 9.0, "História de sobrevivência tenebrosa e emocionante")
single_game.technical_sheet()

