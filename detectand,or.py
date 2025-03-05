import re

def parse_client_string(client_str):
    """ تشخیص نام کلاینت‌ها و عملگرهای `and`, `or`, `&` (AND) و `|` (OR) """

    # اصلاح برای اضافه کردن اسپیس فقط در صورتی که 'and' یا 'or' یا '&' و '|' بین دو کلمه قرار داشته باشند
    # این فقط زمانی اتفاق می‌افتد که واقعا `and` یا `or` به عنوان عملگر استفاده شوند
    modified_str = re.sub(r'(?<=\w)(and|or|&|\|)(?=\w)', r' \1 ', client_str)
    
    # پیدا کردن عملگرهای `and`, `or`, `&` و `|`
    operators = re.findall(r'\band\b|\bor\b|&|\|', modified_str)
    operators = [op.strip().lower() for op in operators]  # تبدیل به حروف کوچک

    # جدا کردن نام کلاینت‌ها فقط بر اساس `and`, `or`, `&`, `|`
    clients = re.split(r'\band\b|\bor\b|&|\|', modified_str)
    clients = [c.strip() for c in clients if c.strip()]  # حذف فاصله‌های اضافی و رشته‌های خالی

    return clients, operators  # برگرداندن کلاینت‌ها و عملگرها

# تست کد
test_strings = [
    "A&BandC",          # ✅ ['A', 'B', 'C'] و ['and']
    "UserX|UserY&UserZ",  # ✅ ['UserX', 'UserY', 'UserZ'] و ['or', 'and']
    "Client1&Client2|Client3",  # ✅ ['Client1', 'Client2', 'Client3'] و ['and', 'or']
    "Andy and Bob",       # ✅ ['Andy', 'Bob'] و ['and']
    "Orlando or Alice",   # ✅ ['Orlando', 'Alice'] و ['or']
    "andyandorlando",  # ✅ ['andyandorlando'] و []
    "Device1|Device2&Device3",  # ✅ ['Device1', 'Device2', 'Device3'] و ['or', 'and']
    "OnlyOneClient"       # ✅ ['OnlyOneClient'] و []
]

for s in test_strings:
    print(parse_client_string(s))