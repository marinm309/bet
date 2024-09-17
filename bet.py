import sys
import msvcrt

def main():
    
    def check_winning_bet(c1, c2):
        return ((1/c1 + 1/c2) < 1), (1/c1 + 1/c2)
        
    def money_bet_calculation(c1, c2, b):
        if c1 >= c2:
            total_bet = c2 * b
            coff2_bet = b
            coff1_bet = total_bet / c1
            profit = coff2 * bet - (coff2_bet + coff1_bet)
        else:
            total_bet = c1 * b
            coff1_bet = b
            coff2_bet = total_bet / c2
            profit = coff1 * bet - (coff2_bet + coff1_bet)
            
        return coff1_bet, coff2_bet, profit
        
    def results_printing(c1, c2, c1_bet, c2_bet, p, c):
        print('')
        print(f'The Coefficient of validation is {c}')
        print('')
        print(f'Coefficient: {c1} needs a bet of {c1_bet} lv.')
        print(f'Coefficient: {c2} needs a bet of {c2_bet} lv.')
        print('')
        print(f'Profit: {p}')
        print('')
        print('Press any button to exit.')
        msvcrt.getch()
        sys.exit()
    
    coff1 = float(input('Coefficient 1: '))
    coff2 = float(input('Coefficient 2: '))
    bet = float(input('Bet: '))
    
    is_bet_winning, winning_bet_coefficient = check_winning_bet(coff1 ,coff2)
    
    if not is_bet_winning:
        print('')
        print('Not a winning bet!')
        print('')
        print(f'The Coefficient of validation is {winning_bet_coefficient}')
        print('')
        print('Press any button to exit.')
        msvcrt.getch()
        sys.exit()
        return
    
    coff1_bet, coff2_bet, profit = money_bet_calculation(coff1, coff2, bet)
    
    results_printing(coff1, coff2, coff1_bet, coff2_bet, profit, winning_bet_coefficient)
    
main()