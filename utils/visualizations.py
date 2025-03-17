
import pandas as pd
from data.database import collection
def show_sentiment_chart():
    data = list(collection.find())
    df = pd.DataFrame(data)
    sentiment_counts = df["sentiment"].value_counts()
    return df["sentiment"].value_counts()