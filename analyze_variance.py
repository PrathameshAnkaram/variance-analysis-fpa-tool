
import pandas as pd

# Load data
df = pd.read_csv('financials_demo.csv')

# Calculate variance
df['Variance ($)'] = df['Actual'] - df['Budget']
df['Variance (%)'] = ((df['Actual'] - df['Budget']) / df['Budget']) * 100
df['Direction'] = df['Variance ($)'].apply(lambda x: 'Increase' if x > 0 else 'Decrease' if x < 0 else 'No Change')

# Sort by absolute variance
df_sorted = df.sort_values(by='Variance ($)', key=abs, ascending=False)

# Display results
print("\n===== VARIANCE ANALYSIS =====\n")
print(df_sorted.to_string(index=False, float_format='{:,.2f}'.format))

# Optional: Export results
output = input("\nExport results to CSV? (y/n): ")
if output.lower() == 'y':
    df_sorted.to_csv('variance_analysis_output.csv', index=False)
    print("Exported to 'variance_analysis_output.csv'")
