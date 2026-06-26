import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the clean master file we created
df = pd.read_csv("cleaned_master_marketing_data.csv")

print("📊 Generating project visualizations...")

# Set up a clean layout style for graphs
sns.set_theme(style="whitegrid")

# CHART 1: Top Cities by Coupon Usage
plt.figure(figsize=(10, 5))
# Filter for only burned coupons
burned_data = df[df['transaction_status'] == 'burned']
city_order = burned_data['city_name'].value_counts().index[:10]

sns.countplot(data=burned_data, y='city_name', order=city_order, palette='viridis')
plt.title('Top 10 Cities with the Most Used (Burned) Coupons', fontsize=14, pad=15)
plt.xlabel('Number of Used Coupons', fontsize=11)
plt.ylabel('City Name', fontsize=11)
plt.tight_layout()

# Save the plot as an image in your folder
plt.savefig('top_cities_coupon_usage.png', dpi=300)
plt.close()
print("💾 Saved chart: 'top_cities_coupon_usage.png'")

# CHART 2: Coupon Status Split by Gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='gender_name', hue='transaction_status', palette='muted')
plt.title('Coupon Engagement Split by Gender', fontsize=14, pad=15)
plt.xlabel('Gender', fontsize=11)
plt.ylabel('Transaction Count', fontsize=11)
plt.legend(title='Transaction Status')
plt.tight_layout()

# Save the second plot
plt.savefig('gender_coupon_engagement.png', dpi=300)
plt.close()
print("💾 Saved chart: 'gender_coupon_engagement.png'")

print("\n🎉 SUCCESS! Visualization images are ready in your folder.")
