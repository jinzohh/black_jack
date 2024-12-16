import random
import time

def print_start_deck():
    # This function prints all 52 cards in the deck.
    # Defining each of the 52 cards in deck.
    deck = [
        '2 Clover', '2 Spades', '2 Heart', '2 Diamond',
        '3 Clover', '3 Spades', '3 Heart', '3 Diamond',
        '4 Clover', '4 Spades', '4 Heart', '4 Diamond',
        '5 Clover', '5 Spades', '5 Heart', '5 Diamond',
        '6 Clover', '6 Spades', '6 Heart', '6 Diamond',
        '7 Clover', '7 Spades', '7 Heart', '7 Diamond',
        '8 Clover', '8 Spades', '8 Heart', '8 Diamond',
        '9 Clover', '9 Spades', '9 Heart', '9 Diamond',
        '10 Clover', '10 Spades', '10 Heart', '10 Diamond',
        'J Clover', 'J Spades', 'J Heart', 'J Diamond',
        'Q Clover', 'Q Spades', 'Q Heart', 'Q Diamond',
        'K Clover', 'K Spades', 'K Heart', 'K Diamond',
        'A Clover', 'A Spades', 'A Heart', 'A Diamond',
    ]

    # Printing each of the 52 cards in deck.
    # The for loop is for better readability purpose.
    print("\nStarting cards in deck: ")
    
    n = 3
    for index, i in enumerate(deck):
        if index == n:
            n += 4
            print(i)
        else:
            print(i + ", ", end='')

    return deck

def shuffle(deck):
    # This function shuffles the cards then prints the shuffled cards.
    # Shuffling the cards.
    random.shuffle(deck)

    # Printing the cards in shuffled deck.
    print("\nShuffled cards in deck: ")

    n = 3
    for index, i in enumerate(deck):
        if index == n:
            n += 4
            print(i)
        else:
            print(i + ", ", end='')

    return deck

def draw_card(shuffled):
    # This function draws a card and returns the card and the value.
    # Drawing the card on top of the shuffled deck.
    drawn_card = shuffled[0]

    # Removing the top card from the shuffled deck since it is now drawn.
    shuffled.pop(0)

    return drawn_card, shuffled
    

def result(shuffled):
    # This function notifies the user of the game's results.
    # Initializing list variables to collect cards and numeric values in hand.
    drawn_hand = []
    val_list_1 = []
    val_list_2 = []
    
    # Running a loop until total value reaches 17 or greater.
    # Initializing variables for number of aces shown up and the total value.
    ace_cnt = 0
    total_val = 0
    while total_val < 17:
        # Calling draw_card() function to draw one card from the shuffled deck.
        drawn, shuffled_remain = draw_card(shuffled)

        # Recording the drawn cards.
        drawn_hand.append(drawn)

        # Assigning a numeric value to the drawn card.
        # Numeric values will be added to 2 different lists because of the different cases of Ace (value of 1 or 11).
        if drawn[0] == 'J' or drawn[0] == 'Q' or drawn[0] == 'K':
            val_list_1.append(10)
            val_list_2.append(10)
            
        elif drawn[0] == 'A':
            ace_cnt += 1

            # Different possibilities for values of Ace will be added to the two lists to be compared.
            if ace_cnt == 1:
                val_list_1.append(11)
                val_list_2.append(1)
            elif ace_cnt == 2:
                val_list_1.append(1)
                val_list_2.append(1)
            elif ace_cnt == 3:
                val_list_1.append(1)
                val_list_2.append(1)
            elif ace_cnt == 4:
                val_list_1.append(1)
                val_list_2.append(1)
            else:
                pass
                
        elif drawn[0] == '1' and drawn[1] == '0':
            val_list_1.append(10)
            val_list_2.append(10)
            
        else:
            val_list_1.append(int(drawn[0]))
            val_list_2.append(int(drawn[0]))

        # Summing up the values obtained from each draw.
        sum_1 = sum(val_list_1)
        sum_2 = sum(val_list_2)
        
        # If the sum values for the two lists equal each other, then it indicates that Ace was not drawn. So, either one of the sum value is the total value.
        # If the sum values for the two lists are different, then check whether sum_1 exceeds 21.
        # If sum_1 exceeds 21, then the sum_2, which has the lower value, will becomes the total value. If not, then sum_1 will becomes the total value.
        if sum_1 == sum_2:
            total_val = sum_1
        else:
            if sum_1 > 21:
                total_val = sum_2
            else:
                total_val = sum_1

        time.sleep(1)
        print("\nCard drawn: " + drawn + ", Total Value: " + str(total_val))
        time.sleep(1)

        # Notifying user of the total value and stop condition.
        if total_val >= 17:
            print("\nYour hand has a total value of " + str(total_val) + ", so no more cards will be drawn.")
        else:
            continue

    # Notifying user if hand is a black jack or bust.
    time.sleep(1)
    if total_val == 21:
        print("\nYou have a Black Jack! Winner Winner Chicken Dinner!")
    elif total_val > 21:
        print("\nIt's a bust! Better luck next time!")
    else:
        pass

    return drawn_hand, shuffled_remain

