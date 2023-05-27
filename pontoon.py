import pygame
import random
 
pygame.init()
 
display_width = 1200
display_height = 800
 
black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
red = (200, 0, 0)
bright_green = (0, 255, 0)
green = (0, 200, 0)
bg_colour = (0,120,0)
 
block_color = (53,115,255)

hand = [None, None, None, None, None]
dealer = [None, None, None, None, None]

in_game = False
current_deck = []
player_stuck = False
player_total = 0
dealer_total = 0
player_bust = False
player_won = False
dealer_bust = False
dealer_won = False
player_score = 0
dealer_score = 0
player_stake = 5
player_funds = 100
draw = False
hand_over = False
first_hand = True
player_ace_count = 0
dealer_ace_count = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pontoon by Andy G')

def create_shoe():
    global current_deck
    file_path = 'C:\\Users\\andyg\\Documents\\Data Science Skills Boot Camp\\Python Projects\\Pontoon\\images\\'
    deck=[(11,file_path + 'ace_of_clubs.png'), (11,file_path + 'ace_of_hearts.png'), (11,file_path + 'ace_of_spades.png'), (11,file_path + 'ace_of_diamonds.png'),
          (2,file_path + '2_of_clubs.png'), (2,file_path + '2_of_hearts.png'), (2,file_path + '2_of_spades.png'), (2,file_path + '2_of_diamonds.png'),
          (3,file_path + '3_of_clubs.png'), (3,file_path + '3_of_hearts.png'), (3,file_path + '3_of_spades.png'), (3,file_path + '3_of_diamonds.png'),
	      (4,file_path + '4_of_clubs.png'), (4,file_path + '4_of_hearts.png'), (4,file_path + '4_of_spades.png'), (4,file_path + '4_of_diamonds.png'),
	      (5,file_path + '5_of_clubs.png'), (5,file_path + '5_of_hearts.png'), (5,file_path + '5_of_spades.png'), (5,file_path + '5_of_diamonds.png'),
	      (6,file_path + '6_of_clubs.png'), (6,file_path + '6_of_hearts.png'), (6,file_path + '6_of_spades.png'), (6,file_path + '6_of_diamonds.png'),
	      (7,file_path + '7_of_clubs.png'), (7,file_path + '7_of_hearts.png'), (7,file_path + '7_of_spades.png'), (7,file_path + '7_of_diamonds.png'),
	      (8,file_path + '8_of_clubs.png'), (8,file_path + '8_of_hearts.png'), (8,file_path + '8_of_spades.png'), (8,file_path + '8_of_diamonds.png'),
	      (9,file_path + '9_of_clubs.png'), (9,file_path + '9_of_hearts.png'), (9,file_path + '9_of_spades.png'), (9,file_path + '9_of_diamonds.png'),
	      (10,file_path + '10_of_clubs.png'), (10,file_path + '10_of_hearts.png'), (10,file_path + '10_of_spades.png'), (10,file_path + '10_of_diamonds.png'),
          (10,file_path + 'jack_of_clubs.png'), (10,file_path + 'jack_of_hearts.png'), (10,file_path + 'jack_of_spades.png'), (10,file_path + 'jack_of_diamonds.png'),
          (10,file_path + 'queen_of_clubs.png'), (10,file_path + 'queen_of_hearts.png'), (10,file_path + 'queen_of_spades.png'), (10,file_path + 'queen_of_diamonds.png'),
          (10,file_path + 'king_of_clubs.png'), (10,file_path + 'king_of_hearts.png'), (10,file_path + 'king_of_spades.png'), (10,file_path + 'king_of_diamonds.png')]

    #create a shoe with 4 decks
    current_deck = deck.copy()
    current_deck.extend(current_deck)
    current_deck.extend(current_deck)

def reset_game():
    global hand
    global dealer

    global in_game
    global player_stuck
    global player_total
    global dealer_total
    global player_bust
    global player_won
    global dealer_bust
    global dealer_won
    global player_score
    global dealer_score
    global player_stake
    global draw
    global hand_over
    global first_hand
    global player_ace_count
    global dealer_ace_count

    hand = [None, None, None, None, None]
    dealer = [None, None, None, None, None]

    in_game = False
    player_stuck = False
    player_total = 0
    dealer_total = 0
    player_bust = False
    player_won = False
    dealer_bust = False
    dealer_won = False
    player_score = 0
    dealer_score = 0
    player_stake = 5
    draw = False
    hand_over = False
    first_hand = True
    player_ace_count = 0
    dealer_ace_count = 0

