import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration
num_agents = 20
num_deals = 500
regions = ['West', 'Central', 'East']
managers = ['Sarah Jenkins', 'Mike Ross', 'Jessica Pearson']
stages = ['Prospecting', 'Engaging', 'Won', 'Lost']

# 1. Generate Sales Teams Data
agents = [f'Agent_{i}' for i in range(1, num_agents + 1)]
teams_data = {
    'sales_agent': agents,
    'manager': [random.choice(managers) for _ in range(num_agents)],
    'regional_office': [random.choice(regions) for _ in range(num_agents)]
}
df_teams = pd.DataFrame(teams_data)
df_teams.to_csv('sales_teams.csv', index=False)
print("sales_teams.csv created.")

# 2. Generate Solar Pipeline Data
# Helper function for random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

pipeline_data = []
for i in range(num_deals):
    stage = random.choices(stages, weights=[0.3, 0.2, 0.3, 0.2])[0]
    agent = random.choice(agents)
    product_size = random.choice(['5kW', '8kW', '10kW', '12kW'])
    
    # Logic: "Won" deals have close dates and values. Others might have nulls.
    if stage == 'Won':
        close_date = random_date(start_date, end_date)
        close_value = random.randint(15000, 45000)
    elif stage == 'Lost':
        close_date = random_date(start_date, end_date)
        close_value = 0 
    else:
        # Prospecting/Engaging might not have a close date yet
        close_date = np.nan
        close_value = np.nan

    pipeline_data.append({
        'opportunity_id': f'OPP-{1000+i}',
        'sales_agent': agent,
        'system_size': product_size,
        'deal_stage': stage,
        'close_date': close_date,
        'close_value': close_value
    })

df_pipeline = pd.DataFrame(pipeline_data)
df_pipeline.to_csv('solar_pipeline.csv', index=False)
print("solar_pipeline.csv created.")