import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

card_list = making_card_list()


# 하나의 카드를 뽑는 함수
def select_one_card(card_list):
    return card_list.pop(
		card_list.index(
	        random.choice(card_list)))


# 왼쪽이 승리하면 True 를 반환하는 함수
def is_win(left_card: tuple, right_card: tuple) -> bool:
    card_values = {'J' : 11, 'Q' : 12, 'K': 13, 'A': 14}
    # shape_to_value_dict = {'spade': 0.4, 'diamond': 0.3, 'heart': 0.2, 'clover': 0.1}
	# 각 카드의 숫자가 J Q K A 인 경우에 숫자값으로 바꿔준다
    left_value = card_values[left_card[1]] if left_card[1] in card_values else left_card[1]
    right_value = card_values[right_card[1]] if right_card[1] in card_values else right_card[1]
    
    if left_value > right_value:
        return True
    elif right_value > left_value:
        return False
    else:
        shape_to_value_dict = {'spade': 4, 'diamond': 3, 'heart': 2, 'clover': 1}
	    
        left_value2 = shape_to_value_dict[left_card[0]]
        right_value2 = shape_to_value_dict[right_card[0]]

        if left_value2 > right_value2:
              return True
        else:
              return False
        


def play_game(need_wins = 6) -> str:
    trump_card_list = making_card_list()

    player1_wins = 0
    player2_wins = 0

    while not (player1_wins == need_wins or player2_wins == need_wins):
        # 카드를 섞어준다
        random.shuffle(trump_card_list)
        player1_card = select_one_card(trump_card_list)
        player2_card = select_one_card(trump_card_list)
        if is_win(player1_card, player2_card):
            player1_wins += 1
            winner = 'player1'
        else:
            player2_wins += 1
            winner = 'player2'

        print(f'{player1_card} {player2_card} {winner} win!')

    final_score = f'{player1_wins}:{player2_wins}'

    return final_score + ' player1 win' if player1_wins > player2_wins else ' player2 win'


print(play_game(6))