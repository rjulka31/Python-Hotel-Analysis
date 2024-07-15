import pandas as pd

#agg table

df_agg_booking= pd.read_csv("datasets/fact_aggregated_bookings.csv")
df_agg_booking["Occ_pct"]=df_agg_booking["successful_bookings"]/df_agg_booking["capacity"]
df_agg_booking["Occ_pct"]=df_agg_booking["Occ_pct"].apply(lambda x: round(x*100,2))
#print(df_agg_booking.head(2))

#average occupancy rate in each of the room categories
print(df_agg_booking.groupby("room_category")["Occ_pct"].mean().round(2))

#room table

df_room=pd.read_csv("datasets/dim_rooms.csv")
#print(df_room.head(2))
#print(df_agg_booking.head(2))
df=pd.merge(df_agg_booking,df_room, left_on="room_category",right_on="room_id")
#print(df)
print(df.groupby("room_class")["Occ_pct"].mean().round(2))
 ##df has 2 columns indentical will diffferent column name

df.drop("room_id",axis=1, inplace=True)
#print(df)

#average occupancy rate per city

df_hotel= pd.read_csv("datasets/dim_hotels.csv")
#print(df_hotel.head(2))
#print(df_agg_booking.head(2))
df=pd.merge(df_hotel,df,on="property_id")
#print(df.head(2))
#print(df.groupby("city")["Occ_pct"].mean().round(2))

#occupancy better? Weekday or Weekend
df_date=pd.read_csv("datasets/dim_date.csv")
#print(df_date.head(2))
#print(df.head(2))
df=pd.merge(df,df_date,left_on="check_in_date",right_on="date")
#print(df.head(2))
#print(df.groupby("day_type")["Occ_pct"].mean(),round(2))


#In the month of June, what is the occupancy for different cities**
print(df)
print(df.columns)
print(df["mmm yy"].unique())
df_June=df[df["mmm yy"]=="Jun 22"]
print(df_June)
print(df_June.columns)
print(df_June.groupby("city")["Occ_pct"].mean().round(2).sort_values(ascending=False))


#new data for the month of august. Append that to existing data**

df_august = pd.read_csv("datasets/new_data_august.csv")
# print(df_august.head(3))
# print(df_august.columns)
# print(df.columns)
latest_df = pd.concat([df, df_august], ignore_index = True, axis = 0) #adding rows columns same #axis=0 append row wise
# print(latest_df.tail(10))

#revenue realized per city**
#revene in bookings

df_bookings= pd.read_csv("datasets/fact_bookings.csv")
# print(df_bookings.head(2))
# print(df_hotel.head(2))
df_bookings_all = pd.merge(df_bookings, df_hotel, on="property_id")
# print(df_bookings_all.head(3))
# print(df_bookings_all.groupby("city")["revenue_realized"].sum())

#print month by month revenue**
# print(df_date.head(2))
print(df_bookings_all.head(3))
print(df_bookings_all["check_in_date"])
#join check in date & date
# print(df_bookings_all.info())
#
# print(df_date.info())

#convert object datetype to date

df_date["date"]=pd.to_datetime(df_date["date"])
#print(df_date.head(2))
print(df_date.info())
print(df_date["date"])

df_bookings_all["check_in_date"] = pd.to_datetime(df_bookings_all["check_in_date"])
print(df_bookings_all.head(2))
print(df_bookings_all.info())
#
# df_bookings_all = pd.merge(df_bookings_all, df_date, left_on="check_in_date", right_on="date")
# print(df_bookings_all.head(3))
# print(df_bookings_all.groupby("mmm yy")["revenue_realized"].sum())