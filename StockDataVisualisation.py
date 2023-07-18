import streamlit as st
import requests
from streamlit_lottie import st_lottie 
import numpy as np
import matplotlib as plt
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg


st.set_page_config(page_title="MY webpage",page_icon=":tada:",layout="wide")
nav=st.sidebar.radio("CONTENT",["HOME","DETAILED DESCRIPTION","COMPARISON"])
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#st.title("DATA VISULATION USING STOCK MARKET")
if nav=="HOME":
    url="https://assets2.lottiefiles.com/packages/lf20_yRrgc4.json"
    with st.container():
        a,b=st.columns(2)
        with a:
            st.subheader("Hi, I am Harshal Sandhu :wave:")
                
            st.title("I am a ungrad student from IIT")
            message=""" I am passionate about finding news ways to implement python in new ways which would help me in my day to day life"""
            st.write(message)
            st.write("here is my github link:")
        with b:
            pass
            #image = "path/to/image.jpg"  # Example: Provide the path to your image file or URL

            # Display the image
            #st.image(image, caption='Image Caption', use_column_width=True)        
    with st.container():
        st.write("----")
        leftcolumn,rightcolumn=st.columns(2)
        with leftcolumn:
            st.header("What does the website do")
            st.write("##")
            st.write(
                """ 
                -This projects basically helps in datavisualisation of stocks performance.\n
                -You can
                >get details of any stock of India or US.\n
                >get details of the stock price over the years using a graph.\n
                >get do comparisons between differenct stocks.\n
                """
            )      
        with rightcolumn:
            st_lottie(url,height=300,key="coding")
                
            
        
        
elif nav=="COMPARISON":
    st.title("COMPARING BETWEEN DIFFERENT STOCKS")
    st.write("This web page is designed to make comparison between multiple stocks")
    left,right=st.columns(2)
    with left:
        name=list(st.text_input("ENTER THE STOCK SYMBOLS:").split())
        #st.write(name)
        #st.write(name)
    with right:
        b=st.selectbox("Country",["INDIA","AMERICA"])
    c=st.slider("Period",min_value=1,max_value=50)
    if name==[] :
        pass
    else:
        #symbol = input("Enter a stock symbol: ")
        if b=="INDIA":
            a='.NS'
        else:
            a=""
        closing_prices = pd.DataFrame()

        # Retrieve historical data for each stock symbol
        for symbol in name:
            stock = yf.Ticker(symbol + a)  # Append ".NS" for stocks in the National Stock Exchange (NSE)
            history = stock.history(period=str(c)+"y")
            closing_prices[symbol] = history['Close']
        colours=["#fd7f6f", "#7eb0d5", "#b2e061", "#bd7ebe", "#ffb55a", "#ffee65", "#beb9db", "#fdcce5", "#8bd3c7"]

        line=['-', '-', '--', '-', '--', '-', '--']
        # Plot the closing prices
        plt.figure(figsize=(10, 6))
        c=0
        for symbol in name:
            plt.plot(closing_prices[symbol], label=symbol, color=colours[c], linewidth=2)
            c+=1

        plt.title("Stock Price History",fontsize=14)
        plt.xlabel("Date",fontsize=12)
        plt.ylabel("Closing Price ",fontsize=12)
        plt.grid(True,linestyle='--', alpha=0.7)
        plt.legend()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
        
elif nav=="DETAILED DESCRIPTION":
    st.title("Here you get the detailed description of any INDIAN or US stock")
    left,right=st.columns(2)
    with right:
        z=st.selectbox("Country",["INDIA","AMERICA"])
        
    with left:
        name1=st.text_input("ENTER THE STOCK NAME:")
        if z=="INDIA":
                a='.NS'
        else:
            a=""
    s=st.slider("Period",min_value=1,max_value=50)
    if name1=="":
        pass
    else:
        ticker=yf.Ticker(name1+a)
        stock_info=ticker.info
    
    left1,right1=st.columns(2)
    with left1:
        if name1=="":
            pass
        else:
                
            #stock_info=ticker.info
            st.write("The stock symbol is represented by: ",stock_info["symbol"])
            st.write("Company name is:  ",stock_info["longName"])
            st.write("The stock sector:  ",stock_info["sector"])
            st.write("The stock industry:  ",stock_info["industry"])
            st.write("The country:  ",stock_info["country"])
            st.write("The official website is: ",stock_info["website"])
    with right1:
        pass
        #   

            
    a,b=st.columns(2)
    with a:
        if name1=="":pass
        else:
            
            history = ticker.history(period=str(s)+"y")
            plt.plot(history["Close"],label=name1,color="#fd7f6f")
            plt.title("Stock Price History",fontsize=14)
            plt.xlabel("Date",fontsize=12)
            plt.ylabel("Closing Price ",fontsize=12)
            plt.grid(True,linestyle='--', alpha=0.7)
            plt.legend()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
    with b:
        #ticker=yf.Ticker(str(name1)+a)
        if name1=="":
            pass
        else:
            history = ticker.history(period=str(s)+"y")
            
            history['Year'] = history.index.year
            data_by_year= history.groupby('Year')["Volume"].sum()
            
            plt.bar(data_by_year.index, data_by_year,color="#ffb55a")
            plt.xlabel("Year",fontsize=12)
            plt.ylabel("Volume",fontsize=12)
            plt.title(f"{name1} Stock Volume by Year",fontsize=14)
            plt.show()
            st.set_option('deprecation.showPyplotGlobalUse', False)


            st.pyplot()
        
        
    
    