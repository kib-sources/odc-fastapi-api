"""
Выпуск новой банкноты

Файл создан 02.02.2025 в 13:54:30

~/funcs/production/issuance.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2025'
__license__ = 'KIB'
__credits__ = [
    'pavelmstu',
]
__version__ = "20250202"
__status__ = "Develop"

# __status__ = "Production"

from funcs import app
from objects.banknote import BanknoteHeader, Banknote

from fastapi.responses import JSONResponse

from common import doc_fix


@app.post("/production/issuance/{banknote_id}", response_model=Banknote, tags=["production"])
@doc_fix
async def issuance(banknote_id: str, banknote_header: BanknoteHeader) -> JSONResponse:
    """
    **TODO ссылка на документацию**

    Создаёт новую банкноту

    """
    assert isinstance(banknote_header, BanknoteHeader)
    assert banknote_header.banknote_id == banknote_id

    # TODO return Banknote(...)
    return JSONResponse("Not implemented yet", status_code=501)
