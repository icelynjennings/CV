import logging

from datetime import date

from readings import Member
from load_readings import get_readings
from tariff import BULB_TARIFF

logging.basicConfig()
logger = logging.getLogger("bulb")


def calculate_bill(member_id, account_id, bill_date) -> (float, float):
    """Calculates a member's energy bill within a given date. 
    account_id can be passed to filter only to a member's specific account."""
    bill_date = date.fromisoformat(bill_date)

    # Filter input while freeing memory of unneeded sections of the file.
    readings = get_readings()
    member = Member(member_id, readings)
    del readings 

    # Calculate bill    
    return member.calculate_bill(BULB_TARIFF, account_id, bill_date)

def calculate_and_print_bill(member_id, account, bill_date) -> None:
    """Calculate the bill and then print it to screen.
    Account is an optional argument - I could bill for one account or many.
    There's no need to refactor this function."""
    member_id = member_id or 'member-123'
    bill_date = bill_date or '2017-08-31'
    account = account or 'ALL'
    amount, kwh = calculate_bill(member_id, account, bill_date)
    print('Hello {member}!'.format(member=member_id))
    print('Your bill for {account} on {date} is £{amount}'.format(
        account=account,
        date=bill_date,
        amount=amount))
    print('based on {kwh}kWh of usage in the last month'.format(kwh=kwh))
