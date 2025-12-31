import streamlit as st
import os
if st.button("🔍 查看磁盘目录"):
    st.write("工作目录：", os.getcwd())
    st.write("/app 内容：")
    st.code("\n".join(os.listdir("/app")))
    st.write("/tmp 内容：")
    st.code("\n".join(os.listdir("/tmp")))
    # 如果想看整个树（文件多时会很长）
    # tree = subprocess.check_output(["tree", "-L", "2", "/app"], text=True)
    # st.text(tree)
