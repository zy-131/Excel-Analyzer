def get_data(f):
    dates = []
    descriptions = []
    amounts = []
    balances = []
    with open(f) as file:
        next(file)
        for line in file:
            newline = line.rstrip('\n')
            data = newline.split(',')
            dates.append(data[0])
            descriptions.append(data[1])
            amounts.append(data[2])
            balances.append(data[3])
    file.close()
    amounts[0] = '0'
    return dates, descriptions, amounts, balances


def get_monthly(date, amt):
    monthly_spent = [0, 0, 0, 0, 0, 0]
    monthly_earned = [0, 0, 0, 0, 0, 0]
    for i in range(len(date)):
        date_value = date[i]
        d = date_value[0:2]
        if d.find('1') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[0] += x
            else:
                monthly_spent[0] += x
        elif d.find('2') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[1] += x
            else:
                monthly_spent[1] += x
        elif d.find('3') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[2] += x
            else:
                monthly_spent[2] += x
        elif d.find('4') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[3] += x
            else:
                monthly_spent[3] += x
        elif d.find('5') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[4] += x
            else:
                monthly_spent[4] += x
        elif d.find('6') != -1:
            x = float(amt[i])
            if x >= 0:
                monthly_earned[5] += x
            else:
                monthly_spent[5] += x
    return monthly_spent, monthly_earned


def get_specific(date, amt, des, bal):
    day = input("Please enter date of transaction: ")
    d = date[:]
    i = d.count(day)
    if i >= 1:
        while i != 0:
            x = d.index(day)
            description = des[x]
            amount = amt[x]
            balance = bal[x]
            print(day + ', ' + description + ', Amount = ' + amount + ', Balance = ' + balance)
            d[x] = 0
            i -= 1
    else:
        print("Date of transaction does not exist.")


def get_total(amt):
    spent = 0
    earned = 0
    for i in amt:
        if i.find('-') != -1:
            spent += float(i)
        else:
            earned += float(i)
    return spent, earned


def format_months(m_earned, m_spent):
    print("\n         January       February      March       \tApril"
          "     \t  May     \t\tJune")
    print("Earned   ", end='')
    for i in m_earned:
        print(format(i, '.2f'), end='')
        whitespace = 14 - len(str(format(i, '.2f')))
        for x in range(whitespace):
            print(" ", end='')
    print("\nSpent    ", end='')
    for i in m_spent:
        print(format(i, '.2f'), "   ", end='')
        whitespace = 10 - len(str(format(i, '.2f')))
        for x in range(whitespace):
            print(" ", end='')
    print("\n")


def main():
    file_name = input("Enter properly formatted csv file: ")
    dates, descriptions, amounts, balances = get_data(file_name)
    cont = True
    while cont:
        option = input("Enter monthly for monthly budgetary expenses, specific for specific date information, "
                       "or total for total earning and spending: ")
        if option == "monthly":
            monthly_spent, monthly_earned = get_monthly(dates, amounts)
            format_months(monthly_earned, monthly_spent)
        elif option == "specific":
            get_specific(dates, amounts, descriptions, balances)
        elif option == "total":
            spent, earned = get_total(amounts)
            print("Earned =", format(earned, '.2f'), ", Spent =", format(spent, '.2f'))
        else:
            print("Sorry, did not understand")

        y_or_n = input("Would you like to continue? (yes or no): ")
        if y_or_n == "yes":
            cont = True
        else:
            cont = False


main()











