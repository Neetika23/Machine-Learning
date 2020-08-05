# Create subset of only the numeric columns
so_numeric_df = so_survey_df.select_dtypes(include=['int64', 'float64'])

# Print the column names contained in so_survey_df_num
print(so_numeric_df.columns)
