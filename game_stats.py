

class GameStats():
    '''Track statistics for the game.'''

    def __init__(self, settings):
        '''Initialize stats.'''
        self.settings = settings
        self.reset_stats()
    
    def reset_stats(self):
        '''Initialize statistics that can change during the game.'''
        self.snails_left = self.settings.snail_limit