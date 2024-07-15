import pandas as pd

df_agg_booking= pd.read_csv("datasets/fact_aggregated_bookings.csv")
#print(df_agg_booking.head(2))

#create new column

df_agg_booking["Occ_pct"]=df_agg_booking["successful_bookings"]/df_agg_booking["capacity"]
print(df_agg_booking.head(2))

#round off occ_pct value

df_agg_booking["Occ_pct"]=df_agg_booking["Occ_pct"].apply(lambda x: round(x*100,2))
print(df_agg_booking.head(2))
