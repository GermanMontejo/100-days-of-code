from unittest.mock import patch
import random
from guess import get_random_number, Game

@patch.object(random, 'randint')