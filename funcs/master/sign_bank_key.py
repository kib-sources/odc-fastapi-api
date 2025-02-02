"""

Файл создан 02.02.2025 в 14:22:41

~/funcs/master/sign_master_key.py
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

from objects.types import KEY

from common import doc_fix


@app.post("/master/{master_id}/sign_bank_key", tags=["master"])
@doc_fix
async def sign_bank_key(master_id: int, bok: KEY):
    """
    Функция подписывания одного BOK ключа
    мастер-ключом.
    """

    return JSONResponse("Not implemented yet", status_code=501)

