from django.db import models

class GameBoard(models.Model):
    board = models.CharField(max_length=9, default='-'*9)
    current_player = models.CharField(max_length=1, default='X')

    def __str__(self):
        return f"Game #{self.pk}"
