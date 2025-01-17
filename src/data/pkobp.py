import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import List
import logging
from .transaction import Transaction

class PkoBpParser:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def _clean_amount(self, amount: str) -> float:
        return float(str(amount).strip('"').replace(' ', '').replace(',', '.'))

    def _concatenate_description(self, row: pd.Series) -> str:
        desc_fields = []
        
        for col in row.index[7:]:
            if pd.notna(row[col]) and str(row[col]).strip('"'):
                desc_fields.append(str(row[col]).strip('"'))
        return " | ".join(desc_fields)

    def load_transactions(self) -> List[Transaction]:
        try:
            df = pd.read_csv(
                self.file_path,
                encoding='cp1250',
                header=0,
                sep=',',
                quoting=1, # QUOTE_ALL
                na_filter=False,
                on_bad_lines='warn'
            )
            
            transactions = []
            
            for idx, row in df.iterrows():
                try:
                    transaction = Transaction(
                        date_operation=datetime.strptime(row[0].strip('"'), '%Y-%m-%d'),
                        date_value=datetime.strptime(row[1].strip('"'), '%Y-%m-%d'),
                        amount=self._clean_amount(row[3]),
                        currency=row[4].strip('"'),
                        description=self._concatenate_description(row),
                        raw_operation_type=row[2].strip('"'),
                        extra_data={
                            'balance_after': self._clean_amount(row[5]),
                            'raw_data': row.to_dict()
                        }
                    )
                    transactions.append(transaction)
                except Exception as e:
                    self.logger.error(f"Error processing row {idx}: {e}")
                    continue
                    
            return transactions
            
        except Exception as e:
            self.logger.error(f"Error reading file: {e}")
            raise