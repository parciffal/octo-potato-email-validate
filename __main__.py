from email_validator import validate_email, EmailNotValidError
import pandas as pd




class EmailVerify:
    def __init__(self, csv_file: str) -> None:
        self.__csv_file = csv_file

    def load_csv(self):
        self.__df = pd.DataFrame

    def validate(self):
        pass



