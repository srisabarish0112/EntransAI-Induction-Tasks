# Data Analysis Project

## **Objective**

The primary objective of this project is to analyze a dataset containing customer demographics, product categories, and financial data. The goal is to uncover key insights regarding customer behavior, product performance, and financial trends, which can be utilized for better decision-making and strategic planning. The analysis includes exploring customer age, gender distribution, product profitability, and trends in revenue and profits over time.

---

## **Procedure**

### 1. **Import Data and Preprocessing**
   - **Functions Used**: 
     - `pandas.read_excel()`: Load data from Excel.
     - `.info()`: Check data types and identify inconsistencies.
     - `.isnull().sum()`: Identify missing values.
     - `.fillna()` / `.dropna()`: Handle missing data.
     - `.to_pickle()`: Save cleaned data for future use.
   - **Process**:
     - Loaded the dataset and checked for data consistency.
     - Handled missing values by filling or dropping rows/columns.
     - Saved the cleaned dataframe for further analysis.

### 2. **Summary Statistics**
   - **Functions Used**:
     - `.mean()`, `.median()`, `.mode()`: Calculate central tendency measures.
     - `.describe()`: Generate summary statistics (mean, std, min, max).
   - **Process**:
     - Calculated key statistics for numeric columns, providing insights into the overall distribution of data.

### 3. **Histogram of Customer Age**
   - **Functions Used**:
     - `matplotlib.pyplot.hist()`: Create histogram.
     - `plt.xlabel()`, `plt.ylabel()`, `plt.title()`: Label the plot.
   - **Process**:
     - Visualized the distribution of customer ages to identify any patterns or outliers.
   
   ![Histogram](https://github.com/user-attachments/assets/764bd616-7bdf-4c99-a150-b1e2f1f00bcd)

### 4. **Gender Distribution**
   - **Functions Used**:
     - `.value_counts()`: Count occurrences of each gender.
     - `plot(kind='pie')` or `sns.countplot()`: Create pie chart or bar chart.
   - **Process**:
     - Represented the gender distribution either as a percentage or frequency.

   ![Piechart](https://github.com/user-attachments/assets/b69b4554-8d7b-44cb-9f30-48d933a3088b)

### 5. **Age Group and Revenue Relationship**
   - **Functions Used**:
     - `sns.barplot()`: Create bar chart.
     - `.groupby()`: Aggregate revenue by age group.
   - **Process**:
     - Grouped data by age groups and summed revenue for each group.
     - Visualized the relationship between age group and revenue using a bar chart.

   ![Barchart](https://github.com/user-attachments/assets/18ed2bcc-a579-4a48-b713-6f3317570b25)

### 6. **Most and Least Profitable Product Category**
   - **Functions Used**:
     - `.groupby()`: Aggregate total profits by category.
     - `.plot(kind='barh')`: Create horizontal bar chart.
   - **Process**:
     - Summed up profits for each product category.
     - Visualized categories to easily identify the most and least profitable ones.

   ![Profit](https://github.com/user-attachments/assets/65763b1c-9a12-4fd3-b5cc-0eb9e22a05a9)

### 7. **Revenue and Profit Trends Over Time**
   - **Functions Used**:
     - `pd.to_datetime()`, `.dt.to_period('M')`: Convert dates to month-year format.
     - `.groupby()`: Aggregate revenue and profit per month.
     - `plt.plot()`: Plot trends over time.
   - **Process**:
     - Analyzed and visualized monthly trends in revenue and profit based on user-specified time periods.

   ![Trends](https://github.com/user-attachments/assets/d9d21354-00e1-47c3-9ac0-49abc4b60ede)

### 8. **Average Profit Margin per Product**
   - **Functions Used**:
     - `.groupby()`: Aggregate revenue and profit per product.
     - Calculate profit margin: `(Profit / Revenue) * 100`.
     - `sns.scatterplot()`: Plot profit margins with size and color variations.
   - **Process**:
     - Calculated profit margins for each product.
     - Plotted profit margins against products with marker size representing profit levels.

   ![Average](https://github.com/user-attachments/assets/8ef6bf4e-296b-4a4c-9579-a0a7b1a8b4da)

### 9. **Sub-Category Performance within Product Categories**
   - **Functions Used**:
     - `.groupby()`: Aggregate revenue and profit by category and sub-category.
     - `.unstack()`: Prepare data for stacking.
     - `.plot(kind='bar', stacked=True)`: Create stacked bar charts.
   - **Process**:
     - Grouped data by product category and sub-category.
     - Visualized performance using stacked bar charts to show contributions of sub-categories within each product category.

   ![Subcategory](https://github.com/user-attachments/assets/7cdd4d71-f63a-4bd3-8add-571093b2692e)

---

## **Results**

### 1. **Summary Statistics**
   - Central tendency measures (mean, median, mode) were calculated for numeric columns, offering insights into the distribution of data.

### 2. **Customer Age Distribution**
   - The histogram revealed key patterns and potential outliers in customer age, which can help in targeted marketing strategies.

### 3. **Gender Distribution**
   - The gender distribution chart illustrated the balance (or imbalance) between male and female customers, aiding in understanding the target market.

### 4. **Revenue by Age Group**
   - The bar chart displayed the relationship between different age groups and their respective revenue contributions, highlighting valuable customer segments.

### 5. **Profitable Product Categories**
   - The horizontal bar chart helped easily identify the most and least profitable product categories, essential for product optimization and business strategy.

### 6. **Revenue and Profit Trends**
   - The line plot revealed key trends in revenue and profit over time, offering insights into seasonality or the impact of specific events on business performance.

### 7. **Profit Margins by Product**
   - The scatter plot provided a clear view of profit margins across products, with the size/color variation representing profit levels, which aids in identifying high-margin products.

### 8. **Sub-Category Performance**
   - Stacked bar charts allowed examination of sub-category performance within each product category, helping to identify areas of strength and improvement.