def sort_hand(hand_cards):
    # This function perform insertion sort to sort the cards in hand in increasing order.
    # Initializing list variables for ordering purpose.
    hand_convert = []
    sorted_hand = []

    # Replacing A, J, Q, K with numbers for ordering purpose and appending the numeric value to the hand_convert list.
    for i in hand_cards:
        if i[0] == 'A':
            hand_convert.append(1)
        elif i[0] == 'J':
            hand_convert.append(11)
        elif i[0] == 'Q':
            hand_convert.append(12)
        elif i[0] == 'K':
            hand_convert.append(13)
        elif i[0] == '1' and i[1] == '0':
            hand_convert.append(10)
        else:
            hand_convert.append(int(i[0]))
    
    # Performing Insertion Swap algorithm.
    for j in range(1, len(hand_convert)):
        w = j
        while w > 0 and hand_convert[w-1] > hand_convert[w]:
            hand_convert[w], hand_convert[w-1] = hand_convert[w-1], hand_convert[w]
            w = w - 1
    
    # Assigning the original card values to the numbers in hand_convert list.
    for index, w in enumerate(hand_convert):
        # if w == 1, then it corresponds to Ace. Append the Ace from hand_cards to the new sorted_hand list.
        # if w == 11, then it corresponds to Jack. Append the Jack from hand_cards to the new sorted_hand list.
        # if w == 12, then it corresponds to Queen. Append the Queen from hand_cards to the new sorted_hand list.
        # if w == 13, then it corresponds to King. Append the King from hand_cards to the new sorted_hand list.
        # For all others, then it corresponds to numbered cards. Append the numbered card from hand_cards to the new sorted_hand list.
        if w == 1:
            for q in hand_cards:
                if q[0] == 'A':
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                else:
                    continue
                
        elif w == 11:
            for q in hand_cards:
                if q[0] == 'J':
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                else:
                    continue
                
        elif w == 12:
            for q in hand_cards:
                if q[0] == 'Q':
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                else:
                    continue
                
        elif w == 13:
            for q in hand_cards:
                if q[0] == 'K':
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                else:
                    continue
                
        else:
            for q in hand_cards:
                if w == 10 and q[0] + q[1] == str(w):
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                elif q[0] == str(w):
                    sorted_hand.append(q)
                    hand_cards.remove(q)
                    break
                else:
                    continue
                
    # Printing the sorted hand.
    time.sleep(1)
    print("\nMy sorted hand: ")
    for z in sorted_hand:
        if sorted_hand.index(z) == len(sorted_hand) - 1:
            print(z)
        else:
            print(z + ", ", end='')

def print_end_deck(remains):
    # This function prints the remaining cards in the deck.
    # Printing the remaining cards in deck.
    time.sleep(1)
    print("\nRemaining cards in deck: ")
    
    n = 3
    for index, i in enumerate(remains):
        if index == n:
            n += 4
            print(i)
        elif index == len(remains) - 1:
            print(i)
        else:
            print(i + ", ", end='')
    
def black_jack():
    # This is the main function.
    # Inputfield to play the game or not.
    res = input("Play Black Jack? [(y)es or (n)o]: ")

    # Validate response by checking for 'y'.
    if 'y' in res:
        play_blackjack = True
    else:
        play_blackjack = False
        print("\nEnding program...")

    # Running a loop to continue playing until user quits.
    while play_blackjack:
        # Calling print_start_deck() function to print all 52 cards in deck.
        card_deck = print_start_deck()

        # Calling shuffle() function to randomize the cards in the deck and then printing the cards.
        time.sleep(1)
        print("\nShuffling cards...")
        time.sleep(2)
        shuffled_deck = shuffle(card_deck)

        # Calling result() function to find out the result of the game.
        hand, remaining_deck = result(shuffled_deck)

        # Calling sort_hand() function to sort the cards in hand (insertion sort algorithm).
        time.sleep(1)
        sort_hand(hand)

        # Calling print_end_deck() function to print the remaining cards in deck.
        time.sleep(1)
        print_end_deck(remaining_deck)

        # Asking the user if he/she would like to keep playing or not.
        res_2 = input("\nPlay again? [(y)es or (n)o]: ")

        if 'y' in res_2:
            play_blackjack = True
            print("\nRestarting Black Jack...")
        else:
            play_blackjack = False
            print("\nEnding program...")

if __name__ == "__main__":
    black_jack()