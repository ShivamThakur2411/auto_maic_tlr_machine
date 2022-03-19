class Automatic_teller_machine(object):
    def __init__(self, card_num, pin):
        self.card_num = card_num
        self.pin = pin
    def check_balance(self):
        print("your balance is 44,000 INR.")
    def cash_withdraw(self, entered_amount):
        money_remaining = 44000 - entered_amount
        print("amount " + str(entered_amount) + "INR. is withdrawn, remaining amount is - " + str(money_remaining))


card_n = int(input("enter you card number - "))
pin_n = int(input("enter PIN - "))

auto_tlr_mach = Automatic_teller_machine(card_n, pin_n)

further_act = int(input("Press (1) to check balance, (2) to withdraw money - "))

if further_act==1:
    auto_tlr_mach.check_balance()
elif further_act==2:
    withdrawing_amt = int(input("Enter the amount to be withdraw - "))
    auto_tlr_mach.cash_withdraw(withdrawing_amt)
else:
    print("ENTER EITHER (1) OR (2)..!")