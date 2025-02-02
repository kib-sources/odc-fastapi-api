"""
TODO Описание модуля

Файл создан 02.02.2025 в 13:17:12

~/objects/banknote.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'SG, 2024'
__license__ = 'SG LLC'
__credits__ = [
    'pavelmstu',
]
__version__ = "20250202"
__status__ = "Develop"

# __status__ = "Production"


import os

from pydantic import BaseModel

from typing import Optional, List

from objects.types import HASH


class BanknoteHeader(BaseModel):

    bank_id: str
    banknote_id: str

    # TODO заполнить в соответствии с ODCv3 документацией


class BanknoteApplicability(BaseModel):

    hash: HASH

    # TODO заполнить в соответствии с ODCv3 документацией

class BanknoteChain(BaseModel):
    hash: HASH

    # TODO заполнить в соотвествии с ODCv3 документацией


class Banknote(BaseModel):
    header : BanknoteHeader
    applicabilities : List[BanknoteApplicability]
    chains: List[BanknoteChain]


