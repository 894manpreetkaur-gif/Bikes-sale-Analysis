import streamlit as st
import pandas as pd

st.title("Bike Sales Analysis")

tab1, tab2, tab3 = st.tabs(["Project Overview ","Dataset Overview","Data Analysis"])

with tab1:
    import streamlit as st

    st.subheader("📌 Description", divider=True)
    st.write("""
             The ***Bike Sales Data Analysis*** project focuses on examining sales transactions of bikes across different countries, customer age groups, and product categories. The dataset contains detailed information about customer demographics, product specifications, order quantity, cost, revenue, and profit.

     This project aims to analyze sales performance, understand customer purchasing behavior, and identify key factors influencing revenue and profit generation. Using data analysis techniques, the project helps derive meaningful business insights that can support strategic decision-making.

     The dataset contains `89` records and `19` features, covering sales transactions from `December 2021`.
    """)

    st.subheader("🎯Objective", divider=True)
    st.write(
    """The main objectives of this project are:\n
    1. Analyze Sales Performance

        ➙ Calculate total revenue, total cost, and total profit.

        ➙ Identify high-performing products and regions.

        ➙ Customer Demographic Analysis

    2. Analyze sales based on age group (Youth, Adults, Seniors).

        ➙ Compare purchasing patterns by gender.

        ➙ Identify which age group generates the most revenue.

    3. Product Analysis

        ➙ Examine product categories and sub-categories.

        ➙ Identify best-selling bike models.

        ➙ Analyze profit margins per product.

    4. Geographical Analysis

        ➙ Compare sales across countries and states.

        ➙ Identify top revenue-generating regions.

    5. Order & Quantity Insights

        ➙ Study order quantity distribution.

        ➙ Analyze relationship between quantity, cost, and revenue.
    """)

    st.subheader("🚀Future Scope", divider=True)
    st.write(
        """This project can be expanded further in the following ways:

    1. Predictive Analysis

        ➙ Use Machine Learning models to predict future sales.

        ➙ Forecast revenue trends.

    2. Customer Segmentation

        ➙ Apply clustering techniques to identify customer segments.

        ➙ Personalized marketing strategies.

    3. Profit Optimization Model

        ➙ Identify optimal pricing strategies.

        ➙ Analyze cost reduction strategies.

    4. Dashboard Development
 
        ➙ Build interactive dashboards using:

            ➛ Power BI

            ➛ Tableau

            ➛ Streamlit (Python)

    5. Time-Series Analysis

        ➙ If more historical data is available, perform monthly/yearly sales trend analysis.

    6. Inventory Optimization

        ➙ Predict demand to manage stock efficiently.
    """)

    st.subheader("Data Resource",divider = True)
    st.write(
        """The Bike Sales dataset used in this project was obtained from Kaggle.
    It contains customer demographics, order details, and revenue information, which are used to perform exploratory data analysis and build interactive visualizations.
    """)


with tab2:
    df = pd.read_excel("bike_sales.xlsx")
    st.subheader("Dataset View", divider=True)
    st.dataframe(df)

    # (d) Dataset Explanation
    st.subheader("Dataset Explanation", divider=True)
    
    # 1. Columns and Rows Count
    dataset_shape = df.shape
    st.write("Total number of Rows:-`{r}` and Total number of Columns:-`{c}`".format(r=dataset_shape[0],c=dataset_shape[1]))

    # 2.Duplicate Values
    st.subheader(" Total number of Duplicate values:- `{}` ".format(df.duplicated().sum()))
    st.write()
    
    # 3.Missing Values & Information of dataframe
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Data of Missing values ")
        missing_data = df.isnull().sum()
        st.dataframe(missing_data)

    with right_column:
        st.subheader("Full Statistics of Dataset ")
        dataset_info = df.describe()
        st.write(dataset_info)

    # 5. Types of Columns

    st.subheader(" Types of Column")
    st.write(df.dtypes)        
 


with tab3:
    import plotly.express as px
    import matplotlib.pyplot as plt

    # Pie chart
    fig1 = px.pie(df,values="Order_Quantity", names="Age_Group" , title = " 1. Bike Purchasing According to Age Group")
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""

