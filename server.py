"""
Основной запускаемый файл

Файл создан 02.02.2025 в 12:47:48

~//server.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2025'
__license__ = 'KIB'
__credits__ = [
    'pavelmstu',
]
__version__ = "20250202"
__status__ = "Production"

import uvicorn

from funcs import app

# Импортируем все функции.
#   не убирайте эту строку, несмотря на IDE рекомендации
import funcs.imports #!


from settings import HOST
from settings import PORT


def main():
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
    )


if __name__ == "__main__":
    main()
