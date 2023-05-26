class InvalidNumberOfPlayersError(Exception):
    """
    Used for raising a custom exception in play_game method
    """
    pass

class Player:
    """
    Represents a Player with a position, state, start space, end space, 2 tokens, and a specific board
    """
    def __init__(self, player_position):
        self._player_position = player_position
        self._state = 'Playing'
        # depending on player_letter chosen, change default start_space data member, end_space data_member,
        # and create tokens specific to that player.
        if self._player_position == 'A':
            self._start_space = 1
            self._end_space = 50
            self._tokens = {'p': Token('p', 'A'), 'q': Token('q', 'A')} #{token name: token object}
            self._board = Board('A').get_board_spaces()
        elif self._player_position == 'B':
            self._start_space = 15
            self._end_space = 8
            self._tokens = {'p': Token('p', 'B'), 'q': Token('q', 'B')}  # {token name: token object}
            self._board = Board('B').get_board_spaces()
        elif self._player_position == 'C':
            self._start_space = 29
            self._end_space = 22
            self._tokens = {'p': Token('p', 'C'), 'q': Token('q', 'C')}  # {token name: token object}
            self._board = Board('C').get_board_spaces()
        else:
            self._start_space = 43
            self._end_space = 36
            self._tokens = {'p': Token('p', 'D'), 'q': Token('q', 'D')}  # {token name: token object}
            self._board = Board('D').get_board_spaces()

    def __repr__(self):
        """
        Takes no parameters
        Used to print out more readable information on a Player object.
        """
        return f'Player object {self._player_position}'

    def get_completed(self):
        """
        Takes no parameters
        Returns True or False if the player has finished or not finished the game
        """
        finished_token_count = 0
        for token_obj in self._tokens.values():
            if token_obj.get_step_count() == 57:
                finished_token_count += 1
        if finished_token_count == 2:
            self._state = 'Finished'
            return True
        return False

    def get_token_p_step_count(self):
        """
        Takes no parameters
        Returns the total steps the token p has taken on the board
        """
        return self._tokens['p'].get_step_count()

    def get_token_q_step_count(self):
        """
        Takes no parameters
        Returns the total steps the token q has taken on the board
        """
        return self._tokens['q'].get_step_count()

    def get_space_name(self, steps_of_token):
        """
        Takes as a parameter the total steps of the token
        Returns the name of the space the token has landed on on the board as a string
        """
        if steps_of_token > 57:
            return None
        elif 51 <= steps_of_token <= 56:
            # insert player position letter to beginning of the string for home spaces
            return f'{self._player_position}{self._board[steps_of_token + 1]}'
        return str(self._board[steps_of_token + 1])

    def get_tokens(self):
        """
        Takes no parameters
        Returns the token dictionary of the Player object that is referenced
        """
        return self._tokens

    def get_board(self):
        """
        Takes no parameters
        Returns the board (list) of the Player object that is referenced
        """
        return self._board

    def get_player_position(self):
        """
        Takes no parameters
        Returns the player position of the Player object that is referenced
        """
        return self._player_position

    def set_both_tokens_to_stacked(self):
        """
        Takes no parameters
        Doesn't return anything
        Used in the stacking/kicking logic to set both of a Player's tokens to be stacked
        """
        for token in self._tokens:
            self._tokens[token].set_is_stacked(True)

    def get_tokens_at_home_count(self):
        """
        Takes no parameters
        Returns a count of how many of Player's tokens are on "Home" space
        Used in play_game method to repeatedly check how many of a Player's tokens are at home
        """
        home_count = 0
        for token_obj in self._tokens.values():
            if token_obj.get_step_count() == -1:
                home_count += 1
        return home_count

