from . import Expense
import matplotlib.pyplot as plt

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if divided_for_loop != divided_set_comp:
        print('Sets are NOT equal by == test')

    for a, b in zip(divided_set_comp, divided_for_loop):
        if not a.issubset(b) or not b.issubset(a):
            print('Sets are NOT equal by subset test')
        else:
            print('Sets are same.')


if __name__ == "__main__":
    main()