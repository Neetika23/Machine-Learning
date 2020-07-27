# Replace missing values with the median for each column
X = prices_perc_shifted.fillna(np.mean(prices_perc_shifted))
y = prices_perc.fillna(np.mean(prices_perc))

# Fit the model
model = Ridge()
model.fit(X, y)
