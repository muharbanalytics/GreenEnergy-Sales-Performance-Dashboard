import pandas as pd
import os

# Define paths
pipeline_path = os.path.join('data', 'solar_pipeline.csv')
teams_path = os.path.join('data', 'sales_teams.csv')

# 1. Load Data
print("Loading data...")
df_pipeline = pd.read_csv(pipeline_path)
df_teams = pd.read_csv(teams_path)

# 2. Clean and Pre-process
# Convert close_date to datetime
df_pipeline['close_date'] = pd.to_datetime(df_pipeline['close_date'])

# Extract Quarter (Q1, Q2, etc.)
df_pipeline['quarter'] = df_pipeline['close_date'].dt.to_period('Q')

# Handle Missing Values (Example: Fill null close_value with 0 for tracking)
df_pipeline['close_value'] = df_pipeline['close_value'].fillna(0)

# 3. Merge Data (Replacing XLOOKUP)
print("Merging datasets...")
df_merged = pd.merge(
    df_pipeline,
    df_teams,
    on='sales_agent',
    how='left'
)

# Quality Check
print(f"Total rows: {len(df_merged)}")
print(f"Missing Regional Offices: {df_merged['regional_office'].isnull().sum()}")

# 4. Export for Dashboard
output_path = os.path.join('data', 'processed_sales_data.csv')
df_merged.to_csv(output_path, index=False)
print(f"Processed data saved to {output_path}")