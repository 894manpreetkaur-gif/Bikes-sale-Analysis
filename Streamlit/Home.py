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
    st.subheader(":blue[Dataset View]", divider=True)
    st.dataframe(df)

    # (d) Dataset Explanation
    st.subheader(":blue[Dataset Explanation]", divider=True)
    
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
    st.header("Visual Representation")
    import plotly.express as px
    import matplotlib.pyplot as plt

    # Pie chart
    fig1 = px.pie(df,values="Order_Quantity", names="Age_Group" , title = "Bikes Purchasing According The Age Group")
    st.plotly_chart(fig1, use_container_width=True)

    # Scatterplot
    fig2= px.scatter(df,x= " Cost ",y=" Profit ", title="Bikes Purchasing according to the Customer Gender",size=" Profit ",color=" Profit ")
    st.plotly_chart(fig2, use_container_width =True)
    
    # Bar Chart
    fig3 = px.bar(df, x= "Country", y="Order_Quantity", title="Country Wise Purchase")
    st.plotly_chart(fig3, use_container_width=True)

    fig4= px.data.gapminder()
    fig4 = px.area(df,x="Country",y= " Profit ", title = "Country Wise Profit",  color="Product_Description", line_group=" Profit ")
    st.plotly_chart(fig4, use_container_width = True)

    # Histogram
    fig5 = px.histogram(df,x="Product_Description",y="Order_Quantity",color = "State",barmode ="stack",title="Bikes Purchasing according to the Customer Gender")
    st.plotly_chart(fig5, use_container_width = True)


