from axie_utils import Scatter

from utils import get_private_keys


RON_AMOUNT = 1  # количество RON на каждый аккаунт

# откуда списывать RON
RONIN = ''
PRIVATE_KEY = ''

keys = get_private_keys()

pay_dict = {ronin : RON_AMOUNT for ronin in keys if ronin != RONIN}

aa = Scatter(token='ron', from_acc=RONIN,
            from_private=PRIVATE_KEY,
            to_ronin_ammount_dict=pay_dict)
aa.execute_ron(1)