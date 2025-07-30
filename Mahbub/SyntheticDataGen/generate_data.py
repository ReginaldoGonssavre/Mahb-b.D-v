import pandas as pd
import numpy as np
from sdv.tabular import GaussianCopula

# Sample data
data = pd.DataFrame({
    'user_id': np.arange(100),
    'feature1': np.random.rand(100),
    'feature2': np.random.randint(0, 2, 100)
})

# Create a model and generate synthetic data
model = GaussianCopula()
model.fit(data)
synthetic_data = model.sample(num_rows=500)

# Save to a csv file
synthetic_data.to_csv('synthetic_data.csv', index=False)

print("Synthetic data generated and saved to synthetic_data.csv")