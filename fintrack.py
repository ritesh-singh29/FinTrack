import pandas as pd

data = {
    "Date": pd.to_datetime([
        "2026-01-01","2026-01-10",
        "2026-02-01","2026-02-05",
        "2026-03-01","2026-03-04","2026-03-08"
        ]),
    "Month":["Jan","Jan","Feb","Feb","Mar","Mar","Mar"],
    "Category":["Rent","Food","Rent","Food","Rent","Food","Travel"],
    "Amount":[15000,5000,15000,6000,15000,4000,3000],
    "Expense_Type":["Fixed","Variable","Fixed","Variable","Fixed","Variable","Variable"],
    "Payment_Mode":["UPI","Cash","UPI","Cash","UPI","Cash","Cash"]
}
df=pd.DataFrame(data)
print(df)

# Total monthly expense
print(df.groupby("Month")["Amount"].sum().reset_index())
# Which Category eats most of the money?
Category_expense=df.groupby("Category")["Amount"].sum().reset_index()
print(Category_expense)

# Visualize the expenses
import matplotlib.pyplot as plt
Category_expense.plot(kind = "bar",
                      x = "Category",
                      y = "Amount")
plt.ylabel("Expense in Rupees")
plt.title("Category wise expense")
print(plt.show())

# How much total spending in rent vs others?
cat_pct=df.groupby("Category")["Amount"].sum()
print(cat_pct)

percentage=((cat_pct/cat_pct.sum())*100).round(2).reset_index()
print(percentage)

plt.figure(figsize=(6,5))
plt.pie(percentage["Amount"],
        labels = percentage["Category"],
        autopct="%1.1f%%")
plt.title("Expense distribution by category")
print(plt.show())

# Fixed vs Variable
print(df)
print(df.groupby("Expense_Type")["Amount"].sum().reset_index())

# Payment mode analysis
print(df.groupby("Payment_Mode")["Amount"].sum().reset_index())
print(df["Payment_Mode"].value_counts().reset_index())

# Which day the expense is most?
df["Day"]=df["Date"].dt.day_name()
print(df)
day_expense=df.groupby("Day")["Amount"].sum().reset_index()
# Sort the values in descending order
print(day_expense.sort_values("Amount", ascending=False))
day_expense.plot(kind="bar",
                 x = "Day",
                 y = "Amount")
plt.title("Spending by day of week")
plt.xlabel("Day")
plt.ylabel("Expense in Rs.")
print(plt.show())

