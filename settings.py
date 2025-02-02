"""
Настройки системы
Файл создан 02.02.2025 в 13:02:04

~//settings.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2025'
__license__ = 'KIB'
__credits__ = [
    'pavelmstu',
]
__version__ = "20250202"
__status__ = "Production"

import os

HOST = os.getenv('HOST', '0.0.0.0')

PORT = int(os.getenv('PORT', 8000))


# URL для help сервера https://docusaurus.io/
URL_ODC_DOC = os.getenv('URL_ODC_DOC', 'http://localhost:3000')
assert not URL_ODC_DOC.endswith('/')