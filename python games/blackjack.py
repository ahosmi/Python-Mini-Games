import random
import tkinter as tk
from tkinter import messagebox

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def blackjack():
    player_cards = []
    dealer_cards = []

    def hit():
        player_cards.append(deal_card())
        player_score_label.config(text=f"Your cards: {player_cards}, score: {calculate_score(player_cards)}")
        if calculate_score(player_cards) > 21:
            messagebox.showinfo("Result", "Busted! You lose!")
            reset()

    def stand():
        while calculate_score(dealer_cards) < 17:
            dealer_cards.append(deal_card())
        dealer_score_label.config(text=f"Dealer's cards: {dealer_cards}, score: {calculate_score(dealer_cards)}")

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if dealer_score > 21:
            messagebox.showinfo("Result", "Dealer busted! You win!")
        elif player_score > dealer_score:
            messagebox.showinfo("Result", "You win!")
        elif player_score < dealer_score:
            messagebox.showinfo("Result", "You lose!")
        else:
            messagebox.showinfo("Result", "It's a draw!")
        reset()

    def reset():
        player_cards.clear()
        dealer_cards.clear()
        player_score_label.config(text="")
        dealer_score_label.config(text="")
        player_cards.append(deal_card())
        player_cards.append(deal_card())
        player_score_label.config(text=f"Your cards: {player_cards}, score: {calculate_score(player_cards)}")
        dealer_cards.append(deal_card())
        dealer_score_label.config(text=f"Dealer's card: {dealer_cards[0]}")

    root = tk.Tk()
    root.title("Blackjack")

    player_frame = tk.Frame(root)
    player_frame.pack()

    player_score_label = tk.Label(player_frame, text="")
    player_score_label.pack()

    dealer_frame = tk.Frame(root)
    dealer_frame.pack()

    dealer_score_label = tk.Label(dealer_frame, text="")
    dealer_score_label.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    hit_button = tk.Button(button_frame, text="Hit", command=hit)
    hit_button.grid(row=0, column=0)

    stand_button = tk.Button(button_frame, text="Stand", command=stand)
    stand_button.grid(row=0, column=1)

    reset()

    root.mainloop()

blackjack()
