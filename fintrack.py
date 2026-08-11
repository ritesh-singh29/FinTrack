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
    "Payment_Mode":["Fixed","Variable","Fixed","Variable","Fixed","Variable","Variable"],
    "Payment_Mode":["UPI","Cash","UPI","Cash","UPI","Cash","Cash"]
}
df=pd.DataFrame(data)
print(df)
# Total monthly expense
print(df.groupby("Month")["Amount"].sum().reset_index())
# Which Category eats most of the money?
