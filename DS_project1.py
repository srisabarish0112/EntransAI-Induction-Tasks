import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    return pd.read_excel(file_path)

# Check for missing values
def check_missing_values(df):
    return df.isnull().sum()

# Calculate summary statistics
def summary_statistics(df):
    return {
        'mean': df.mean(numeric_only=True),
        'median': df.median(numeric_only=True),
        'mode': df.mode(numeric_only=True)
    }

# Get the count of unique categories
def get_unique_counts(df):
    return {
        'product_categories': df['Product_Category'].nunique(),
        'product_sub_categories': df['Sub_Category'].nunique(),
        'products': df['Product'].nunique()
    }

# Plot customer age distribution
def plot_age_distribution(df):
    df['Customer_Age'] = pd.to_numeric(df['Customer_Age'], errors='coerce')
    df = df.dropna(subset=['Customer_Age'])
    
    plt.figure(figsize=(10,6))
    plt.hist(df['Customer_Age'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Age distribution of Customers', fontsize=16)
    plt.xlabel('Customer Age', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Plot gender distribution
def plot_gender_distribution(df):
    gender_counts = df['Customer_Gender'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
    plt.title('Gender Distribution', fontsize=16)
    plt.show()

# Plot total revenue by age group
def plot_revenue_by_age_group(df):
    bins = [0, 25, 34, 64, 100]
    labels = ['Youth (<25)', 'Young Adults (25-34)', 'Adults (35-64)', 'Seniors (64+)']
    df['Age_Group'] = pd.cut(df['Customer_Age'], bins=bins, labels=labels, right=False, include_lowest=True)
    age_group_revenue = df.groupby('Age_Group', observed=False)['Revenue'].sum()

    plt.figure(figsize=(10, 6))
    plt.bar(age_group_revenue.index.astype(str), age_group_revenue.values, color='skyblue', edgecolor='black')
    plt.title('Total Revenue by Age Group', fontsize=16)
    plt.xlabel('Age Group', fontsize=14)
    plt.ylabel('Total Revenue', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plot profits by product category
def plot_profit_by_category(df):
    category_profit = df.groupby('Product_Category')['Profit'].sum()
    plt.figure(figsize=(10, 6))
    category_profit.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
    plt.title('Profits by Product Category', fontsize=16)
    plt.xlabel('Total Profit', fontsize=14)
    plt.ylabel('Product Category', fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Get most and least profitable product categories
def get_profitable_categories(df):
    category_profit = df.groupby('Product_Category')['Profit'].sum()
    most_profitable = category_profit.idxmax()
    most_profitable_profit = category_profit.max()
    least_profitable = category_profit.idxmin()
    least_profitable_profit = category_profit.min()

    return {
        'most_profitable': (most_profitable, most_profitable_profit),
        'least_profitable': (least_profitable, least_profitable_profit)
    }

# Plot revenue and profit trends over time
def plot_revenue_profit_trends(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    filtered_df.set_index('Date', inplace=True)
    monthly_data = filtered_df.resample('ME').agg({'Revenue': 'sum', 'Profit': 'sum'})

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_data.index, monthly_data['Revenue'], label='Revenue', color='skyblue', marker='o')
    plt.plot(monthly_data.index, monthly_data['Profit'], label='Profit', color='green', marker='o')
    plt.title(f"Revenue and Profit Trends from {start_date.strftime('%m/%Y')} to {end_date.strftime('%m/%Y')}", fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Amount', fontsize=14)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(monthly_data.index, monthly_data.index.strftime('%b-%Y'), rotation=45)
    plt.tight_layout()
    plt.show()

# Calculate and plot profit margin
def plot_profit_margin(df):
    df['Profit_Margin'] = (df['Profit'] / df['Revenue']) * 100
    average_profit_margin = df.groupby('Product')['Profit_Margin'].mean()

    plt.figure(figsize=(50, 10))
    plt.scatter(average_profit_margin.index, average_profit_margin.values, color='skyblue', edgecolor='black')
    plt.title('Average Profit Margin per Product', fontsize=16)
    plt.xlabel('Product', fontsize=14)
    plt.ylabel('Average Profit Margin (%)', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot average profit margin with profit size
def plot_profit_margin_with_size(df):
    average_profit_margin = df.groupby('Product')['Profit_Margin'].mean()
    total_profit = df.groupby('Product')['Profit'].sum()

    plt.figure(figsize=(60, 8))
    plt.scatter(average_profit_margin.index, average_profit_margin.values, s=total_profit.values / 100, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Average Profit Margin per Product with Profit as Marker Size', fontsize=16)
    plt.xlabel('Product', fontsize=14)
    plt.ylabel('Average Profit Margin (%)', fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Create a pivot table for revenue and profit by category and sub-category
def create_category_subcategory_pivot(df):
    grouped_data = df.groupby(['Product_Category', 'Sub_Category']).agg({'Revenue': 'sum', 'Profit': 'sum'}).reset_index()
    pivot_revenue = grouped_data.pivot(index='Product_Category', columns='Sub_Category', values='Revenue').fillna(0)
    pivot_profit = grouped_data.pivot(index='Product_Category', columns='Sub_Category', values='Profit').fillna(0)
    
    pivot_revenue.plot(kind='bar', stacked=True, figsize=(12, 8), cmap='tab20')
    plt.title('Revenue by Product Category and Sub-Category', fontsize=16)
    plt.xlabel('Product Category', fontsize=14)
    plt.ylabel('Total Revenue', fontsize=14)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "/Users/srisabarish/Downloads/sales_data.xlsx"
    df = load_data(file_path)
    
    print(check_missing_values(df))
    print(summary_statistics(df))
    print(get_unique_counts(df))
    
    plot_age_distribution(df)
    plot_gender_distribution(df)
    plot_revenue_by_age_group(df)
    plot_profit_by_category(df)
    print(get_profitable_categories(df))
    
    start_date = pd.Timestamp(year=2023, month=1, day=1)
    end_date = pd.Timestamp(year=2023, month=12, day=31)
    plot_revenue_profit_trends(df, start_date, end_date)
    
    plot_profit_margin(df)
    plot_profit_margin_with_size(df)
    create_category_subcategory_pivot(df)
