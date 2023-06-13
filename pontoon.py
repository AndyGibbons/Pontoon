"""----------------------------------------------------------------------------
Pontoon!
========

This is a single-player version of Pontoon (aka Blackjack or 21).

How to play
===========

When you run the game, you start playing by clicking on the "Deal" button. 
You will be dealt your first two cards, and the dealer their first. You
then choose how many more cards you wish to take, if any, up to 5 cards.
Be careful not to score more than 21 with your cards (picture cards have a 
value of 10,Aces either 1 or 11, and other cards their numeric value) or you 
will bust and the dealer will win without having to take anymore cards. When 
you whoose to stick with the cards you have, the dealer takes cards trying to 
beat you. The dealer must stick on 17 or above, but cannot stick lower than 
that.

The shoe (set of cards used in the game) contains four packs of cards, in case 
you fancy trying your hand at card counting. 
When the number of cards left in the shoe drops to under 10, the game creates 
a new shoe. You also start with £100 and stake £5 on each hand. The game allows
you to go into debt, so be careful not to lose your shirt!

Author: Andy Gibbons
Latest update: June 2023
----------------------------------------------------------------------------"""
import pygame
import random
import os
 
pygame.init()

# Dictionary used to store the state of the game
gameState = {
    "hand" : [None, None, None, None, None],    # player's cards
    "dealer" : [None, None, None, None, None],  # dealer's cards 

    "in_game" : False,                     # a hand is being played  
    "current_deck" : [],                   # The current shoe of cards
    "player_stuck" : False,                # Player chose to stick
    "player_bust" : False,                 # The player scored > 21
    "player_won" : False,                  # Yay!
    "dealer_bust" : False,                 # The dealer scored > 21
    "dealer_won" : False,                  # Boo!
    "player_score" : 0,                    # Player's score in current hand
    "dealer_score" : 0,                    # Dealer's score in current hand
    "player_stake" : 5,                    # The amount of each bet
    "player_funds" : 100,                  # The player's starting pot
    "draw" : False,                        # The hamd is drawn
    "hand_over" : False,                   # The hand is over
    "player_ace_count" : 0,                # number of aces in player's hand
    "dealer_ace_count" : 0}                # number of aces in dealer's hand
 
# Set up the display for the game
display_width = 1200
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pontoon by Andy Gibbons')

# define colours to use in the game display
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
red = (200, 0, 0)
bright_green = (0, 255, 0)
green = (0, 200, 0)
bg_colour = (0,120,0)
block_color = (53,115,255)

"""----------------------------------------------------------------------------
user-defined functions
----------------------------------------------------------------------------"""

def create_shoe():
    """ create the cards for the game made of four packs of playing cards"""
    global gameState

    #find path to the game's directory
    dir = os.path.dirname(__file__)

    # construct path to card image files
    file_path = os.path.join(dir, "images")
    
    # list containing the card images and the card numerical values
    
    # add aces and picture cards to the deck
    deck = [(11,file_path + '\\ace_of_clubs.png'), 
          (11,file_path + '\\ace_of_hearts.png'), 
          (11,file_path + '\\ace_of_spades.png'), 
          (11,file_path + '\\ace_of_diamonds.png'),
          (10,file_path + '\\jack_of_clubs.png'), 
          (10,file_path + '\\jack_of_hearts.png'), 
          (10,file_path + '\\jack_of_spades.png'), 
          (10,file_path + '\\jack_of_diamonds.png'),
          (10,file_path + '\\queen_of_clubs.png'), 
          (10,file_path + '\\queen_of_hearts.png'), 
          (10,file_path + '\\queen_of_spades.png'), 
          (10,file_path + '\\queen_of_diamonds.png'),
          (10,file_path + '\\king_of_clubs.png'), 
          (10,file_path + '\\king_of_hearts.png'), 
          (10,file_path + '\\king_of_spades.png'), 
          (10,file_path + '\\king_of_diamonds.png')]
    
    # add remaining cards to the deck
    for value in range(2,11):
        deck.append((value,file_path + '\\' + str(value) + '_of_clubs.png')) 
        deck.append((value,file_path + '\\' + str(value) + '_of_hearts.png')) 
        deck.append((value,file_path + '\\' + str(value) + '_of_spades.png')) 
        deck.append((value,file_path + '\\' + str(value) + '_of_diamonds.png'))


    #create a shoe with 4 decks
    gameState["current_deck"] = deck.copy()
    gameState["current_deck"].extend(gameState["current_deck"])
    gameState["current_deck"].extend(gameState["current_deck"])

