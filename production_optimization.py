import pulp


model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

lemonade = pulp.LpVariable("lemonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("juice", lowBound=0, cat="Integer")

water = 2 * lemonade + juice <= 100
sugar = lemonade <= 50
lemon_juice = lemonade <= 30 
fruit_puree = 2 * juice <= 40

model += lemonade + juice

model += water 
model += sugar
model += lemon_juice
model += fruit_puree

model.solve()

print("Для максимізації загальної кількості продуктів, потрібно виробити:")
print("лемонаду:", lemonade.varValue)
print("фруктового соку:", juice.varValue)
