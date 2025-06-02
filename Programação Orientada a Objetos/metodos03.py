"""Métodos Especiais"""

class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name}"
    
game1 = Game("Counter Stike", 2023, True, 8.5)
game2 = Game("Forzan 5", 2023, True, 9.0)
game3 = Game("The Last Of Us IV", 2024, False, 9.5)

print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}\nAvaliação do jogo: {game1.note}")
print(f"\nNome do jogo: {game2.name}\nAno de lançamento: {game2.yearLaunch}\n Avaliação do jogo: {game2.note}")
print(f"\nNome do jogo: {game3.name}\nAno de lançamento: {game3.yearLaunch}\n Avaliação do jogo: {game3.note}")


