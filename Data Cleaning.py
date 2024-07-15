import pandas as pd

#df_bookings= pd.read_csv("datasets/fact_bookings.csv")
#print(df_bookings.head(2))
#print(df_bookings.shape)
#print(df_bookings.describe())

#data cleaning of booking

#checking negatives in no of guests columns

#print(df_bookings[df_bookings.no_guests<0])  # negative
#df_bookings= df_bookings[df_bookings.no_guests>0]  # true data for guest,positive no now
#print(df_bookings)

#working on reveneue generated column now
#print(df_bookings.revenue_generated.min(),df_bookings.revenue_generated.max())

#OUTLIERS
#figure out max rent - use 3 tier standard deviation

#avg=df_bookings.revenue_generated.mean()  # finding mean
#std= df_bookings.revenue_generated.std()   # finding std
#higher_limit= avg+3*std  #figure out higher limit
#print(higher_limit)
#lower_limit= avg-3*std  #figure out lower limit
#print(lower_limit)
#print(df_bookings[df_bookings.revenue_generated<0])

#print(df_bookings[df_bookings.revenue_generated>higher_limit])  #wrong data
#df_bookings= df_bookings[df_bookings.revenue_generated<higher_limit]  #true data for reveneue generated
#print(df_bookings.shape)

#checking revenue realised column

#print(df_bookings.revenue_realized.describe())  # data seems fine

# handling NA

#print(df_bookings.isnull().sum()) # observse that rating has nA


#WORKING On AGG BOOKING

df_agg_booking= pd.read_csv("datasets/fact_aggregated_bookings.csv")
#print(df_agg_booking.head(2))
#print(df_agg_booking.isnull().sum())
#print(df_agg_booking[df_agg_booking.capacity.isna()]) # wehave 2 values a NAN in capacity

#fillig NA in capacity using median

#print(df_agg_booking.capacity.median())  # 25 is median
#fillNA
df_agg_booking=df_agg_booking["capacity"].fillna(df_agg_booking['capacity'].median())

print(df_agg_booking)
