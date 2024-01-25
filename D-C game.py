#ماژول ها
import random # برای استفاده کردن از ایتم رندوم
import os     # برای پاک کردن ترمینال

# تابع برای دریافت اطلاعات از کاربر
def input_get():
    default_repeat_count = random.randint(5, 10)
    default_rounds_per_game = random.randint(3, 6)
    
    print("------------------------------------")
    print(f"WELCOME TO  D/C GAME...\nCreator GITHUB/eh3an-code...LETS DO IT!")
    print("------------------------------------")
    
    use_default = input(f"this game has random game&round that ({default_repeat_count} games, {default_rounds_per_game} rounds per game). Is it good? (y/n): ").lower()

    if use_default == 'y':
        print("------------------------------------")
        print(f"This game will have {default_repeat_count} games, and each game will have {default_rounds_per_game} rounds.")
        print("------------------------------------")
        print("GHVANIN:\n agar har do ghaeichi = 1 point for both\n agar har do kaghaz = 3 point for both\n agar motafavet bood barandeh ghaeichi = 5 point for D(gheichi)\n")
        print("------------------------------------")
        return default_repeat_count, default_rounds_per_game
    else:
        custom_repeat_count = int(input("Enter the desired number of games: "))
        custom_rounds_per_game = int(input("Enter the desired number of rounds per game: "))
        print("------------------------------------")
        print(f"This game will have {custom_repeat_count} games, and each game will have {custom_rounds_per_game} rounds.")
        print("------------------------------------")
        print("GHVANIN:\n agar har do ghaeichi = 1 point for both\n agar har do kaghaz = 3 point for both\n agar motafavet bood barandeh ghaeichi = 5 point for D(gheichi)\n")
        print("------------------------------------")
        return custom_repeat_count, custom_rounds_per_game

# تابع برای اجرای بازی
def game_play(player1_choice, player2_choice):
    
    if player1_choice == 'D' and player2_choice == 'D':
        return 1, 1  # هرکدام 1 سکه طلایی می‌گیرند
    elif player1_choice == 'C' and player2_choice == 'C':
        return 3, 3  # هرکدام 3 سکه طلایی می‌گیرند
    elif player1_choice == 'C' and player2_choice == 'D':
        return 0, 5  # برنده که قیچی اورده 5 امتیاز 
    elif player1_choice == 'D' and player2_choice == 'C':
        return 5, 0  # برنده که قیچی اورده 5 امتیاز 

# تابع برای پیدا کردن برنده
def winner_find(player1_score, player2_score):
    if player1_score > player2_score:
        return "player1 winner!"
    elif player1_score < player2_score:
        return "player2 winner!"
    else:
        return "equaled!"

# تابع نمایش نتایج بازی تا اون لحظه
def result_print(round_num, player1_choice, player2_choice, player1_score, player2_score, winner, rounds_history):
    os.system('clear' if os.name == 'posix' else 'cls')  # پاک کردن ترمینال

    print(f"\n--------  result  --------")
    
    # نمایش راندهای قبلی
    for i, prev_round in enumerate(rounds_history, start=1):
        print(f"--- Round {i} ---")
        print(f"player1: {prev_round['player1_choice']}  player2: {prev_round['player2_choice']}")
        print(f"score player1: {prev_round['player1_score']}  score player2: {prev_round['player2_score']}")
        print(prev_round['winner'])
        print("-------------------------")
    
    # جمع امتیازهای هر بازیکن  
    total_score_player1 = sum(round['player1_score'] for round in rounds_history)
    total_score_player2 = sum(round['player2_score'] for round in rounds_history)

    print("\nTotal Scores:")
    print(f"total score player1: {total_score_player1}")
    print(f"total score player2: {total_score_player2}")

    write_to_file('total_score.txt', f"total score player1: {total_score_player1}") # ثبت امتیاز های بازکن 1 در فایل
    write_to_file('total_score.txt', f"total score player2: {total_score_player2}") # ثبت امتیاز های بازکن 2 در فایل

    # نمایش بازکننده کل بازی
    if total_score_player1 > total_score_player2:
        print("Player1 is winning!")
    elif total_score_player1 < total_score_player2:
        print("Player2 is winning!")
    else:
        print("two player is equal!")
    print("-------------------------")
    input("Press Enter to continue...")  # منتظر ماندن تا کاربر Enter بزند

# تابع برای  نوشتن در فایل
def write_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

# تابع اجرا کننده دوباره بازی
def play_again():
    answer = input("Do you want to play again? (y/n): ")
    return answer.lower() == 'y'

# تابع برای انتخاب مود بازی
def select_game_mode():
    print("Select Game Mode:")
    print("1. Player vs Player (PvP)")
    print("2. Player vs AI (PvAI)")
    print("3. AI vs AI (AIvAI)")
    mode = input("Enter the mode number (1/2/3): ")

    if mode == '1':
        print("mode is player vs player")
        return "1"
    elif mode == '2':
        print("mode is player vs AI")
        return "2"
    elif mode == '3':
        print("mode is AI vs AI")
        return "3"
    else:
        print("Invalid input. Please enter a valid mode.")
        print("------------------------------------")
        return select_game_mode()