def deal():

    #only deal if not already in a game and player has not stuck
    global in_game
    global player_stuck
    global player_score
    global dealer_score
    global first_hand
    global player_won
    global player_ace_count
    global dealer_ace_count

    if not in_game and not player_stuck:
        reset_game()	
        #generate a random number to select next card
        next_card = random.randrange(0, len(current_deck))
        #first card for player
        curr_card = current_deck[next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        hand[0] = image
        current_deck.pop(next_card)
        player_score += curr_card[0]
        if curr_card[0] == 11:
            player_ace_count += 1
        #first card for dealer
        next_card = random.randrange(0, len(current_deck))
        curr_card = current_deck[next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        dealer[0] = image
        current_deck.pop(next_card)
        dealer_score += curr_card[0]
        if curr_card[0] == 11:
            dealer_ace_count += 1
        #second card for player
        next_card = random.randrange(0, len(current_deck))
        curr_card = current_deck[next_card]
        image = pygame.image.load(curr_card[1])
        image = pygame.transform.scale(image, (100, 150))
        hand[1] = image
        current_deck.pop(next_card)
        player_score += curr_card[0]
        if curr_card[0] == 11:
            player_ace_count += 1

        if player_score == 21:
            player_won = True
        else:
            in_game = True

def twist():

    #only twist if in a game
    global in_game
    global player_stuck
    global player_score
    global player_bust
    global player_funds
    global hand_over
    global player_ace_count

    if in_game and not player_stuck:
        i=0
        while i < 5:
            if hand[i] == None:
                next_card = random.randrange(0, len(current_deck))
                curr_card = current_deck[next_card]
                image = pygame.image.load(curr_card[1])
                image = pygame.transform.scale(image, (100, 150))
                hand[i] = image
                current_deck.pop(next_card)
                player_score += curr_card[0]
                if curr_card[0] == 11:
                    player_ace_count += 1
                break
            i+=1	

        if player_score > 21:
            if player_ace_count > 0:
                player_ace_count -=1
                player_score -= 10
            else:
                player_bust = True
                player_funds -= player_stake
                hand_over = True
                in_game = False
                player_stuck = False

def stick():

    #only stick if in a game
    global in_game
    global player_stuck
    global dealer_score
    global dealer_bust
    global player_funds
    global draw
    global player_won
    global dealer_won
    global hand_over
    global dealer_ace_count

    if in_game and not hand_over:
        player_stuck = True
        i=0
        while i < 5:
            if dealer[i] == None:
                next_card = random.randrange(0, len(current_deck))
                curr_card = current_deck[next_card]
                image = pygame.image.load(curr_card[1])
                image = pygame.transform.scale(image, (100, 150))
                dealer[i] = image
                current_deck.pop(next_card)
                dealer_score += curr_card[0]
                if curr_card[0] == 11:
                    dealer_ace_count += 1

                if dealer_score > 21:
                    if dealer_ace_count > 0:
                        dealer_ace_count -= 1
                        dealer_score -= 10
                if dealer_score >= 17:
                    break
            i+=1
        if dealer_score > 21:
            if dealer_ace_count > 0:
                dealer_ace_count -= 1
                dealer_score -= 10
            else:
                dealer_bust = True
                player_funds += player_stake
        elif dealer_score == player_score:
            draw = True
        elif dealer_score > player_score:
            dealer_won = True
            player_funds -= player_stake
        else:
            player_won = True
            player_funds += player_stake

        hand_over = True
        in_game = False
        player_stuck = False



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(x,y,text,textSize):
    messageText = pygame.font.Font('freesansbold.ttf',textSize)
    TextSurf, TextRect = text_objects(text, messageText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)

def button(msg,x,y,w,h,ic,ac,action=None):
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
 
def playerBust():
    global player_bust

    message_display(600,480,"You bust!",70)
    player_bust = True

def dealerBust():
    global dealer_bust
    
    message_display(600,50,"Dealer bust!",70)
    dealer_bust = True

def playerWon():
    global player_won

    message_display(600,480,"You won!",70)
    player_won = True

def dealerWon():
    global dealer_won
    
    message_display(600,50,"Dealer won!",70)
    dealer_won = True

def game_drawn():
    global draw

    message_display(600,480,"You Drew!",70)
    draw = True

def quitgame ():
    pygame.quit()
    quit()    

def game_loop():

    gameExit = False
    global player_bust
    global dealer_bust
    global player_won
    global dealer_won
    global draw
    global current_deck
 
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(current_deck) < 10:
            create_shoe()

        gameDisplay.fill(bg_colour)

        message_display((display_width/2),(display_height/2),"Pontoon!",115)
        message_display(180,200,"Dealer",70)
        message_display(220,600,"You",70)
        message_display(1000,700,"Stake: £" + str(player_stake),20)
        message_display(1010,730,"Funds: £" + str(player_funds),20)
        message_display(1010,760,"Cards: " + str(len(current_deck)),20)

        button("Deal",430,750,50,25,green,bright_green,deal)
        button("Twist",530,750,50,25,green,bright_green,twist) 
        button("Stick",630,750,50,25,green,bright_green,stick)
        button("Quit",730,750,50,25,green,bright_green,quitgame)

        if dealer_bust:
            playerWon()
            dealerBust()

        if player_bust:
            playerBust()
            dealerWon()

        if player_won:
            playerWon()

        if dealer_won:
            dealerWon()

        if draw:
            game_drawn()

        index = 0
        card_x = [330, 440, 550, 660, 770]
        for x in hand:
            if x != None:
                rect = x.get_rect()
                rect.x = card_x[index]
                rect.y = 550
                gameDisplay.blit(x, rect)
                index += 1
        index = 0
        card_x = [330, 440, 550, 660, 770]
        for x in dealer:
            if x != None:
                rect = x.get_rect()
                rect.x = card_x[index]
                rect.y = 100
                gameDisplay.blit(x, rect)
                index += 1
        pygame.display.update()

game_loop()
pygame.quit()
quit()