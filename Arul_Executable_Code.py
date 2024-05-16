#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import seaborn as sns
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt

#retrieving data
Data = pd.read_csv("C:\\Users\\91978\\Desktop\\important\\supermarket_sales.csv")
Data


Data['Date'] = pd.to_datetime(Data['Date'])
Data['year'] = Data['Date'].dt.year

# Sales data categorized by year
yearly_sales = Data.groupby('year')['Total'].sum()
print(yearly_sales)


#Sales data categorized by month
Data['month'] = Data['Date'].dt.month
monthly_sales = Data.groupby('month')['Total'].sum()
print(monthly_sales)


#Sales data categorized by gender
sales_by_gender = Data.groupby('Gender')['Total'].sum()
print(sales_by_gender)


#Sales data categorized by city
sales_by_city = Data.groupby('City')['Total'].sum()
print(sales_by_city)


#Sales data categorized by payment type
sales_by_payment = Data.groupby('Payment')['Total'].sum()
print(sales_by_payment)


#Sales data categorized by product line, including gross income
sales_by_productline = Data.groupby('Product line')['gross income'].sum()
print(sales_by_productline)


#Trend analysis of sales over time

analysis_sales = Data.groupby('month')['Total'].sum()
print(monthly_sales)


#Average ratings for each product line.
Average_rating_product_line = Data.groupby('Product line')['Rating'].mean()
print(Average_rating_product_line)



# Plot 1: Sales data categorized by year
print("\033[1m\033[31mTotal Sales Data Categorized by Year:\033[10m") 
for year, sales in yearly_sales.items():
    print(f"\033[34mYear {year}:\033[0m \033[32m${sales:,.2f}\033[0m")

# Create subplots for the dashboard
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 15))


#Plot2: Sales data categorized by month
axs[0, 0].bar(monthly_sales.index, monthly_sales.values, color='skyblue')
axs[0, 0].set_title('Sales data categorized by month')
axs[0, 0].set_xlabel('month')
axs[0, 0].set_ylabel('Total Sales')
axs[0, 0].grid(axis='y')

#Plot3:Sales data categorized by gender
axs[0, 1].pie(sales_by_gender.values, labels=sales_by_gender.index, autopct='%1.1f%%', startangle=140)
axs[0, 1].set_title('Sales data categorized by gender')
plt.axis('equal')


#Plot4: Sales data categorized by city
axs[1, 0].bar(sales_by_city.index, sales_by_city.values, color='skyblue')
axs[1, 0].set_title('Sales data categorized by city')
axs[1, 0].set_xlabel('city')
axs[1, 0].set_ylabel('Total Sales')
axs[1, 0].grid(axis='y')

#plot5: Sales data categorized by payment type
axs[1, 1].pie(sales_by_payment.values, labels=sales_by_payment.index, autopct='%1.1f%%', startangle=140)
axs[1, 1].set_title('Sales data categorized by payment type')
plt.axis('equal')

#plot6:Sales data categorized by product line, including gross income
plt.figure(figsize=(10, 6))
sales_by_productline.plot(kind='bar', color='skyblue')
plt.title('Sales data categorized by product line, including gross income')
plt.xlabel('Product Line')
plt.ylabel('Gross Income')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')
plt.tight_layout()
plt.show()

#plot7 L: Trend analysis of sales over time
Data['Date'] = pd.to_datetime(Data['Date'])
plt.figure(figsize=(10, 6))
sns.lineplot(data=Data, x='Date', y='Total', marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total')
plt.grid(True)
plt.show()
warnings.simplefilter(action='ignore', category=FutureWarning)


#plot8: Average ratings for each product line.


plt.figure(figsize=(10, 6))
Average_rating_product_line.plot(kind='bar', color='skyblue')
plt.title('Average Rating for Each Product Line')
plt.xlabel('Product Line')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')
plt.tight_layout()
plt.show()





