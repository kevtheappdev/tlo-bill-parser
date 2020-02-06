import requests
from typing import IO, List


class BILLTYPES:
    INTRODUCED = 'I'
    HOUSE_COMMITTEE_REPORT = 'H'


class URLSTRINGS:
    BILL_TEXT = 'https://www.legis.state.tx.us/tlodocs/{legis_session}R/billtext/html/' \
                'HB{bill_num}{bill_type}.htm'


def house_bill_text(legis_session: int, bill_num: str, bill_type: BILLTYPES) -> str:
    """
    :param legis_session:
    :param bill_num:
    :param bill_type:
    :return:
    """

    bill_url = URLSTRINGS.BILL_TEXT.format(legis_session=legis_session, bill_num=bill_num, bill_type=bill_type)
    bill_request = requests.get(bill_url)

    if bill_request.status_code == 200:
        return bill_request.text
    else:
        pass


print(house_bill_text(86, '00002', BILLTYPES.HOUSE_COMMITTEE_REPORT))
