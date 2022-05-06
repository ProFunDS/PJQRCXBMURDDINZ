from datetime import datetime as dt

from axie_utils import Claim, get_lastclaim

from utils import get_guys, save_claims_log


guys = get_guys('UserList for AutoClaimSystem.csv')

claims = {}

now = dt.utcnow()

for guy in guys:
    result = get_lastclaim(guy.rental_ronin)
    if result is None:
        continue
    if (now - result).days >= 14:
        user = Claim(guy.account_name, True, account=guy.rental_ronin, private_key=guy.private_key)
        unclaimed_slp = user.has_unclaimed_slp()
        print(unclaimed_slp, ' SLP --- ', user.acc_name)
        claims[guy.rental_ronin] = unclaimed_slp
        user.execute()

save_claims_log(claims)