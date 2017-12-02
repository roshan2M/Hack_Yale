import csv

assets = []
profits = []
liabilities = []
assets_st = []
assets_lt = []
equity = []
sales = []
employees = []

with open('report1.csv') as f:
    rows = csv.reader(f)
    for row in rows:
        assets.append(row[3])
        profits.append(row[4])
        liabilities.append(row[8])
        assets_st.append(row[9])
        assets_lt.append(row[10])
        equity.append(row[11])
        sales.append(row[12])
        employees.append(row[13])

assets = assets[1:]
profits = profits[1:]
liabilities = liabilities[1:]
assets_st = assets_st[1:]
assets_lt = assets_lt[1:]
equity = equity[1:]
sales = sales[1:]
employees = employees[1:]