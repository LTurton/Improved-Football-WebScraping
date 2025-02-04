from datetime import datetime
from datetime import timedelta

class DateHelpers:
    
    @staticmethod
    def get_todays_date():
        return datetime.today().strftime('%Y-%m-%d')
    
    @staticmethod
    def get_yesterdays_date():
        return (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')
    
    @staticmethod
    def get_tomorrows_date():
        return (datetime.today() + timedelta(days = 1)).strftime('%Y-%m-%d')

    @staticmethod
    def request_custom_date():
        date = input("Enter the date that you would like to see fixtures from in the format (YYYY-MM-DD): ")
        return date