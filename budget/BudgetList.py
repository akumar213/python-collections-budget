from budget.Expense import Expense, Expenses


class BudgetList:

    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self, item):
        expense = self.sum_expenses + item.amount
        if expense < self.budget:
            self.expenses.append(item)
            self.sum_expenses = expense
        else:
            self.overages.append(item)
            self.sum_overages += item.amount

    def __len__(self):
        return len(self.overages) + len(self.expenses)


def main():
    myBudgetList = BudgetList(1200)
    expenses = Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense)

    print('The count of all expenses: ', str(len(myBudgetList)))


if __name__ == '__main__':
    main()
