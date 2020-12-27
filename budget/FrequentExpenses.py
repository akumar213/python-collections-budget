from . import Expense
import collections
import matplotlib.pyplot as pp

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
print('Read Expenses from file....')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)
print('Spending Categories: {}'.format(spending_categories))

# spending_categories_count = {}
# for expense in expenses.list:
#     category = expense.category
#     if category in spending_categories_count.keys():
#         count = spending_categories_count[category]
#         spending_categories_count[category] = count + 1
#     else:
#         spending_categories_count[category] = 1
# print('Spending Categories Count: {}'.format(spending_categories_count))

spending_counter = collections.Counter(spending_categories)
print('spending_counter: {}'.format(spending_counter))
top5 = spending_counter.most_common(5)
# print(type(top5[0]))
categories, count = zip(*top5)
# print(categories)
# print(count)


fig, ax = pp.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
pp.show()
