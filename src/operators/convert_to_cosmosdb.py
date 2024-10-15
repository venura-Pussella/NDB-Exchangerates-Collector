import uuid
def convert_df_to_cosmos_db_format(df):
    
    cosmos_db_documents = []
    for _, row in df.iterrows():
        rate_document = {
            "id": str(uuid.uuid4()),
            "timestamp": f"{row['Date']}T{row['Time']}Z",
            "currency_name": row['Currency Name'],
            "code": row['Currency Code'],
            "currency_buying_rate": float(row['CurrencyBuying Rate']) if row['CurrencyBuying Rate'] else None,
            "currency_selling_rate": float(row['CurrencySelling Rate']) if row['CurrencySelling Rate'] else None,
            "travelers_cheques_buying_rate": float(row['Travelers ChequesBuying Rate']) if row['Travelers ChequesBuying Rate'] else None,
            "travelers_cheques_selling_rate": float(row['Travelers ChequesSelling Rate']) if row['Travelers ChequesSelling Rate'] else None,
            "telegraphic_transfers_buying_rate": float(row['Telegraphic TransfersBuying Rate']) if row['Telegraphic TransfersBuying Rate'] else None,
            "telegraphic_transfers_selling_rate": float(row['Telegraphic TransfersSelling Rate']) if row['Telegraphic TransfersSelling Rate'] else None,
            "st_bank_code": row['ST BANK CODE'],
            "bank": row['Bank']
        }
        cosmos_db_documents.append(rate_document)
    
    return cosmos_db_documents