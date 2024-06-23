from deck import Deck
from player import Player

class Game:
    def __init__(self):
        name1 = input('プレイヤー１の名前: ')
        name2 = input('プレイヤー２の名前: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def print_winner(self, winner):
        w = 'このラウンドは{}が勝ちました'
        print(w.format(winner.name))
    
    def print_draw(self, p1, p2):
        d = '{}は{}、{}は{}を引きました'
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print('戦争を始めます!')
        while len(cards) >= 2:
            m = 'qで終了、それ以外のキーでPlay: '
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)
        win = self.winner(self.p1, self.p2)
        print('ゲーム終了、{}の勝利です！'.format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return '引き分け！'