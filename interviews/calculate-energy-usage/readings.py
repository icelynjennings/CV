import calendar
import logging
from datetime import datetime, date

logger = logging.getLogger('bulb')

class Reading():
    """Represents a meter reading under a member's account,
    taken in a certain month of a certain year."""

    def __init__(self, unit, cumulative, reading_date, fuel):
        self.unit = unit
        self.cumulative = cumulative
        self.reading_date = datetime.fromisoformat(reading_date[:-1])
        self.month = int(self.reading_date.month)
        self.year = int(self.reading_date.year)
        self.fuel = fuel

    def __hash__(self):
        return hash((self.fuel, self.month, self.year))

    def previous_reading_date(self) -> (int, int):
        return (12, self.year-1) if self.month == 1 else (self.month-1, self.year)

    @staticmethod
    def to_kwh(value, calorific_value=39.5, regulatory_factor=1.02264, regulatory_kwh_conversion_divisor=3.6):
        """Returns a reading's cumulative value in kWh."""
        if int(calorific_value) not in range(38, 42):
            raise ValueError("calorific_value must be between 38 and 41.")
        return ((value * regulatory_factor ) * calorific_value) / regulatory_kwh_conversion_divisor


class Account():
    """Represents a single account belonging to a Member."""

    def __init__(self, name, account_data):
        self.name = name
        self.readings = dict()

        for fuel, readings in account_data.items():
            for reading in readings:
                date = datetime.fromisoformat(reading["readingDate"][:-1])
                self.readings[(fuel, date.month, date.year)] = Reading(
                    reading["unit"],
                    reading["cumulative"],
                    reading["readingDate"],
                    fuel
                )

    def calculate_monthly_usage(self, fuel, bill_date) -> (float, int):
        """Calculate daily usage by comparing with last reading 
        then multiply by month length in days"""

        try:
            key = fuel, int(bill_date.month), int(bill_date.year)
            curr_reading = self.readings[key]
        except KeyError:
            logger.debug(f"No {fuel} reading for {bill_date}.")
            return 0.0, 0


        try:
            key = fuel, *curr_reading.previous_reading_date()
            prev_reading = self.readings[key]
        except KeyError:
            logger.debug(f"No {fuel} reading for {bill_date}.")
            return 0.0, 0

        days_between = (curr_reading.reading_date - prev_reading.reading_date).days
        month_length = calendar.monthrange(curr_reading.reading_date.year, curr_reading.reading_date.month)[1]
        daily_use = (curr_reading.cumulative - prev_reading.cumulative) / days_between

        return daily_use * month_length, month_length


class Member():
    """Represents a member or customer."""

    def __init__(self, member_id, readings):
        self.member_id = member_id
        accounts = readings.get(member_id)
        if accounts is None:
            raise ValueError(f"Couldn't find member {member_id}.")

        self.accounts = dict() 

        for name, account_data in accounts[0].items():
            self.accounts[name] = Account(name, account_data[0])

    def calculate_tariff(self, fuel, tariff, kwh_used, days) -> float:
        monthly_standing_charge = tariff[fuel]["standing_charge"] * days
        per_unit_rate = (tariff[fuel]["unit_rate"] * kwh_used) / 100
        return monthly_standing_charge + per_unit_rate

        
    def calculate_bill(self, tariff, account_id, bill_date) -> (float, float):
        """Returns a member's bill across their Accounts on a given date."""
        total_bill, total_kwh, total_m3 = 0, 0, 0

        if account_id == "ALL" or account_id is None:
            accounts = self.accounts
        else:
            try:
                accounts = {account_id: self.accounts[account_id]}
            except KeyError:
                raise KeyError(f"Couldn't find account {account_id} under member {self.member_id}")

        for _, account in accounts.items(): # TODO maybe replace with a reduce()
            kwh_used, days = account.calculate_monthly_usage("electricity", bill_date)
            m3_used, days = account.calculate_monthly_usage("gas", bill_date)
            total_kwh += kwh_used
            total_m3 += m3_used
            total_kwh += Reading.to_kwh(m3_used)

            total_bill += self.calculate_tariff("electricity", tariff, kwh_used, days)
            total_bill += self.calculate_tariff("gas", tariff, Reading.to_kwh(m3_used), days)

        return total_bill, total_kwh
