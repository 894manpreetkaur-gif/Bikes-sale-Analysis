import streamlit as st
import pandas as pd

df = pd.read_excel("../bike_sales.xlsx")


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
    fig1 = px.pie(df,values="Order_Quantity", names="Age_Group" , title = " 1. Bikes Purchasing According to Age Group")
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""

**Explanation**: This pie chart shows how **bike purchases are distributed among different age groups**.
- **Adults (35–64)** account for **52.4%** of purchases, making them the **largest group of buyers**.
- **Young Adults (25–34)** represent **32.6%** of total purchases and form the **second largest customer group**.
- **Youth (<25)** contribute **14.4%**, showing a **smaller share of bike purchases**.
- A small portion (**0.53%**) represents **missing or null age data** in the dataset.

**🔑Key Insight**:\n 
Most bikes are purchased by **Adults and Young Adults**, indicating these groups are the **primary target customers for bike sales**.
             """)
    
    #Bar Chart
    fig2 = px.bar(df,x="Customer_Gender",y=" Profit ",title="2. Relationship bwtween Customer Gender and Profit")
    st.plotly_chart(fig2, use_container_width = True)
    st.write("""
**Explanation**: This chart shows the **the total profit contribution from each gender group**.
- **Female** customers (F) generated the **highest profit**, reaching around 98K.
- **Male** customers (M) generated **lower profit**, approximately 67K.
- The difference shows that female customers contributed significantly more to overall profit.
             
**🔑 Key Insight**:\n
Female customers generate significantly higher profit than male customers, making them the most valuable customer segment in this dataset.
             """)

    # Scatterplot
    fig3= px.scatter(df,x= " Cost ",y=" Profit ", title="3. The relationship between Cost and Profit for bike purchases",size=" Profit ",color=" Profit ")
    st.plotly_chart(fig3, use_container_width =True)
    st.write("""
**Explanation**: This scatterchart shows the **relationship between Cost and Profit** for bike purchases**. 
              
Each bubble represents a data point where:
- **X-axis (Cost)** represents the cost of the bike.
- **Y-axis (Profit)** shows the profit earned from the sale.
- **Bubble size** indicates the **number of purchases / sales volume**.
- **Color intensity** represents the **profit level**, where lighter colors show higher profit.

**🔑Key Insight:** \n
Higher-priced bikes tend to generate **greater profit and sales value**, indicating that **premium bikes contribute significantly to overall business profit**.
""")
    
   
    #  Multi-line chart
    fig4= px.data.gapminder()
    fig4 = px.area(df,x="Country",y= " Profit ", title = "4. Country Wise Profit ",  color="Product_Description", line_group=" Profit ")
    st.plotly_chart(fig4, use_container_width = True)
    st.write("""
**Explanation**: This multi-line chart shows the **profit generated from different countries**.
- **Australia** shows the highest profit values, indicating it is the most profitable market for bike sales.
- The **United States** also generates high profit, showing strong market demand.
- **France** records a moderate level of profit compared to the top countries.
- **Germany and Canada** contribute moderate profit levels to the overall sales.
- **United Kingdom** shows lower profit values compared to other countries.
             
**🔑Key Insight:**\n
Australia and the United States contribute the highest share of profit, making them the **most important markets for the bike business**.
""")
    
    # Bar Chart
    fig5 = px.bar(df, x= "Country", y="Order_Quantity", title="5. Country Wise Bike Purchases")
    st.plotly_chart(fig5, use_container_width=True)
    st.write("""
**Explanation**: This bar chart shows the **number of bike purchases (order quantity) in different countries**.

- The **United States** has a high number of bike purchases, showing strong demand in this market.
- **Australia** records the **highest number of purchases**, indicating it is the **largest market for bike sales** in the dataset.
- **France** also shows a moderate number of purchases compared to other countries.
- **United Kingdom, Germany, and Canada** have **moderate purchase levels**, contributing to overall sales.
- Some countries show **very low purchase quantities**, indicating smaller market demand.

