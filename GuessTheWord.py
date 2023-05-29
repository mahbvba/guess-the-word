import os
def main():
  max_guesses = 8
  number_of_guesses = 0
  is_player_1_active = True
  active_player = ""
  player_won_turn = False
  player_1_name = input("Enter Player 1's name (name will default to Player 1 if none is entered ): ")
  player_1_name = player_1_name if player_1_name else "Player 1"
  player_2_name = input("Enter Player 2's name (name will default to Player 2 if none is entered ): ")
  player_2_name = player_2_name if player_2_name else "Player 2"
  # Stores the Score of the game in the array, i.e. scoreArray[0] will hold the score for player1
  # And scoreArray[1] will hold the score for player2
  scoreArray = [0,0]
  while(True):
    player_won_turn = False
    active_player = getActivePlayer(is_player_1_active,player_1_name,player_2_name)
    print("It's " + active_player + " 's turn")
    word = list(input(active_player + " enter your word... "))
    output_word = getFuzzyWord(word)
    os.system('clear')
    number_of_guesses = 0
    is_player_1_active = not is_player_1_active
    active_player = getActivePlayer(is_player_1_active,player_1_name,player_2_name)
    # word = input(active_player + " please enter your word")
    # Turn
    while(number_of_guesses < max_guesses):
      guess = input(active_player + " Enter your guess...")
      number_of_guesses = number_of_guesses + 1
      if(guess in word):
        print(updateOutput(output_word,word,guess))
      if(list(guess) == word or word == output_word):
        print('Congratulations, ' + active_player + ' has won the turn.')
        incrementScore(is_player_1_active, scoreArray)
        player_won_turn = True
        break;
    if(not player_won_turn):
      print(active_player + ' did not win this turn. Better luck next time!')
    is_player_1_active = not is_player_1_active
    output_word = getFuzzyWord(word)
    if(not player_won_turn):
      incrementScore(is_player_1_active,scoreArray)
    print(getScoreAsString(scoreArray, player_1_name,player_2_name))
    is_player_1_active = not is_player_1_active
    active_player = getActivePlayer(is_player_1_active,player_1_name,player_2_name)

# if output is **** and word is toad and guess is a, then the function would return **a*
def updateOutput(output,  word,  guess):
  for i in range( len(word)):
    if(word[i] == guess):
      output[i] = guess
  return output

# Returns list of asterisks from list of characters
def getFuzzyWord(input):
  copy_of_input = input.copy()
  for i in range (len(copy_of_input)):
    copy_of_input[i] = '*'
  return copy_of_input

def getActivePlayer(is_is_player_1_active, player_1_name,player_2_name):
  if(is_is_player_1_active):
    return player_1_name
  else:
    return player_2_name

def getScoreAsString(scoreArray, player_1_name,player_2_name):
  if(len(scoreArray) != 2):
    return ("Error: ScoreArray should have 2 elements, one for each player. Has " + len(scoreArray) + "elements.")
  return (player_1_name +" score: " + str(scoreArray[0]) + " pts | " + player_2_name + " score: " + str(scoreArray[1]) + " pts")

def incrementScore(is_player_1_active, scoreArray):
  if(len(scoreArray) != 2):
    return ("Error: ScoreArray should have 2 elements, one for each player. Has " + len(scoreArray) + "elements.")
  if(is_player_1_active):
    scoreArray[0] = scoreArray[0] + 1
  else:
    scoreArray[1] = scoreArray[1] + 1

main()