# تابع برای استراتژی  عامل هوشمند اول
#با کاغذ شروع میکند وبعدش با توجه به حرکت اخر حریف جواب میدهد
def smart_agent_strategy_1(opponent_moves):
    if len(opponent_moves) < 1:
        return 'C'  # کاغذ
    elif opponent_moves[-1] == 'C':
        return 'C'  # کاغذ
    else:
        return 'D'  # قیچی

# تابع برای استراتژی هوشمند دوم
#با قیچی شروع میکند و بعدش با کاغذ بازی میکند فقط زمانی دوباره از قیچی استفاده میکند که  حریفش دوبار پشت سر هم کاغذ بازی کرده باشد
def smart_agent_strategy_2(opponent_moves):
    if len(opponent_moves) < 1:
        return 'D'  # قیچی
    elif len(opponent_moves) == 1:
        return 'C'  # کاغذ
    elif opponent_moves[-1] == 'C' and opponent_moves[-2] == 'C':
        return 'D'  # قیچی
    else:
        return 'C'  # کاغذ


# تابع اجرا کننده بازی
def main():
    rounds_history = []  # اضافه کردن لیست برای ذخیره تاریخچه راندها
    
    while True:
        repeat_count, rounds_per_game = input_get() # گرفتن تعداد راند ها و بازی ها 
        
        mode = select_game_mode() # گرفتن نوع بازی
        
        selected_function1= random.choice([smart_agent_strategy_1, smart_agent_strategy_2]) # انتخاب استراتژی
        selected_function2= random.choice([smart_agent_strategy_1, smart_agent_strategy_2]) # انتخاب استراتژی
        
        opponent_moves1 = [] # ذخیره حرکات حریف در لیست حرکات بازیکن 1
        opponent_moves2 = [] # ذخیره حرکات حریف در لیست حرکات بازیکن 2
        
        for game_num in range(1, repeat_count + 1):
            print(f"\n---------------- Game {game_num} ----------------")
            game_rounds_history = []  # اضافه کردن لیست برای ذخیره تاریخچه راندها هر بازی
            
            for round_num in range(1, rounds_per_game + 1):
                   
                if mode == "1":
                    print( "D = GHAEICHI...C = KAGHAZE" )
                    player1_choice = input("player1! choice (D or C): ")
                    player2_choice = input("player2! choice (D or C): ")
                
                elif mode == "2":
                    print( "D = GHAEICHI...C = KAGHAZE" )
                    player1_choice = input("player1! choice (D or C): ")
                    opponent_moves1.append(player1_choice)
                    chose = selected_function1(opponent_moves1)
                    player2_choice = chose
                    print("AI choice :"+chose)
                    input("Press Enter to continue...")  # منتظر ماندن تا کاربر Enter بزند
                
                elif mode == "3":
                    print( "D = GHAEICHI...C = KAGHAZE" )
                    chose1  = selected_function1(opponent_moves2)
                    player1_choice = chose1
                    opponent_moves1.append(player1_choice)
                    print("AI 1 choice :"+chose1)
                    chose2  = selected_function2(opponent_moves1)
                    player2_choice = chose2
                    opponent_moves2.append(player2_choice)
                    print("AI 2 choice :"+chose2)
                    input("Press Enter to continue...")  # منتظر ماندن تا کاربر Enter بزند
                
                
                player1_score, player2_score = game_play(player1_choice, player2_choice) # محاسبه امتیازات
                
                winner = winner_find(player1_score, player2_score) # پیدا کردن برنده
                
                # ذخیره نتایج راند جاری
                current_round = {
                    'player1_choice': player1_choice,  
                    'player2_choice': player2_choice,  
                    'player1_score': player1_score,
                    'player2_score': player2_score,
                    'winner': winner
                }
                # اضافه کردن نتایج راند جاری به لیست
                game_rounds_history.append(current_round)
                # نمایش همه راند ها
                result_print(round_num, player1_choice, player2_choice, player1_score, player2_score, winner, rounds_history + game_rounds_history)
                # ذخیره نتایج بازی در فایل
                if winner == "player1 winner!":
                    write_to_file('winner_log.txt', '1')
                elif winner == "player2 winner!":
                    write_to_file('winner_log.txt', '2')
                else:
                    write_to_file('winner_log.txt', '0')
            
            # اضافه کردن تاریخچه راندهای هر بازی به تاریخچه کلی
            rounds_history.extend(game_rounds_history)

        print("Thank you for playing!")
        print("------------------------------------")
        # پرسیدن اینکه تمایل به ادامه بازی دارد یا خیر
        if not play_again():
            break
        print("------------------------------------")

#این الگو برای جلوگیری از اجرای توابع یا کدهای غیر ضروری هنگامی که یک فایل به عنوان ماژول در یک برنامه بزرگتر استفاده می‌شود، بسیار مفید است.
if __name__ == "__main__":
    main()
