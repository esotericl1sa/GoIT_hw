from datetime import datetime
import re


def get_days_from_today(date):
    today = datetime.today().date()   # Today's date as a date object
    pattern = r"^\d{4}-\d{2}-\d{2}$"  # RegEx pattern for matching 'YYYY-MM-DD' format
    result = re.match(pattern, date)

    if result:
        dt_date = datetime.strptime(date, "%Y-%m-%d").date()  # Parse the input date
        return (today - dt_date).days  # Subtract date from today and return number of days
    else:
        return "Invalid input."
