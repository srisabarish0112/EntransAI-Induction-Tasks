** STRUCTURED SUMMARY OF THE PROJECT ** 


1. Import Data and Preprocessing
Functions Used:
pandas.read_excel() to load data from Excel.
.info() to check data types.
.isnull().sum() to identify null values.
.fillna() or .dropna() to handle missing data.
.to_pickle() to save the processed data.

Process:
Loaded the dataset and checked for datatype consistency.
Addressed missing values either by filling with appropriate values or dropping rows/columns.
Saved the cleaned dataframe for future use.

2. Summary Statistics

Functions Used:
.mean(), .median(), .mode() for central tendency measures.
.describe() for overall statistics like mean, std, min, max.

Process:
Generated summary statistics for numeric columns.
Highlighted key insights such as average and median values.



3. Histogram of Customer Age

Functions Used:
matplotlib.pyplot.hist() to create the histogram.
plt.xlabel(), plt.ylabel(), and plt.title() to label the plot.

Process:
Visualized the distribution of customer ages to identify patterns or outliers.
Customized the bins and colors for clarity.

![Histogram](https://github.com/user-attachments/assets/764bd616-7bdf-4c99-a150-b1e2f1f00bcd)


4. Gender Distribution

Functions Used:
.value_counts() to count occurrences of each gender.
plot(kind='pie') for pie chart or sns.countplot() for bar chart.

Process:
Represented gender distribution as a percentage or frequency.
Chose the appropriate chart based on visualization requirements.

![Piechart](https://github.com/user-attachments/assets/b69b4554-8d7b-44cb-9f30-48d933a3088b)

5. Age Group and Revenue Relationship

Functions Used:
sns.barplot() to create a bar chart.
.groupby() to aggregate revenue by age group.

Process:
Grouped data by age groups and summed up revenue for each group.
Used a bar chart to display the relationship between age group and revenue.

![Barchart](https://github.com/user-attachments/assets/18ed2bcc-a579-4a48-b713-6f3317570b25)

6. Most and Least Profitable Product_Category

Functions Used:
.groupby() to calculate total profits by category.
.plot(kind='barh') to create a horizontal bar chart.

Process:
Summed up profits for each product category.
Visualized categories to easily identify the most and least profitable ones.

![Profit](https://github.com/user-attachments/assets/65763b1c-9a12-4fd3-b5cc-0eb9e22a05a9)


7. Revenue and Profit Trends Over Time

Functions Used:
pd.to_datetime() and .dt.to_period('M') to convert dates into month-year format.
.groupby() to sum revenue and profit per month.
plt.plot() for line plots.

Process:
Took user inputs for start and end periods.
Filtered data for the specified range and analyzed monthly trends in revenue and profit.
Visualized trends using line plots.

![Trends](https://github.com/user-attachments/assets/d9d21354-00e1-47c3-9ac0-49abc4b60ede)


8. Average Profit Margin per Product

Functions Used:
.groupby() to aggregate revenue and profit per product.
Calculated profit margin as (Profit / Revenue) * 100.
sns.scatterplot() for scatter plots with size and color variation.

Process:
Computed profit margins for products.
Plotted profit margins against products, with marker size representing profit levels.

![average](https://github.com/user-attachments/assets/8ef6bf4e-296b-4a4c-9579-a0a7b1a8b4da)


9. Sub_Category Performance within Product Categories

Functions Used:
.groupby() to sum revenue and profit by product category and sub-category.
.unstack() to prepare data for stacking.
.plot(kind='bar', stacked=True) to create stacked bar charts.

Process:
Grouped data by product category and sub-category.
Calculated total revenue and profit for each sub-category.
Used stacked bar charts to represent contributions of sub-categories within each category.

![subcategory](https://github.com/user-attachments/assets/7cdd4d71-f63a-4bd3-8add-571093b2692e)



