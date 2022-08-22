import math


print("choose either 'investment' or 'bond' from the menu below to proceed")

print("investment - to calculate the amount of intrest youll earn on intrest")
print("bond - to calculate the amount youll have to pay on a home loan")

user_input = input("investment or bond: ")

user_input_cap = user_input.lower()


if user_input_cap == "investment":
    user_amount = float(input("please state how much money you will be depositing?: "))
    user_rate = int(input("please enter intrest rate as a percentage?: "))
    investment_period = int(input("how long are you going to invest for?: "))
    user_rate_type = input("would you like simple or compound instrest?: ")
    user_rate_percent = user_rate/100

    if(user_rate_type == "simple"):
        A = user_amount * (1+user_rate_percent * investment_period)
        simple_reterns = round(A,2)
        print("the amount of simple intrest you will recieve is R" + str(simple_reterns))


    elif(user_rate_type == "compound"):
        A = user_amount * math.pow((1+user_rate_percent),investment_period)
        compund_reterns = round(A,2)

        print("the amount of simple compound intrest you will recieve is R" + str(compund_reterns))
    
    

else:

        property_value =float(input("please state how much is your property worth?: "))
        user_rate1 =int(input("please enter intrest rate as a percentage?: "))
        repay_rate1 =int(input("how long will it take you in months to pay the loan: "))
        user_rate_percent = user_rate1/100
        monthly_rate =float(user_rate_percent/12)

        f=((monthly_rate * property_value)/(1-(1+monthly_rate)**(-repay_rate1)))
        bond_repayment = round(f,2)

        print("your monthly repayment is equal to R" + str(bond_repayment)) 




