import pandas as pd
import matplotlib.pyplot as plt

class DataLoader:
    @staticmethod
    def load_data(file_path):
        return pd.read_excel(file_path)

class DataAnalysis:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
        return self.df.isnull().sum()

    def summary_statistics(self):
        return {
            'mean': self.df.mean(numeric_only=True),
            'median': self.df.median(numeric_only=True),
            'mode': self.df.mode(numeric_only=True)
        }

    def get_unique_counts(self):
        return {
            'product_categories': self.df['Product_Category'].nunique(),
            'product_sub_categories': self.df['Sub_Category'].nunique(),
            'products': self.df['Product'].nunique()
        }

class Visualizations:
    def __init__(self, df):
        self.df = df

    def plot_age_distribution(self):
        self.df['Customer_Age'] = pd.to_numeric(self.df['Customer_Age'], errors='coerce')
        df_filtered = self.df.dropna(subset=['Customer_Age'])
        plt.figure(figsize=(10, 6))
        plt.hist(df_filtered['Customer_Age'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Age distribution of Customers', fontsize=16)
        plt.xlabel('Customer Age', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    def plot_gender_distribution(self):
        gender_counts = self.df['Customer_Gender'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
        plt.title('Gender Distribution', fontsize=16)
        plt.show()

    def plot_revenue_by_age_group(self):
        bins = [0, 25, 34, 64, 100]
        labels = ['Youth (<25)', 'Young Adults (25-34)', 'Adults (35-64)', 'Seniors (64+)']
        self.df['Age_Group'] = pd.cut(self.df['Customer_Age'], bins=bins, labels=labels, right=False, include_lowest=True)
        age_group_revenue = self.df.groupby('Age_Group', observed=False)['Revenue'].sum()

        plt.figure(figsize=(10, 6))
        plt.bar(age_group_revenue.index.astype(str), age_group_revenue.values, color='skyblue', edgecolor='black')
        plt.title('Total Revenue by Age Group', fontsize=16)
        plt.xlabel('Age Group', fontsize=14)
        plt.ylabel('Total Revenue', fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_profit_by_category(self):
        category_profit = self.df.groupby('Product_Category')['Profit'].sum()
        plt.figure(figsize=(10, 6))
        category_profit.sort_values().plot(kind='barh', color='skyblue', edgecolor='black')
        plt.title('Profits by Product Category', fontsize=16)
        plt.xlabel('Total Profit', fontsize=14)
        plt.ylabel('Product Category', fontsize=14)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def plot_revenue_profit_trends(self, start_date, end_date):
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        self.df['Revenue'] = pd.to_numeric(self.df['Revenue'], errors='coerce')
        self.df['Profit'] = pd.to_numeric(self.df['Profit'], errors='coerce')

        filtered_df = self.df[(self.df['Date'] >= start_date) & (self.df['Date'] <= end_date)]
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

class ProfitAnalysis:
    def __init__(self, df):
        self.df = df

    def get_profitable_categories(self):
        category_profit = self.df.groupby('Product_Category')['Profit'].sum()
        most_profitable = category_profit.idxmax()
        most_profitable_profit = category_profit.max()
        least_profitable = category_profit.idxmin()
        least_profitable_profit = category_profit.min()

        return {
            'most_profitable': (most_profitable, most_profitable_profit),
            'least_profitable': (least_profitable, least_profitable_profit)
        }

    def plot_profit_margin(self):
        self.df['Profit_Margin'] = (self.df['Profit'] / self.df['Revenue']) * 100
        average_profit_margin = self.df.groupby('Product')['Profit_Margin'].mean()

        plt.figure(figsize=(50, 10))
        plt.scatter(average_profit_margin.index, average_profit_margin.values, color='skyblue', edgecolor='black')
        plt.title('Average Profit Margin per Product', fontsize=16)
        plt.xlabel('Product', fontsize=14)
        plt.ylabel('Average Profit Margin (%)', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_profit_margin_with_size(self):
        self.df['Profit_Margin'] = (self.df['Profit'] / self.df['Revenue']) * 100
        average_profit_margin = self.df.groupby('Product')['Profit_Margin'].mean()
        total_profit = self.df.groupby('Product')['Profit'].sum()

        plt.figure(figsize=(60, 8))
        plt.scatter(average_profit_margin.index, average_profit_margin.values, s=total_profit.values / 100, color='skyblue', edgecolor='black', alpha=0.7)
        plt.title('Average Profit Margin per Product with Profit as Marker Size', fontsize=16)
        plt.xlabel('Product', fontsize=14)
        plt.ylabel('Average Profit Margin (%)', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    file_path = "/Users/srisabarish/Downloads/sales_data.xlsx"
    df = DataLoader.load_data(file_path)

    analysis = DataAnalysis(df)
    print(analysis.check_missing_values())
    print(analysis.summary_statistics())
    print(analysis.get_unique_counts())

    visualizations = Visualizations(df)
    visualizations.plot_age_distribution()
    visualizations.plot_gender_distribution()
    visualizations.plot_revenue_by_age_group()
    visualizations.plot_profit_by_category()

    start_date = pd.Timestamp(year=2023, month=1, day=1)
    end_date = pd.Timestamp(year=2023, month=12, day=31)
    visualizations.plot_revenue_profit_trends(start_date, end_date)

    profit_analysis = ProfitAnalysis(df)
    print(profit_analysis.get_profitable_categories())
    profit_analysis.plot_profit_margin()
    profit_analysis.plot_profit_margin_with_size()
