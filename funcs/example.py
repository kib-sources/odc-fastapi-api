"""
TODO Описание модуля

Файл создан 02.02.2025 в 13:06:37

~/funcs/example.py
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

@app.get("/users/{username}")
async def read_user(username: str):
    return {"message": f"Hello {username}"}
