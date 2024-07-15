import pandas as pd
#reading bookings csv
#df_bookings= pd.read_csv("datasets/fact_bookings.csv")

#exploring booking csv

#print(df_bookings.head(3))                     #head
#print(df_bookings.shape)                       #shape
#print(df_bookings.booking_platform.unique())   # unique on single column
#print(df_bookings.nunique())                    # nunique on entire data frame
#print(df_bookings.describe())                  #describe
#print(df_bookings.booking_platform.value_counts())      #value_count
#print(df_bookings.revenue_generated.min())      #min
#print(df_bookings.revenue_generated.max())      #max
#print(df_bookings.revenue_generated.max(),df_bookings.revenue_generated.min())

#reading other Csv's

df_date=pd.read_csv("datasets/dim_date.csv")
df_hotels=pd.read_csv("datasets/dim_hotels.csv")
df_rooms=pd.read_csv("datasets/dim_rooms.csv")
df_agg_booking=pd.read_csv("datasets/fact_aggregated_bookings.csv")

#explore hotels csv

#print(df_hotels.head(2))
#print(df_hotels.shape)
#print(df_hotels.category.value_counts())
#print(df_hotels.city.value_counts().sort_values())  #sort values


#explore agg booking csv

#print(df_agg_booking.head(2))
#print(df_agg_booking.shape)
#print(df_agg_booking.property_id.nunique())
#print(df_agg_booking.property_id.unique())
#print(df_agg_booking.groupby("property_id")["successful_bookings"].sum())
#print(df_agg_booking[df_agg_booking.successful_bookings > df_agg_booking.capacity])
print(df_agg_booking.capacity.max())
print(df_agg_booking[df_agg_booking.capacity== df_agg_booking.capacity.max()])