from datetime import datetime, date

def get_days_to_new_year():
    today = datetime.today()
    source_date = date(today.year, 12,31)
    return source_date.toordinal() - today.toordinal()

if __name__ == '__main__':
    print(get_days_to_new_year())