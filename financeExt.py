import yfinance as yf
import pandas as pd

stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "BRK-B", "V", "JNJ",
    "WMT", "DIS", "PYPL", "UNH", "HD", "MA", "VZ", "KO", "PFE", "CSCO", "PEP", "NFLX",
    "ABT", "MRK", "INTC", "T", "NKE", "MCD", "ORCL", "XOM", "BA", "CVX", "IBM", "COST",
    "MMM", "SPGI", "CAT", "ACN", "RTX", "DHR", "GS", "LMT", "TXN", "WFC", "AMGN", "BMY",
    "CCI", "MDT", "ISRG", "PGR", "LOW", "UPS", "SYK", "QCOM", "BP.L", "HSBA.L", "AZN.L",
    "GLEN.L", "DGE.L", "BATS.L", "SHEL.L", "BARC.L", "TSCO.L", "RIO.L", "ULVR.L", "LLOY.L",
    "AV.L", "NG.L", "GSK.L", "REL.L", "SBRY.L", "RELIANCE.BO", "TCS.BO", "INFY.BO",
    "HDFCBANK.BO", "ICICIBANK.BO", "KOTAKBANK.BO", "SBIN.BO", "ITC.BO", "HCLTECH.BO",
    "WIPRO.BO", "LT.BO", "0700.HK", "0941.HK", "0005.HK", "2318.HK", "0011.HK", "0083.HK",
    "0388.HK", "1299.HK", "3988.HK", "1398.HK", "2313.HK", "2388.HK", "6862.HK", "1109.HK",
    "AIR.PA", "MC.PA", "SAP.DE", "ALV.DE", "BMW.DE", "OR.PA", "VIV.PA", "BAS.DE", "LIN.DE",
    "DTE.DE", "BNP.PA", "FP.PA", "SAN.PA", "EN.PA", "AI.PA", "SU.PA", "FRE.DE", "ADS.DE",
    "DB1.DE", "MTX.DE", "ZAL.DE", "SHOP.TO", "BNS.TO", "RY.TO", "TD.TO", "BAM.TO", "ENB.TO",
    "CNQ.TO", "BB.TO", "WEED.TO", "SU.TO", "MFC.TO", "SLF.TO", "FTNT", "PANW", "NOW",
    "ADBE", "CRM", "SPOT", "ZM", "DOCU", "SQ", "SNAP", "UBER", "LYFT", "TWLO", "OKTA", "NET"
]

def fetch_stock_data(stocks):
    data = []
    for stock in stocks:
        try:
            ticker = yf.Ticker(stock)
            info = ticker.history(period="1mo")
            if not info.empty:
                info.reset_index(inplace=True)
                info['Date'] = pd.to_datetime(info['Date']).dt.tz_localize(None)  
                info['Stock'] = stock
                data.append(info)
            else:
                print(f"$ {stock}: No data found (possibly delisted)")
        except Exception as e:
            print(f"Failed to get ticker '{stock}' reason: {e}")
    return pd.concat(data, ignore_index=True) if data else pd.DataFrame()

stock_data = fetch_stock_data(stocks)

if not stock_data.empty:
    stock_data.to_excel("C:\\Users\\arjun\\OneDrive\\Documents\\ESG\\ESG_portfolio_data.xlsx", index=False)
    print("Data saved to C:\\Users\\arjun\\OneDrive\\Documents\\ESG\\ESG_portfolio_data.xlsx")
else:
    print("No data to save.")