def reset_hand():
    """ reset game state values used playing a hand to use in a new hand """
    global gameState

    gameState["hand"] = [None, None, None, None, None]   
    gameState["dealer"] = [None, None, None, None, None] 
    gameState["in_game"] = False
    gameState["player_stuck"] = False
    gameState["player_bust"] = False
    gameState["player_won"] = False
    gameState["dealer_bust"] = False
    gameState["dealer_won"] = False
    gameState["player_score"] = 0
    gameState["dealer_score"] = 0
    gameState["player_stake"] = 5
    gameState["draw"] = False
    gameState["hand_over"] = False
    gameState["player_ace_count"] = 0
    gameState["dealer_ace_count"] = 0
    
def deal():
    """ deal cards to start a new hand """
    global gameState
    
    #only deal if not already in a game and player has not stuck
    if not gameState["in_game"] and not gameState["player_stuck"]:
        
        reset_hand()

        #generate a random number to select next card
        next_card = random.randrange(0, len(gameState["current_deck"]))
        #first card for player
        curr_card = gameState["current_deck"][next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        gameState["hand"][0] = image
        gameState["current_deck"].pop(next_card)
        gameState["player_score"] += curr_card[0]
        if curr_card[0] == 11:
            gameState["player_ace_count"] += 1
        #first card for dealer
        next_card = random.randrange(0, len(gameState["current_deck"]))
        curr_card = gameState["current_deck"][next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        gameState["dealer"][0] = image
        gameState["current_deck"].pop(next_card)
        gameState["dealer_score"] += curr_card[0]
        if curr_card[0] == 11:
            gameState["dealer_ace_count"] += 1
        #second card for player
        next_card = random.randrange(0, len(gameState["current_deck"]))
        curr_card = gameState["current_deck"][next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        gameState["hand"][1] = image
        gameState["current_deck"].pop(next_card)
        gameState["player_score"] += curr_card[0]
        if curr_card[0] == 11:
            gameState["player_ace_count"] += 1

        if gameState["player_score"] == 21:
            gameState["player_won"] = True
        else:
            gameState["in_game"] = True


def twist():
    """ player takes another card """
    global gameState

    #only twist if in a game
    if gameState["in_game"] and not gameState["player_stuck"]:
        i=0
        while i < 5:
            if gameState["hand"][i] == None:
                next_card = random.randrange(0, len(gameState["current_deck"]))
                curr_card = gameState["current_deck"][next_card]
                image = pygame.image.load(curr_card[1])
                image = pygame.transform.scale(image, (100, 150))
                gameState["hand"][i] = image
                gameState["current_deck"].pop(next_card)
                gameState["player_score"] += curr_card[0]
                if curr_card[0] == 11:
                    gameState["player_ace_count"] += 1
                break
            i += 1	

        if gameState["player_score"] > 21:
            if gameState["player_ace_count"] > 0:
                gameState["player_ace_count"] -= 1
                gameState["player_score"] -= 10
            else:
                gameState["player_bust"] = True
                gameState["player_funds"] -= gameState["player_stake"]
                gameState["hand_over"] = True
                gameState["in_game"] = False
                gameState["player_stuck"] = False

def stick():
    """ player choses to stick with their current cards """
    global gameState

    #only stick if in a game
    if gameState["in_game"] and not gameState["hand_over"]:
        gameState["player_stuck"] = True
        i=0
        while i < 5:
            if gameState["dealer"][i] == None:
                next_card = random.randrange(0, len(gameState["current_deck"]))
                curr_card = gameState["current_deck"][next_card]
                image = pygame.image.load(curr_card[1])
                image = pygame.transform.scale(image, (100, 150))
                gameState["dealer"][i] = image
                gameState["current_deck"].pop(next_card)
                gameState["dealer_score"] += curr_card[0]
                if curr_card[0] == 11:
                    gameState["dealer_ace_count"] += 1

                if gameState["dealer_score"] > 21:
                    if gameState["dealer_ace_count"] > 0:
                        gameState["dealer_ace_count"] -= 1
                        gameState["dealer_score"] -= 10
                if gameState["dealer_score"] >= 17:
                    break
            i+=1
        if gameState["dealer_score"] > 21:
            if gameState["dealer_ace_count"] > 0:
                gameState["dealer_ace_count"] -= 1
                gameState["dealer_score"] -= 10
            else:
                gameState["dealer_bust"] = True
                gameState["player_funds"] += gameState["player_stake"]
        elif gameState["dealer_score"] == gameState["player_score"]:
            gameState["draw"] = True
        elif gameState["dealer_score"] > gameState["player_score"]:
            gameState["dealer_won"] = True
            gameState["player_funds"] -= gameState["player_stake"]
        else:
            gameState["player_won"] = True
            gameState["player_funds"] += gameState["player_stake"]

        gameState["hand_over"] = True
        gameState["in_game"] = False
        gameState["player_stuck"] = False

def message_display(x,y,text,textSize):
    """ display given text centred on x, y values given """
    messageText = pygame.font.Font('freesansbold.ttf',textSize)
    textSurf = messageText.render(text, True, black)
    textRect = textSurf.get_rect()
    textRect.center = (x,y)
    gameDisplay.blit(textSurf, textRect)

def button(msg,x,y,w,h,ic,ac,action=None):
    """ create button at given x,y position to perform given action """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()    
            pygame.event.wait(pygame.MOUSEBUTTONUP)    
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    message_display((x+(w/2)), (y+(h/2)),msg,15)
 
def quitgame ():
    pygame.quit()
    quit()    

def game_loop():
    """ main game loop """

    global gameState

    while True: # loop until player quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # create a new show of cards if less than 10 cards left
        if len(gameState["current_deck"]) < 10:
            create_shoe()

        # create the game display
        gameDisplay.fill(bg_colour)

        message_display((display_width/2),(display_height/2),"Pontoon!",115)
        message_display(180,200,"Dealer",70)
        message_display(220,600,"You",70)
        message_display(1000,700,"Stake: £" 
                        + str(gameState["player_stake"]),20)
        message_display(1010,730,"Funds: £" 
                        + str(gameState["player_funds"]),20)
        message_display(1010,760,"Cards: " 
                        + str(len(gameState["current_deck"])),20)

        # create buttons to call main game functions
        button("Deal",430,750,50,25,green,bright_green,deal)
        button("Twist",530,750,50,25,green,bright_green,twist) 
        button("Stick",630,750,50,25,green,bright_green,stick)
        button("Quit",730,750,50,25,green,bright_green,quitgame)

        # check the current game state and display appropriate message
        if gameState["player_won"]:
            message_display(600,480,"You won!",70)

        elif gameState["dealer_bust"]:
            message_display(600,480,"You won!",70)
            message_display(600,50,"Dealer bust!",70)

        elif gameState["player_bust"]:
            message_display(600,480,"You bust!",70)
            message_display(600,50,"Dealer won!",70)

        elif gameState["dealer_won"]:
            message_display(600,50,"Dealer won!",70)

        elif gameState["draw"]:
                message_display(600,480,"You Drew!",70)

        index = 0

        # Draw the player's hand on display
        card_x = [330, 440, 550, 660, 770]
        for x in gameState["hand"]:
            if x != None:
                rect = x.get_rect()
                rect.x = card_x[index]
                rect.y = 550
                gameDisplay.blit(x, rect)
                index += 1

        index = 0

        # Draw the dealer's hand on display
        card_x = [330, 440, 550, 660, 770]
        for x in gameState["dealer"]:
            if x != None:
                rect = x.get_rect()
                rect.x = card_x[index]
                rect.y = 100
                gameDisplay.blit(x, rect)
                index += 1

        # update the display
        pygame.display.update()

game_loop()
pygame.quit()
quit()