import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 設定 CSV 檔案名稱
csv_file = "data.csv"

# 初始化 CSV（如果不存在就建立）
if not os.path.exists(csv_file):
    df_init = pd.DataFrame(columns=["Timestamp", "Count"])
    df_init.to_csv(csv_file, index=False)

# 初始化 session state
if "count" not in st.session_state:
    st.session_state.count = 0

st.title("📋 數量統計表單")

st.markdown(f"### 目前數量： `{st.session_state.count}`")

# 加減按鈕
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("➖ 減一"):
        st.session_state.count -= 1
with col2:
    st.write(" ")
with col3:
    if st.button("➕ 加一"):
        st.session_state.count += 1

# 送出按鈕
if st.button("✅ 送出"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    count = st.session_state.count

    # 寫入 CSV
    df_new = pd.DataFrame([[timestamp, count]], columns=["Timestamp", "Count"])
    df_new.to_csv(csv_file, mode='a', header=False, index=False)

    st.success(f"已送出數量：{count}")
    st.session_state.count = 0  # 選擇性：送出後歸零

# 顯示歷史資料
st.markdown("---")
st.subheader("📄 歷史送出紀錄")
df_log = pd.read_csv(csv_file)
st.dataframe(df_log, use_container_width=True)
