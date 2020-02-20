import requests
from html2text import HTML2Text
import os

class BILLTYPES:
    INTRODUCED = 'I'
    HOUSE_COMMITTEE_REPORT = 'H'


class URLSTRINGS:
    BILL_TEXT = 'https://www.legis.state.tx.us/tlodocs/{legis_session}R/billtext/html/' \
                'HB{bill_num}{bill_type}.htm'


def house_bill_text(legis_session: int, bill_num: str, bill_type: str) -> str:
    """
    :param legis_session:
    :param bill_num:
    :param bill_type:
    :return:
    """

    bill_url = URLSTRINGS.BILL_TEXT.format(legis_session=legis_session, bill_num=bill_num, bill_type=bill_type)
    bill_request = requests.get(bill_url)

    # strip out text from html
    h = HTML2Text()
    text = bill_request.text
    h.ignore_links = True
    result = h.handle(text)
    return result


# for i in range(1, 7315):
#     num = str(i).zfill(5)
#     fileName = 'bill-texts/HB{num}{type}.txt'.format(num=num, type=BILLTYPES.INTRODUCED)
#     file = open(fileName, 'w')
#     file.write(house_bill_text(86, str(i).zfill(5), BILLTYPES.INTRODUCED)) # pad bill number to 5-digits
