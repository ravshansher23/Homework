import requests
import sys


def currency_rates(code) -> float:

        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        code = code.upper()
        if response.ok:
            text = response.text
            cur = text.split(code)

            if len(cur) == 1:
                return None
            value = cur[1].split("</Value>")[0].split("<Value>")[1]
            value = float(value.replace(",", "."))
            name_nom = cur[1].split("</Name>")[0].split("<Name>")[1]
            nominal = cur[1].split("</Nominal>")[0].split("<Nominal>")[1]
        else:
            return None
        result_value = f'{nominal} {name_nom} = {value} руб.'
        return result_value




