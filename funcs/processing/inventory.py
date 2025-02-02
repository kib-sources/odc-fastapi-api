"""

import funcs.processing

Файл создан 02.02.2025 в 13:16:21

~/funcs/processing/__init__.py
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
from objects.banknote import Banknote

from fastapi.responses import JSONResponse

from common import doc_fix


@app.post("/processing/inventory/{banknote_id}")
@doc_fix
async def inventory(banknote_id: str, banknote: Banknote):
    """
    [Смотри inventory]({{URL_ODC_DOC}}/docs/project3/functions/inventory_server)

    Функция **сервера**.
    
    Данная функция вызывается из **одноимённой функции кошелька**
    
    Необходима для двух целей:
    1. Для пользователей: дополнительное подтверждение offline платежа.
    1. Для банка-эмитента: история движения каждой банкноты в системе для дальнейшего анализа.
    
    """
    assert isinstance(banknote, Banknote)
    assert banknote.header.banknote_id == banknote_id

    return JSONResponse("Not implemented yet", status_code=501)

