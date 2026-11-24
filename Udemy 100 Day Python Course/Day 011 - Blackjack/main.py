from art import logo
from random import choice
from time import sleep
from subprocess import run


def deal_cards(player: str, num_of_cards: int) -> list[int]:
    cards_to_deal: list[int] = [choice(cards) for _ in range(num_of_cards)]
    fake_cards_to_deal: list[int | str] = [card if card != 11 and card != 1 else "Ace" for card in cards_to_deal[:]]

    for i, card in enumerate(cards_to_deal):
        if card == 10:
            fake_cards_to_deal[i] = choice([10, "King", "Queen", "Jack"])

    if player == "user":
        user_cards.extend(cards_to_deal)
        fake_user_cards.extend(fake_cards_to_deal)
    else:
        dealer_cards.extend(cards_to_deal)
        fake_dealer_cards.extend(fake_cards_to_deal)

    return cards_to_deal


def print_cards(player: str) -> None:
    cards_of_player_to_check = user_cards if player == "user" else dealer_cards
    fake_cards_of_player_to_check = fake_user_cards if player == "user" else fake_dealer_cards
    name = "Your" if player == "user" else "Dealer's"

    print(
        f"\n{name} cards: {", ".join([str(card) for card in fake_cards_of_player_to_check])}. {name} current score is: {sum(cards_of_player_to_check)}."
    )


def ask_to_hit_or_stand() -> str:
    while True:
        wants_another_card = input("\nEnter 'hit' or 'stand': ").lower()

        if wants_another_card in ["hit", "stand"]:
            break
        else:
            print("Please enter a valid answer.")

    return wants_another_card


def check_if_busted(player: str) -> bool:
    global wants_to_play_or_quit

    cards_of_player_to_check = user_cards if player == "user" else dealer_cards

    if sum(cards_of_player_to_check) > 21:
        if 11 in cards_of_player_to_check:
            cards_of_player_to_check[cards_of_player_to_check.index(11)] = 1
            check_if_busted(player)
        else:
            if player == "user":
                print_cards("user")
                print_cards("dealer")
                print_winner()

            return True

    return False


def ask_if_wants_to_play_again_or_quit() -> str:
    while True:
        wants_to_continue = input("\nEnter 'play again' or 'quit': ").lower()

        if wants_to_continue in ["play again", "quit"]:
            break
        else:
            print("Please enter a valid answer.")

    return wants_to_continue


def deal_dealers_cards() -> None:
    while sum(dealer_cards) < 17:
        print("Dealer hits.")

        deal_cards("dealer", 1)
        sleep(3)

        if check_if_busted("dealer"):
            print_cards("dealer")
            return

        print_cards("dealer")

    print("Dealer stands.")


def print_winner() -> None:
    global wants_to_play_or_quit

    user_sum = sum(user_cards)
    dealer_sum = sum(dealer_cards)

    if user_sum > 21:
        print(
            f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. You busted. You lose!"
        )
    elif dealer_sum > 21:
        print(
            f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. Dealer busted. You win!"
        )
    elif user_sum > dealer_sum:
        print(f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. You win!")
    elif user_sum < dealer_sum:
        print(f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. You lose!")
    elif user_sum == dealer_sum == 21 and len(user_cards) == 2 and len(dealer_cards) > 2:
        print(
            f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. You got a natural blackjack, but the dealer got a multi-card blackjack. You win!"
        )
    elif user_sum == dealer_sum == 21 and len(user_cards) == len(dealer_cards) == 2:
        print(
            f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. Both you and the dealer got a blackjack. It's a push!"
        )
    elif user_sum == dealer_sum == 21 and len(user_cards) > 2 and len(dealer_cards) == 2:
        print(
            f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. The dealer got a natural blackjack, but you got a multi-card blackjack. You lose!"
        )
    else:
        print(f"\nYou have a final score of {user_sum} and the dealer has a final score of {dealer_sum}. It's a push!")

    wants_to_play_or_quit = ask_if_wants_to_play_again_or_quit()


if __name__ == '__main__':
    cards: list[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    wants_to_play_or_quit: str = "play again"

    while wants_to_play_or_quit == "play again":
        run("clear")
        user_cards: list[int] = []
        fake_user_cards: list[int | str] = []
        dealer_cards: list[int] = []
        fake_dealer_cards: list[int | str] = []

        print(logo)

        deal_cards("user", 2)
        deal_cards("dealer", 2)

        if not check_if_busted("user"):
            print_cards("user")

        print(f"The dealer's first card is: {fake_dealer_cards[0]}")

        if not check_if_busted("user"):
            while True:
                hit_or_stand = ask_to_hit_or_stand()

                if hit_or_stand == "hit":
                    deal_cards("user", 1)

                    if check_if_busted("user"):
                        break

                    print_cards("user")
                else:
                    print_cards("dealer")
                    deal_dealers_cards()
                    print_winner()

                    break
        else:
            print_cards("dealer")
            print_winner()
