# ==========================================
# Retail Superstore Sales Analysis Project
# ==========================================

# Import Libraries
# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Create Images Folder (Only Once)
os.makedirs("Images", exist_ok=True)

# Display all columns
pd.set_option("display.max_columns", None)

print("Libraries Imported Successfully!")
# Load Dataset
df = pd.read_csv("Dataset/Superstore_Messy.csv")

print("\nDataset Loaded Successfully!")

# Show first 5 rows
print(df.head())
# ================================
# Dataset Information
# ================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns)

print("\nStatistical Summary:")
print(df.describe())
# ================================
# Missing Values Check
# ================================

print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# ================================
# Duplicate Records
# ================================

print("\nDuplicate Records:")
print(df.duplicated().sum())
# ================================
# Data Cleaning
# ================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
# ================================
# Total Sales and Profit
# ================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nTotal Sales:")
print(round(total_sales, 2))

print("\nTotal Profit:")
print(round(total_profit, 2))
# ================================
# Category-wise Sales Analysis
# ================================

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

# Bar Chart
plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.savefig("Images/category_sales.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ================================
# State-wise Sales (Top 10)
# ================================

state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 States by Sales:")
print(state_sales)

plt.figure(figsize=(12,6))
state_sales.plot(kind="bar")

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.savefig("Images/top10_states_sales.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ================================
# Segment-wise Sales Analysis
# ================================

segment_sales = df.groupby("Segment")["Sales"].sum()

print("\nSegment-wise Sales:")
print(segment_sales)

plt.figure(figsize=(8,5))

segment_sales.plot(kind="bar", color="green")

plt.title("Segment-wise Sales")
plt.xlabel("Segment")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.savefig("Images/segment_sales.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ==============================
# Region-wise Sales
# ==============================

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nRegion-wise Sales:")
print(region_sales)

plt.figure(figsize=(8,5))

region_sales.plot(kind="bar", color="orange")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.savefig("Images/region_sales.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ==============================
# Monthly Sales Trend
# ==============================

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Month-Year column
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

plt.figure(figsize=(14,6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=90)

plt.grid(True)
plt.savefig("Images/monthly_sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ==============================
# Top 10 Products by Sales
# ==============================

product_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Sales:")
print(product_sales)

plt.figure(figsize=(12,6))

product_sales.plot(kind="bar", color="purple")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=75)

plt.tight_layout()
plt.savefig("Images/top10_products_sales.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ==============================
# Category-wise Profit
# ==============================

category_profit = df.groupby("Category")["Profit"].sum()

print("\nCategory-wise Profit:")
print(category_profit)

plt.figure(figsize=(8,5))

category_profit.plot(kind="bar", color=["blue", "green", "red"])

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.savefig("Images/category_profit.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()
# ==============================
# Sales vs Profit Scatter Plot
# ==============================

plt.figure(figsize=(10,6))

plt.scatter(df["Sales"], df["Profit"], alpha=0.5, color="blue")

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.grid(True)
plt.savefig("Images/sales_vs_profit_scatter.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

