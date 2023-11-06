from datetime import datetime
import gspread
import pandas as pd
from email_validator import validate_email, EmailNotValidError
import time 
from ValidateEmail.run import Check


url_1 = "https://docs.google.com/spreadsheets/d/1Fj_ppXidr19B35NaFEacx2L-WvvrVPSt46VpTh9huwY/edit?usp=sharing"

gc = gspread.service_account(filename="./musicsearch-321511-be1743e3af23.json")
wsb = gc.open_by_url(url_1)

ws = wsb.get_worksheet(0)

df = pd.DataFrame(ws.get_all_records())
df['check'] = "Invalide"
now = datetime.now()
# Iterate through the 'email 1' column and validate emails
for i, email in enumerate(df['email 1']):
    try:
        if "not found" not in email:
            emailinfo = validate_email(email, check_deliverability=True)
            normalized_email = emailinfo.normalized

            if Check(normalized_email):
                df.at[i, 'check'] = "Valid"
            time.sleep(1)
            df.to_csv("./result.csv")
    except EmailNotValidError:
        pass
    except Exception as e:
        pass
print(datetime.now() - now)


ws.update([df.columns.values.tolist()] + df.values.tolist())
