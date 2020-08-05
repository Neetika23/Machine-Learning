# Convert the Country column to a one hot encoded Data Frame
one_hot_encoded = pd.get_dummies(so_survey_df, columns=['Country'], prefix='OH')

# Print the columns names
print(one_hot_encoded.columns)
# Create subset of only the numeric columns
so_numeric_df = so_survey_df.select_dtypes(include=['int64', 'float64'])

# Print the column names contained in so_survey_df_num
print(so_numeric_df.columns)
