class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }  
    def play_game(self):
        print('Shall we play a game?')  
        while self.winner is None and self.tie is False:
            self.render()
            move = self.get_move()
            self.board[move] = self.turn
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()
        

 

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
             1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                  ----------
             2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                  ----------
             3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
         """)
    
    def print_message(self):
        if self.tie == True:
            print('tie game!')
        elif self.tie == False and self.winner== None: 
            print(f"it's player {self.turn}'s turn!")     
        elif self.tie == False and self.winner != None:
            print(f'{self.winner} wins the game!')
           

    def render(self):
        self.print_board()
        self.print_message()            

    def get_move(self):
          while True:
             move = input(f"Enter a valid movie (example: A1): ").lower()
             if move in self.board and self.board[move] is None:
                 return move
             else:
                 print('Invalid move. Try again.')


    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'b2', 'c3'],
            ['a3', 'b2', 'c1'],
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]]:
                self.winner = self.board[combination[0]]
                return True
           

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()):
            if self.winner is None:
                self.tie = True
                return True
        return False


    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'   
         


game_instance = Game()
game_instance.play_game()