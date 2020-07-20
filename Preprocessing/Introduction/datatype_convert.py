# Print the head of the hits column
print(volunteer["hits"].head())

# Convert the hits column to type int
volunteer["hits"] = volunteer["hits"].astype("int64")

# Look at the dtypes of the dataset
print(volunteer.dtypes)
