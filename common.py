"""

Файл создан 02.02.2025 в 13:48:33

~//common.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'SG, 2024'
__license__ = 'SG LLC'
__credits__ = [
    'pavelmstu',
]
__version__ = "20250202"
__status__ = "Production"


from settings import URL_ODC_DOC


def doc_fix(apifunc):
    # replace
    for old, new in [
        ('{{URL_ODC_DOC}}', URL_ODC_DOC),
    ]:
        apifunc.__doc__ = apifunc.__doc__.replace(old, new)
    return apifunc

