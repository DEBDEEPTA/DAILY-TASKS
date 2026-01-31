"""
(Retail Analytics)
NumPy (Intermediate)
     A retail company records daily sales of 5 products across 30 days in a 2D NumPy array of shape (30, 5).
     Due to a system error, negative values appear in the dataset.
    Task:
        Replace negative values with 0
        Compute the average weekly sales per product (assume 7 days = 1 week)
        Identify the product with the highest average weekly sales
"""
import numpy as np
def retail_analysis(retial_sales):

    # CLEANING DATA (replace negative values with 0)
    retial_sales = np.where(retial_sales < 0, 0, retial_sales)
    # -----------------------------
    # WEEKLY SALES (7 days = 1 week)
    # Use only first 28 days => 4 full weeks
    # -----------------------------

    # SLICING TO FIRST 28 DAYS FOR WEEKS
    retial_sales_whole_weeks= retial_sales[:28]

    # (weeks=4, days=7, products=5)
    weekly_sales = retial_sales_whole_weeks.reshape(4,7,5)

    # NEED TO CALCULATE WEEKLY SALES FOR EACH PRODUCT
    """
    ________________________________________________________________________________
    | Axis     | Meaning         | Works Along        | Result Size                |
    | -------- | --------------- | ------------------ | -------------------------- |
    | `axis=0` | **Column-wise** | Down the rows      | Output = number of columns |
    | `axis=1` | **Row-wise**    | Across the columns | Output = number of rows    |
    ________________________________________________________________________________
    """
    weekly_sales_sum_each_product = weekly_sales.sum(axis=1)

    avg_weekly_sales_per_product = weekly_sales_sum_each_product.mean(axis= 0)

    # argmax -> return the index of the maximum value
    max_avg_weekly_product = np.argmax(avg_weekly_sales_per_product)

    print(f"Average Weekly Sale per product: {avg_weekly_sales_per_product}")
    print(f"Products with highest average: {max_avg_weekly_product}")

if __name__=="__main__":

    # SETTING SAMPLE DATA
    retial_sales_data = np.full((30,5), 40)
    retial_sales_data[10][4] = -78 # SETTING 4TH PRODUCT OF 10TH DAY TO NEGATIVE VALUE
    retial_sales_data[5][2] = -3

    retial_sales_data[8] = -7   # SETTING ALL PRODUCTS OF 8TH DAY TO -7
    retial_sales_data[9] = 45   # SETTING ALL PRODUCTS OF 9TH DAY TO 45
    retial_sales_data[23] = 12  # SETTING ALL PRODUCTS OF 23 DAY TO 12

    retail_analysis(retial_sales_data)

