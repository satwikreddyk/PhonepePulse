import pandas as pd

data = {
    "success": True,
    "code": "SUCCESS",
    "data": {
        "from": 1672511400000,
        "to": 1679941800000,
        "transactionData": [
            {
                "name": "Merchant payments",
                "paymentInstruments": [
                    {"type": "TOTAL", "count": 7205999708, "amount": 3.745994748195e12}
                ],
            },
        ],
    },
    "responseTimestamp": 1692619032318,
}

transaction_data = data["data"]["transactionData"]
df = pd.DataFrame()
for item in transaction_data:
    name = item["name"]
    payment_instruments = item["paymentInstruments"]
    for instrument in payment_instruments:
        instrument_type = instrument["type"]
        count = instrument["count"]
        amount = instrument["amount"]
        df = df.append({"Transaction Type": name, "Instrument Type": instrument_type, "Count": count, "Amount": amount}, ignore_index=True)

