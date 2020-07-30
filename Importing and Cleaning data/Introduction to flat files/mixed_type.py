# Assign the filename: file
file = 'titanic.csv'
d = np.recfromcsv(file)
# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])
