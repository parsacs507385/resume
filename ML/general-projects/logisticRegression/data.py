import pandas as pd

predf = pd.read_csv("predata.csv")
predf = predf.drop(["last_evaluation", "number_project", "average_montly_hours", "time_spend_company", "Work_accident", "promotion_last_5years", "Department"], axis=1)
predf.to_csv("data.csv", index=False)