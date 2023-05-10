from lib import shuffle_list
from lib import player_guess
from lib import check_guess

# INITAL LIST
mylist=['','O','']
#SHUFFLE LIST
mixed_list=shuffle_list(mylist)
#PLAYER GUESS
guess=player_guess()
#CHECK GUESS
check_guess(mixed_list,guess)