class Board:
    """
    Represents a Board with an owner and a board spaces list representing spaces
    """
    def __init__(self, owner):
        self._owner = owner
        self._board_spaces = ['H', 'R']
        # depending on Player position, create a board_spaces list with spaces respective to that position
        if self._owner == 'A':
            for num in range(1, 51):
                self._board_spaces.append(num)

        elif self._owner == 'B':
            for num in range(15, 57):
                self._board_spaces.append(num)
            for num in range(1, 9):
                self._board_spaces.append(num)

        elif self._owner == 'C':
            for num in range(29, 57):
                self._board_spaces.append(num)
            for num in range(1, 23):
                self._board_spaces.append(num)

        else:
            for num in range(43, 57):
                self._board_spaces.append(num)
            for num in range(1, 37):
                self._board_spaces.append(num)

        for num in range(1, 7):
            self._board_spaces.append(num)
        self._board_spaces.append('E')

    def get_board_spaces(self):
        """
        Takes no parameters
        Returns the board spaces list of the Board object that is referenced
        Used by Player class to store a specific board for each Player
        """
        return self._board_spaces

class Token:
    """
    Represents a Token with a letter, position, step count, owner, and stacked value
    """
    def __init__(self, letter, owner):
        self._letter = letter
        self._position = 'H'
        self._step_count = -1
        self._owner = owner
        self._is_stacked = False

    def __repr__(self):
        return(f'Token object {self._letter}, belonging to Player {self._owner}')

    def get_step_count(self):
        """
        Takes no parameters
        Returns the step count of the Token object that is referenced
        """
        return self._step_count

    def get_letter(self):
        """
        Takes no parameters
        Returns the letter of the Token object that is referenced
        """
        return self._letter

    def get_token_position(self):
        """
        Takes no parameters
        Returns the position of the Token object that is referenced
        """
        return self._position

    def get_is_stacked(self):
        """
        Takes no parameters
        Returns the "is stacked" value of the Token object that is referenced
        Used in move_token method to repeatedly check if a Token is stacked
        """
        return self._is_stacked

    def set_step_count(self, new_step_count):
        """
        Takes a new step count as a parameter
        Doesn't return anything
        Sets the step count of the Token object that is referenced to new step count
        """
        self._step_count = new_step_count

    def set_token_position(self, new_position):
        """
        Takes a new position value as parameter
        Doesn't return anything
        Sets the position of the Token object that is referenced to new position.
        """
        self._position = new_position

    def set_is_stacked(self, bool):
        """
        Takes a boolean value as parameter
        Doesn't return anything
        Sets the "is stacked" value of Token object that is referenced to whatever boolean value is passed in
        """
        self._is_stacked = bool

    def increment_token_step_count(self, num_of_steps):
        """
        Takes "num of steps" value as parameter
        Doesn't return anything
        Increments the "step count" value of Token object that is referenced by the amount passed in
        """
        self._step_count += num_of_steps

    def is_finished(self):
        """
        Takes no parameters
        Returns True if Token object that is referenced is on the "End" space, returns False otherwise
        Used in play_game method to check if a token is on the "End" space and finished moving
        """
        if self._step_count == 57:
            return True
        return False

