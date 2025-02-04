"""
Модуль импртирования всех функций

Файл создан 02.02.2025 в 12:55:39

~/funcs/imports.py
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

# Не убирайте импорты с #! значением.
#   Это импортируемые функции в app

# --------------------------------------------------------------------------------------------------------------------
# -------  master
import funcs.master.sign_master_key #!
import funcs.master.sign_bank_key #!

# --------------------------------------------------------------------------------------------------------------------
# -------  production
import funcs.production.issuance #!
import funcs.production.sign_sim_key #!

# --------------------------------------------------------------------------------------------------------------------
# -------  processing
import funcs.processing.inventory #!