This pie chart shows how **bike purchases are distributed among different age groups**.

- **Adults (35–64)** account for **52.4%** of purchases, making them the **largest group of buyers**.
- **Young Adults (25–34)** represent **32.6%** of total purchases and form the **second largest customer group**.
- **Youth (<25)** contribute **14.4%**, showing a **smaller share of bike purchases**.
- A small portion (**0.53%**) represents **missing or null age data** in the dataset.

**Key Insight:**  
Most bikes are purchased by **Adults and Young Adults**, indicating these groups are the **primary target customers for bike sales**.
             """)

    # Scatterplot
    fig2= px.scatter(df,x= " Cost ",y=" Profit ", title="2. Bikes Purchasing according to the Customer Gender",size=" Profit ",color=" Profit ")
    st.plotly_chart(fig2, use_container_width =True)
    st.write("""
This scatterchart shows the **relationship between Cost and Profit** for bike purchases based on **customer gender**.  
Each bubble represents a data point where:

- **X-axis (Cost)** represents the cost of the bike.
- **Y-axis (Profit)** shows the profit earned from the sale.
- **Bubble size** indicates the **number of purchases / sales volume**.
- **Color intensity** represents the **profit level**, where lighter colors show higher profit.

**Key Insight:**  
Higher-priced bikes tend to generate **greater profit and sales value**, indicating that **premium bikes contribute significantly to overall business profit**.
""")
    
    # Bar Chart
    fig3 = px.bar(df, x= "Country", y="Order_Quantity", title="3. Country Wise Bike Purchases")
    st.plotly_chart(fig3, use_container_width=True)
    st.write("""
This bar chart shows the **number of bike purchases (order quantity) in different countries**.

- The **United States** has a high number of bike purchases, showing strong demand in this market.
- **Australia** records the **highest number of purchases**, indicating it is the **largest market for bike sales** in the dataset.
- **France** also shows a moderate number of purchases compared to other countries.
- **United Kingdom, Germany, and Canada** have **moderate purchase levels**, contributing to overall sales.
- Some countries show **very low purchase quantities**, indicating smaller market demand.

**Key Insight:**  
Australia and the United States contribute significantly to total bike sales, suggesting these regions are **major markets for the bike business**.
""")
    #  Multi-line chart
    fig4= px.data.gapminder()
    fig4 = px.area(df,x="Country",y= " Profit ", title = "4. Country Wise Profit from different bike products",  color="Product_Description", line_group=" Profit ")
    st.plotly_chart(fig4, use_container_width = True)
    st.write("""
This multi-line chart shows the **profit generated from different bike products across various countries**.
             
- **Australia** shows the highest profit values, indicating it is the most profitable market for bike sales.
- The **United States** also generates high profit, showing strong market demand.
- **France** records a moderate level of profit compared to the top countries.
- **Germany and Canada** contribute moderate profit levels to the overall sales.
- **United Kingdom** shows lower profit values compared to other countries.
             
**Key Insight:**\n
Australia and the United States contribute the highest share of profit, making them the **most important markets for the bike business**.
""")

    # Histogram
    fig5 = px.histogram(df,x="Product_Description",y="Order_Quantity",color = "State",barmode ="stack",title="5. Bikes Purchasing according to the Customer Gender and Product Tupes")
    st.plotly_chart(fig5, use_container_width = True)
    st.write("""
This bar chart shows the **number of bikes purchased based on different product types and customer gender**.

- Some bike models show higher purchase quantities, indicating they are more popular among customers.
- **Mountain bike** variants appear frequently with higher order quantities compared to other models.
- Purchases are distributed across multiple regions (states), showing demand in different locations.
- Certain products have lower order quantities, suggesting lower customer preference for those models.
- The chart indicates variation in purchasing patterns across different bike types and regions.

**Key Insight:**\n
A few specific mountain bike models generate the majority of purchases, indicating that **these products are most preferred by customers and drive the highest demand in the market**.
             """)

#
#
#
#
#