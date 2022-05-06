from math import ceil

from axie_utils import Axies, Payment

from utils import get_claims_log, get_guys


company_ronin = 'ronin:COMPANY_RONIN'

guys = get_guys('UserList for AutoClaimSystem.csv')

claims = get_claims_log()

for guy in guys:
    if guy.rental_ronin in claims:
        slp_amount = claims[guy.rental_ronin]
        new_slp_amount = slp_amount - guy.additional
        
        user = Axies(guy.rental_ronin)
        number_of_axies = user.number_of_axies()
        if number_of_axies in range(0, 10): requirements = 240
        elif number_of_axies in range(10, 20): requirements = 160
        elif number_of_axies >= 20: requirements = 240

        fine_sum = 50 * guy.penalties
        scholar_salary_percent = 0.5 if new_slp_amount >= requirements * 14 else 0.4
        scholar_salary = ceil(new_slp_amount * scholar_salary_percent) - fine_sum

        p1 = Payment(guy.account_name + ' (Выплата участнику)',
                guy.rental_ronin, guy.private_key,
                guy.payout_ronin, scholar_salary
        )
        p1.execute()

        company_salary = slp_amount - scholar_salary

        p2 = Payment(guy.account_name + ' (Выплата компании)',
                guy.rental_ronin, guy.private_key,
                company_ronin, company_salary)
        p2.execute()

        print(f'''{p1.name} - {scholar_salary} SLP ({guy.penalties} штрафов)
{p2.name} - {company_salary} SLP ({fine_sum} со штрафов, {guy.additional} доп. списаний)\n''')
