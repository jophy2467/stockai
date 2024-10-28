import numpy as np 
import os
import sys
import pandas as pd 
import plotly.figure_factory as ff 
import streamlit as st 
DIR = os.getcwd()
sys.path.insert(0, DIR)
#from streamlit_style import apply_style

# App title and header
st.set_page_config(page_title="Home Page", page_icon=None, layout="wide", initial_sidebar_state="collapsed")

######################################## tabs ########################################
listTabs =["Introduction", "Terminology", "How to Use"]
whitespace = 0

## Fills and centers each tab label with em-spaces
tabs = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

#"Home" tab
with tabs[0]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        [data-testid="stAppViewContainer"] {            
            background: linear-gradient(45deg, black, #180242 80%);
        }
        [data-testid="stHeader"]{   
            background: black;
        }
        [data-testid=stSidebar] {
            background: black;
        }
        .stTabs [data-baseweb="tab-list"] {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin: 0;
            padding: 0;
        }
        .stTabs [data-baseweb="tab"] {
            flex: 1;
            text-align: center;
            height: 50px;
            background: linear-gradient(45deg, black, #180242 80%);
            border-radius: 4px 4px 0px 0px;
            padding-top: 10px;
            padding-bottom: -50px;
            font-size: 24px; /* Increase font size */
            color: #FFFFFF;
            margin: 0;
            border: none;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(45deg, black, #180242 80%);
            border-bottom: 2px solid #FFFFFF; /* Add a border to indicate selection */
        }
        .centered-heading {
            text-align: center;
            font-family: 'Space Grotesk', sans-serif;
            margin-top: -2%; 
        }
        .hi-text {
            font-size: 130px;
            color: white;
            letter-spacing: 3px; /* Adjust letter spacing */
            margin-bottom: -50px; /* Reduce spacing between lines */
            padding-bottom: 0; /* Correct padding */
            font-weight: 700; /* Bold weight */
        }
        .welcome-text {
            font-size: 80px;
            color: #C4D1FF;
            letter-spacing: 3px; /* Adjust letter spacing */
            margin-top: 0; /* Reduce spacing between lines */
            padding-top: 0; /* Reduce spacing between lines */
            font-weight: 600; /* Semi-bold weight */
        }
        .stockai-text {
            color: #fa4c4c; /* Gold color for StockAI */
            letter-spacing: 3px; /* Adjust letter spacing */
            font-weight: 600; /* Semi-bold weight */
        }
        .catchline-text {
            font-size: 50px;
            color: #D5C4FF;
            letter-spacing: 3px;
            margin-top: -10px;
            font-weight: 400; /* Regular weight */
        }
        .instruction-text {
            font-size: 24px;
            color: #FFFFFF;
            margin-top: 5px;
            font-weight: 400; /* Regular weight */
        }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    st.markdown('<div class="centered-heading"><div class="hi-text">Hi,</div><div class="welcome-text">Welcome to <span class="stockai-text">StockAI</span></div><div class="catchline-text">Your personal AI to navigate markets, analyze strategies, and execute trades effortlessly.</div><div class="instruction-text">Click on the tabs above to learn more and then the sidebar to access StockAI!</div></div>', unsafe_allow_html=True)
    
#Terminology tab
with tabs[1]:
    style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');
        .block-container {
            color: #290B35; /* White */
            font-family: 'Space Grotesk', sans-serif;
            margin-right: auto; /* Centers the container when its width is less than max-width */
            margin-left: auto;
        }
        .subtitle {
            font-family: 'Space Grotesk';
            font-size: 24px;
            font-weight: bold;
            padding-bottom: 0em;
            margin-bottom: 0em;
        }
        ul {
            font-family: 'Space Grotesk';
            font-size: 23px;
            margin-top: 0.5em;
            margin-bottom: 0em;
        }
        .terminology-title {
            font-size: 36px; /* Larger text size */
            color: #FFFFFF; /* White text color */
            background: #30294D; /* Black background */
            padding: 10px 40px; /* Increased padding for better spacing */
            border-radius: 50px; /* Rounded corners for oval shape */
            display: inline-block;
        }
        .intro-text {
            font-family: 'Space Grotesk';
            font-size: 24px;
            color: #FFFFFF;
            margin-top: 20px;
        }
        .box {
            font-family: 'Space Grotesk';
            font-size: 24px;
            color: #FFFFFF; /* White text color */
            background: #251E41; /* Black background */
            padding: 20px 40px; /* Increased padding for better spacing */
            border-radius: 50px; /* Rounded corners for oval shape */
            display: inline-block;
            margin-bottom: 20px;
            width: 90%;
        }
        .left-align {
            text-align: left;
            margin-left: 10%; /* Center the box horizontally */
        }
        .right-align {
            text-align: left;
            margin-right: 5%; /* Center the box horizontally */
        }
        .center-align {
            width: 100%; /* Set width to 100% */
        }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <div class="terminology-title">
                <b>Stock-Related Terminology</b>
            </div>
            <div class="intro-text">
                Look below for some essential stock market terms you should know!
            </div>
        </div>
    """, unsafe_allow_html=True)
    
     # Add a spacer
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="box right-align">
            <b>Basic Terms</b>
            <ul>
                <li><b>Stock</b>: A type of security that signifies ownership in a corporation and represents a claim on part of the corporation's assets and earnings.</li>
                <li><b>Share</b>: A unit of ownership in a company or financial asset.</li>
                <li><b>Dividend</b>: A portion of a company's earnings distributed to shareholders.</li>
                <li><b>Market Capitalization</b>: The total market value of a company's outstanding shares of stock.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="box left-align">
            <b>Trading Terms</b>
            <ul>
                <li><b>Bid Price</b>: The price a buyer is willing to pay for a security.</li>
                <li><b>Ask Price</b>: The price a seller is willing to accept for a security.</li>
                <li><b>Spread</b>: The difference between the bid and ask price.</li>
                <li><b>Volume</b>: The number of shares or contracts traded in a security or market during a given period.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="box right-align">
            <b>Order Types</b>
            <ul>
                <li><b>Market Order</b>: An order to buy or sell a security immediately at the best available current price.</li>
                <li><b>Limit Order</b>: An order to buy or sell a security at a specific price or better.</li>
                <li><b>Stop Order</b>: An order to buy or sell a security once the price reaches a specified level.</li>
                <li><b>Stop-Limit Order</b>: A combination of a stop order and a limit order to buy or sell a security at a specified price or better after a given stop price has been reached.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="box left-align">
            <b>Technical Analysis Terms</b>
            <ul>
                <li><b>Moving Average (MA)</b>: A stock indicator that is commonly used in technical analysis. It helps smooth out price data by creating a constantly updated average price.</li>
                <li><b>Relative Strength Index (RSI)</b>: A momentum oscillator that measures the speed and change of price movements.</li>
                <li><b>Bollinger Bands</b>: A volatility indicator that consists of a set of three lines drawn in relation to a security's price.</li>
                <li><b>Candlestick Chart</b>: A style of financial chart used to describe price movements of a security, derivative, or currency.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="box center-align">
            <b>Specific Terms from StockAI</b>
            <ul>
                <li><b>API Key</b>: A code passed in by computer programs calling an API (Application Programming Interface) to identify the calling program, its developer, or its user to the website.</li>
                <li><b>API Secret</b>: A secret key used in conjunction with the API key to authenticate the calling program.</li>
                <li><b>Endpoint</b>: A specific URL where an API can access the resources it needs to carry out its function.</li>
                <li><b>Ticker</b>: A unique symbol that identifies a specific stock.</li>
                <li><b>Granularity</b>: The level of detail in the data, such as '1 day', '1 hour', '15 minutes', and '5 minutes'.</li>
                <li><b>Candlestick Chart</b>: A type of financial chart used to describe price movements of a security, derivative, or currency.</li>
                <li><b>Simple Moving Average (SMA)</b>: The average price of a stock over a certain period of time.</li>
                <li><b>Exponential Weighted Moving Average (EWMA)</b>: A type of moving average that gives more weight to recent data points.</li>
                <li><b>Relative Strength Index (RSI)</b>: A momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock.</li>
                <li><b>ARIMA (AutoRegressive Integrated Moving Average)</b>: A class of models that explains a given time series based on its own past values, its own past errors, and the past values of a moving average model.</li>
                <li><b>Stationarity</b>: A property of a time series that its statistical properties such as mean, variance, and autocorrelation are all constant over time.</li>
                <li><b>Seasonality</b>: A characteristic of a time series in which the data experiences regular and predictable changes that recur every calendar year.</li>
                <li><b>Forecast</b>: The process of making predictions about the future based on past and present data.</li>
                <li><b>Trading Client</b>: A client used to interact with a trading API to execute trades.</li>
                <li><b>Positions</b>: The amount of a particular security, commodity, or currency held by an individual or entity.</li>
                <li><b>Order Type</b>: The type of order placed in the market, such as 'Limit' or 'Market'.</li>
                <li><b>Paper Trading</b>: Simulated trading that allows investors to practice buying and selling securities without risking real money.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)