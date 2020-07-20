# Print out the variance of the Proline column
print(np.var(wine[["Proline"]]))

# Apply the log normalization function to the Proline column
wine["Proline_log"] = np.log(wine["Proline"])

# Check the variance of the normalized Proline column
print(np.var(wine[["Proline_log"]]))
