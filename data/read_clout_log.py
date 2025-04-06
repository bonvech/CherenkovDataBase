import pandas as pd

def show_event(event):
    for column in event.index:
        print(f"column: {column}, \t value: {event[column]}")



filename = "CLOUT_logSb.10.txt.example.sm.csv"
df = pd.read_csv(filename)

for idx,event in df.iterrows():
    show_event(event)
