from db import init_db, insert_item, get_items_by_date, get_total_by_date, get_merchants_by_item_and_daterange
from datetime import date, timedelta

init_db()

today = date.today().isoformat()
yesterday = (date.today() - timedelta(days=1)).isoformat()

# data dummy buat test
insert_item("McDonald's", yesterday, "Hamburger", 35000)
insert_item("McDonald's", yesterday, "French Fries", 20000)
insert_item("KFC", today, "Fried Chicken", 45000)

print("Item kemarin:", get_items_by_date(yesterday))
print("Total kemarin:", get_total_by_date(yesterday))
print("Merchant jual hamburger 7 hari terakhir:",
      get_merchants_by_item_and_daterange("hamburger", (date.today() - timedelta(days=7)).isoformat(), today))