class LudoGame:
    """
    Represents a LudoGame that has a list of players
    """
    def __init__(self):
        self._players = [] #[player_obj, player_obj]

    def get_all_kickable_tokens(self):
        """
        Takes no parameters
        Returns a list containing all Player's token positions
        Used in the play_game method to check if the Player's token that is moving would be able to "kick" another Player's token back to Home
        """
        token_positions_list = []
        for player_obj in self._players:
            for token_obj in player_obj.get_tokens().values():
                # since this method is only used for kicking logic, it only cares about tokens that are not in home spaces
                if token_obj.get_step_count() <= 50:
                    token_positions_list.append(str(token_obj.get_token_position()))
        return token_positions_list

    def check_stacking_or_kicking(self, player_object , token_name):
        """
        Takes a player object and token name ('p' or 'q') as parameters
        Doesn't return anything
        Used in the play_game method to repeatedly check and execute stacking of tokens or kicking of another player's tokens after a move is made
        """
        # store the token position value of the player argument passed in to compare to
        comparison = player_object.get_tokens()[token_name].get_token_position()

        for player in self._players:
            # store the current player's position value
            current_player_position = player.get_player_position()
            # iterate through token object of each player's token dict
            for token_obj in player.get_tokens().values():
                # if current token obj has same position as one that just moved and they don't belong to the same player
                if token_obj.get_token_position() == comparison and player_object.get_player_position() != current_player_position:
                    # if token is stacked, move both tokens back to "Home" space
                    if token_obj.get_is_stacked():
                        for token in player.get_tokens().values():
                            token.set_step_count(-1)
                            token_obj.set_token_position('H')
                            token_obj.set_is_stacked(False)
                    # otherwise, move the one token back to "Home" space
                    else:
                        token_obj.set_step_count(-1)
                        token_obj.set_token_position('H')
                        token_obj.set_is_stacked(False)
                # if current token has the same position as the one that just moved and they belong to the same player
                elif token_obj.get_token_position() == comparison and player_object.get_player_position() == current_player_position:
                    # if they don't have the same token letter, stack them
                    if token_obj.get_letter() != token_name:
                        player.set_both_tokens_to_stacked()

    def move_token(self, player_object, token_name, steps):
        """
        Takes three parameters, the player object, the token name (‘p’ or ‘q’) and the steps the token will move on the board (int).
        Doesn't return anything
        This method takes care of one token moving on the board
        Updates the token’s total steps and takes care of kicking out other opponent tokens as needed
        """
        # get token dictionary of player and iterate through keys
        token_dict = player_object.get_tokens()
        for token in token_dict:
            # if the token_name passed in matches the key in the token dictionary
            if token == token_name:
                # get the token object of the chosen token and board list of player that was chosen
                token_obj = token_dict[token]
                player_board = player_object.get_board()
                # if token is at 'Home' position
                if token_obj.get_token_position() == 'H':
                    # increment step count by 1 to move out of Home
                    token_obj.increment_token_step_count(1)
                # if token is in home spaces and roll would result in token going past 'E'
                elif token_obj.get_step_count() >= 51 and (token_obj.get_step_count() + steps) >= (len(player_board) - 1):
                    # store starting step count for "backtracking" logic
                    start = token_obj.get_step_count() + 1
                    # if the token is stacked, move both of player's tokens with "backtracking" logic
                    if token_obj.get_is_stacked():
                        for token_obj in token_dict.values():
                            new_step_count = 2 * len(player_board) - 2 - (start + steps) - 1
                            token_obj.set_step_count(new_step_count)
                    # otherwise, just move that token with "backtracking" logic
                    else:
                        new_step_count = 2 * len(player_board) - 2 - (start + steps) - 1
                        token_obj.set_step_count(new_step_count)
                # if token is not at home and moving wouldn't put it past 'E'
                else:
                    # if token is stacked, move both of player's tokens
                    if token_obj.get_is_stacked():
                        for token_obj in token_dict.values():
                            token_obj.increment_token_step_count(steps)
                    # otherwise, just move that token
                    else:
                        token_obj.increment_token_step_count(steps)

    def play_game(self, lst_of_players, turns_lst):
        """
        Takes two parameters, the players list, and the turns list (list of tuples)
        Creates the player list first using the players list passed in, and then moves the tokens according to the turns
        list following the priority rule and updates tokens positions and the player’s game state
        Returns a list of strings representing the current spaces of all the tokens for each player
        """

        try:
            self.validate_number_of_players(lst_of_players)
        except InvalidNumberOfPlayersError:
            print('This game only supports 2-4 players.')

        try:
            for player in lst_of_players:
                self.add_player(player)
        except ValueError:
            print('Player positions can only be A, B, C, or D.')

        for player, steps in turns_lst:
            player_obj = self.get_player_by_position(player)
            tokens_at_home = player_obj.get_tokens_at_home_count()
            players_token_dict = player_obj.get_tokens()
            token_p = players_token_dict['p']
            token_q = players_token_dict['q']
            token_p_step_count = token_p.get_step_count()
            token_q_step_count = token_q.get_step_count()

            if tokens_at_home == 2:
                if steps == 6: # 6 is the only valid roll to get out of home
                    self.move_token_and_update_position(player_obj, 'p', steps)

            # if one token is at home and can move, move it
            elif tokens_at_home == 1:
                if steps == 6:
                    if token_p_step_count == -1:
                        self.move_token_and_update_position(player_obj, 'p', steps)
                    elif token_q_step_count == -1:
                        self.move_token_and_update_position(player_obj, 'q', steps)
            # else, move the other token
                elif steps != 6:
                    if token_p_step_count == -1:
                        self.move_token_and_update_position(player_obj, 'q', steps)
                        self.check_stacking_or_kicking(player_obj, 'q')

                    elif token_q_step_count == -1:
                        self.move_token_and_update_position(player_obj, 'p', steps)
                        self.check_stacking_or_kicking(player_obj, 'p')

            else:
                all_players_tokens_positions = self.get_all_kickable_tokens()

                if token_p_step_count + steps == 57:
                    self.move_token_and_update_position(player_obj, 'p', steps)
                    self.check_stacking_or_kicking(player_obj, 'p')

                elif token_q_step_count + steps == 57:
                    self.move_token_and_update_position(player_obj, 'q', steps)
                    self.check_stacking_or_kicking(player_obj, 'q')

                elif (
                        player_obj.get_space_name(token_p_step_count + steps) in all_players_tokens_positions
                        and player_obj.get_space_name(token_q_step_count + steps) in all_players_tokens_positions
                ):
                    if token_p_step_count < token_q_step_count or token_p_step_count == token_q_step_count:
                        self.move_token_and_update_position(player_obj, 'p', steps)
                        self.check_stacking_or_kicking(player_obj, 'p')
                    elif token_q_step_count < token_p_step_count:
                        self.move_token_and_update_position(player_obj, 'q', steps)
                        self.check_stacking_or_kicking(player_obj, 'q')

                elif player_obj.get_space_name(token_p_step_count + steps) in all_players_tokens_positions:
                    self.move_token_and_update_position(player_obj, 'p', steps)
                    self.check_stacking_or_kicking(player_obj, 'p')

                elif player_obj.get_space_name(token_q_step_count + steps) in all_players_tokens_positions:
                    self.move_token_and_update_position(player_obj, 'q', steps)
                    self.check_stacking_or_kicking(player_obj, 'q')

                else:
                    if token_p_step_count < token_q_step_count or token_p_step_count == token_q_step_count and not token_p.is_finished():
                        self.move_token_and_update_position(player_obj, 'p', steps)
                        self.check_stacking_or_kicking(player_obj, 'p')
                    elif token_q_step_count < token_p_step_count and not token_q.is_finished():
                        self.move_token_and_update_position(player_obj, 'q', steps)
                        self.check_stacking_or_kicking(player_obj, 'q')

        return self.calculate_finishing_spaces()

    def validate_number_of_players(self, lst_of_players):
        """
        Raises error if use enters invalid number of players
        """
        if len(lst_of_players) <= 1 or len(lst_of_players) >= 5:
            raise InvalidNumberOfPlayersError

    def add_player(self, player):
        """
        Raises error if a player is assigned an invalid position
        """
        if player not in ['A', 'B', 'C', 'D']:
            raise ValueError
        player_obj = Player(player)
        self._players.append(player_obj)

    def move_token_and_update_position(self, player_obj, token_type, steps):
        """
        Takes a parameter representing the player object, token type, and steps
        Moves and updates a player's token position
        Does not return anything.
        """
        token = player_obj.get_tokens()[token_type]
        self.move_token(player_obj, token_type, steps)
        new_position_value = player_obj.get_board()[token.get_step_count() + 1]
        token.set_token_position(new_position_value)

    def calculate_finishing_spaces(self):
        """
        Takes no parameters
        Returns a list containing the current position of each Player's Tokens as strings
        Used at the end of the play_game method to easily return the intended information of that method
        """
        finishing_spaces = []
        for player_obj in self._players:
            for token_obj in player_obj.get_tokens().values():
                token_step_count = token_obj.get_step_count()
                finishing_spaces.append(str(player_obj.get_space_name(token_step_count)))
        return finishing_spaces

    def get_player_by_position(self, player_position):
        """
        Takes a parameter representing the player’s position as a string
        Returns the player object
        For an invalid string parameter, it will return "Player not found!"
        """
        for player in self._players:
            if player.get_player_position() == player_position:
                return player
        return 'Player not found!'
