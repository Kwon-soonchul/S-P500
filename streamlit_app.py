
import streamlit as st
import yfinance as yf
import pandas as pd

# 타이틀
st.title("📈 S&P500 주요 기업 수익률 대시보드")

# 사용자 선택 - 기본 종목
default_tickers = ['AAPL', 'MSFT', 'GOOGL']
tickers = st.multiselect("관심 있는 종목을 선택하세요:", options=default_tickers, default=default_tickers)

if tickers:
    # 데이터 불러오기
    data = yf.download(tickers, period='6mo', group_by='ticker', auto_adjust=True)
    close_prices = pd.DataFrame({ticker: data[ticker]['Close'] for ticker in tickers})
    
    # 수익률 계산
    monthly_returns = close_prices.pct_change().resample('M').agg(lambda x: (1 + x).prod() - 1)

    st.subheader("📊 월별 수익률 (%)")
    st.dataframe((monthly_returns * 100).round(2))

    # 차트
    st.line_chart(monthly_returns)
else:
    st.info("종목을 선택해주세요.")
