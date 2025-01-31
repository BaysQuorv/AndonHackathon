import pandas as pd
import matplotlib.pyplot as plt

# Create figure and axis with a good size
plt.figure(figsize=(12, 6))

# Read the CSV file
df = pd.read_csv('moral_threshold_results.csv')

# Create binary values and calculate mean response for each amount
df['binary_response'] = (df['response'] == 'yes').astype(float)  # Using float for mean calculation
avg_responses = df.groupby('amount')['binary_response'].mean().reset_index()

# Create the main plot
plt.plot(avg_responses['amount'], avg_responses['binary_response'], 'bo-', linewidth=2, markersize=8)

# Set x-axis to logarithmic scale
plt.xscale('log', base=2)

# Customize the plot
plt.grid(True, alpha=0.3)
plt.xlabel('Amount ($)', fontsize=12)
plt.ylabel('Average Response (0=No, 1=Yes)', fontsize=12)
plt.title('AI Moral Decision: Taking Money vs Amount (Average of 10 Trials)', fontsize=14)

# Add amount labels at each point
for i, row in avg_responses.iterrows():
    plt.annotate(f'${int(row["amount"])}\n({row["binary_response"]:.2f})', 
                (row['amount'], row['binary_response']),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')

# Adjust layout to prevent label clipping
plt.tight_layout()

# Save the plot
plt.savefig('moral_threshold_plot_10_trials.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plot has been saved as 'moral_threshold_plot_10_trials.png'") 