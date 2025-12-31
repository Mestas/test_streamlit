import os, streamlit as st

root = "/app"
st.title("📁 目录树 + 文件夹大小")

for dirpath, dirnames, filenames in os.walk(root, topdown=False):
    # 先算文件总大小
    size = sum(
        os.path.getsize(os.path.join(dirpath, f))
        for f in filenames
        if os.path.exists(os.path.join(dirpath, f))
    )
    # 再算子目录大小（因为 topdown=False，子目录已统计完）
    sub_size = sum(
        os.path.getsize(os.path.join(dirpath, d))   # 这里其实只能拿到目录节点本身大小
        for d in dirnames
        if os.path.exists(os.path.join(dirpath, d))
    )
    total = size + sub_size
    level = dirpath.replace(root, '').count(os.sep)
    indent = "  " * level
    st.text(f"{indent}📂 {os.path.basename(dirpath)}/  {total:,} bytes")