**🔑Key Insight:**\n  
Australia and the United States contribute significantly to total bike sales, suggesting these regions are **major markets for the bike business**.
""")


    # Histogram
    fig6 = px.histogram(df,x="Product_Description",y="Order_Quantity",color = "State",barmode ="stack",title="6. Total order quantity for different bike products")
    st.plotly_chart(fig6, use_container_width = True)
    st.write("""
    **Explanation**: This bar chart shows the **Total order quantity for different bike products**.

- Some bike models show higher purchase quantities, indicating they are more popular among customers.
- **Mountain bike** variants appear frequently with higher order quantities compared to other models.
- Purchases are distributed across multiple regions (states), showing demand in different locations.
- Certain products have lower order quantities, suggesting lower customer preference for those models.
- The chart indicates variation in purchasing patterns across different bike types and regions.

**🔑Key Insight:**\n
A few specific mountain bike models generate the majority of purchases, indicating that **these products are most preferred by customers and drive the highest demand in the market**.
             """)
    
    
    # Bubble Chart
fig7 = px.scatter(df, x=" Unit_Cost ", y= " Unit_Price ", title="7. Unit Cost vs Unit Price with Profit",size=" Profit ", color="Product_Description")
st.plotly_chart(fig7, use_container_width= True)
st.write("""
**Explanation**: The chart **compares Unit Cost (x-axis) with Unit Price (y-axis) including profit.**
         
- Each dot represents a product/item.
- As unit cost increases, the unit price also generally increases.
- The difference between price and cost shows the profit margin.
- Some items have higher profit margins (large gap between cost and price).
- A few items show low or almost no profit when price is close to cost.
         
**🔑Key Insight:**\n
Higher unit cost products are usually sold at higher prices, but profit margins vary across items. 
         """)

# Area Chart
fig8 = px.area(df, x="Date", y="Revenue", title="8. Revenue Growth Over Time")
st.plotly_chart(fig8, use_container_width=True)
st.write("""
**Explanation**: This Area chart shows the**the revenue trend over time, with Date.**.

- Shows revenue trend over time with Date on X-axis and Revenue on Y-axis.
- The shaded area highlights revenue fluctuations across different days.
- Revenue shows multiple peaks and drops, indicating varying daily sales.
- Higher revenue spikes appear toward the later dates of December.

**🔑 Key Insigh:t**\n
Revenue increases significantly in the later part of the month, suggesting **higher sales activity during that period**. 📈
         
""")

# Box Plot
fig9 = px.box(df, x="Age_Group", y="Revenue", title="9. Revenue Distribution by Age Group")
st.plotly_chart(fig9,use_container_width=True )
st.write("""
**Explanation**: The chart shows **revenue distribution for different age groups.**
- The x-axis represents age groups, and the y-axis shows revenue.
- Adults (35–64) generate the highest revenue overall.
- Young Adults (25–34) contribute moderate revenue with some high values.
- Youth (<25) generally produce lower revenue compared to other groups.
         
**🔑 Key Insight:**:\n
➡️ Adults aged 35–64 contribute the highest revenue among all age groups. 
         """)

# Funnel Chart
fig10 = px.violin(df, x="Age_Group", y=" Profit ", title="10. Profit Distribution by Age Group")
st.plotly_chart(fig10, use_container_width= True )
st.write("""
**Explanation**: The chart shows **profit distribution across different age groups.**
- The x-axis represents age groups, and the y-axis shows profit.
- Adults (35–64) show higher and more consistent profit values.
- Young Adults (25–34) have moderate profit with some high peaks.
- Youth (<25) generally show lower profit levels compared to other groups.
         
**🔑 Key Insight:**\n
➡️ Adults aged 35–64 contribute the most consistent and higher profits. 
          """)

# histogram
fig11 = px.histogram(df, x="Customer_Age", title="11. Customer Age Distribution")
st.plotly_chart(fig11, use_container_width=True)
st.write("""
**Explanation**:The chart shows the **distribution of customer ages.**
- The x-axis represents customer age, and the y-axis shows the number of customers.
- Most customers fall in the 30–40 years age group.
- There are fewer younger customers (below 25).
- Very few customers are above 50 years old.
         
**🔑Key Insight:**\n
The majority of customers are middle-aged, mainly between 30 and 40 years. 
         """)
