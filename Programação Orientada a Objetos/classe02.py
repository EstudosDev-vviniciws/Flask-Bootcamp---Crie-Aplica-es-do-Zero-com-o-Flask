"""Instanciando a Classe"""

class Game:
    name = ""
    YearLauch = 0
    multiplayer = False
    note = 0
    
game1 = Game()
game1.name = "Counter Strike"
game1.YearLauch = "2023"
game1.multiplayer = "True"
game1.note = "8.5"

game2 = Game()
game2.name = "Phasmofobia"
game2.YearLauch = "2012"
game2.multiplayer = "True"
game2.note = "8.0"

print("-- Dados do Jogo --")
print(f"Nome do jogo: {game1.name}\nAno de Lançamento: {game1.YearLauch}\n")

print("-- Dados do Jogo --")
print(f"Nome do jogo: {game2.name}\nAno de lançamento: {game2.YearLauch}\n")