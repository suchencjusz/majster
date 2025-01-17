from enum import Enum

class OperationType(Enum):
    UNKNOWN = "UNKNOWN"
    CARD = "CARD"
    BLIK = "BLIK"
    TRANSFER = "TRANSFER"
    ATM = "ATM"