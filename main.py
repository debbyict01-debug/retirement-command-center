import streamlit as st
import pandas as pd
import yfinance as yf

# --- [老闆專區：要在這裡修改妳的持股] ---
def get_my_portfolio():
    data = [
        {"名稱": "華通", "代號": "2313.TW", "成本": 225.69, "股數": 100},
        {"名稱": "良維", "代號": "6290.TWO", "成本": 220.0, "股數": 40},
        {"名稱": "亞力", "代號": "1514.TW", "成本": 114.1, "股數": 200},
        {"名稱": "台塑化", "代號": "6505.TW", "成本": 59.53, "股數": 1000},
        # 在這裡按格式增加新標的，例如: {"名稱": "鴻海", "代號": "2317.TW", "成本": 210, "股數": 100},
    ]
    return pd.DataFrame(data)

# --- [以下是系統邏輯，沒事不用動] ---
st.set_page_config(page_title="退休進擊戰情室", layout="wide")
st.title("🏹 退休進擊戰情室 V4.0")

df = get_my_portfolio()

# 自動抓取最新價格
@st.cache_data(ttl=300)
def fetch_prices(tickers):
    prices = {}
    for t in tickers:
        try:
            prices[t] = yf.Ticker(t).fast_info['last_price']
        except:
            prices[t] = 0
    return prices

live_prices = fetch_prices(df['代號'].tolist())
df['現價'] = df['代號'].map(live_prices)
df['損益'] = (df['現價'] - df['成本']) * df['股數']
df['報酬率(%)'] = ((df['現價'] - df['成本']) / df['成本'] * 100).round(2)

# 看板顯示
total_pl = df['損益'].sum()
col1, col2, col3 = st.columns(3)
col1.metric("總資產水位", f"${(df['現價']*df['股數']).sum():,.0f}")
col2.metric("今日總損益", f"${total_pl:,.0f}", delta=f"{total_pl:,.0f}")
col3.metric("剩餘子彈", "$6,150")

# 體檢表
st.subheader("📊 持股即時體檢")
st.dataframe(df.style.highlight_min(subset=['損益'], color='#ff4b4b'))

# 進擊建議
st.subheader("💡 指揮官決策建議")
worst = df.loc[df['報酬率(%)'].idxmin()]
if worst['報酬率(%)'] < -5:
    st.warning(f"偵測到資金瓶頸：【{worst['名稱']}】跌幅達 {worst['報酬率(%)']}%。建議評估汰弱留強！")