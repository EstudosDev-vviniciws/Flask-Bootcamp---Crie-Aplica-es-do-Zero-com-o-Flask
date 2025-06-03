"""Variável de Classe"""

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
    
game1 = Game("Counter Stike", 2023, True, 8.5)
game2 = Game("Forzan 5", 2023, True, 9.0)
game3 = Game("The Last Of Us IV", 2024, False, 9.5)

game1.technical_sheet()
game2.technical_sheet()
game3.technical_sheet()

game1.evaluate(9.0)
game1.evaluate(7.5)
game1.average()
game2.evaluate(8.0)
game2.evaluate(8.5)
game2.average()

print(f"Total de jogos criados: {Game.total_games}")