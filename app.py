import os, psutil, streamlit as st

# 1. 磁盘剩余（能拿到的是容器里唯一被挂载的 / ）
disk = psutil.disk_usage("/")
st.write("总空间  :", round(disk.total/1024**3, 2), "GB")
st.write("已用空间:", round(disk.used/1024**3, 2), "GB")
st.write("剩余空间:", round(disk.free/1024**3, 2), "GB")

# 2. 把「/app」下所有文件/夹递归列出来（Streamlit 只会给你看这部分）
root = "/app"
for dirpath, dirnames, filenames in os.walk(root):
    level = dirpath.replace(root, '').count(os.sep)
    indent = ' ' * 2 * level
    st.text(f"{indent}{os.path.basename(dirpath)}/")
    sub_indent = ' ' * 2 * (level + 1)
    for f in filenames:
        fp = os.path.join(dirpath, f)
        try:
            size = os.path.getsize(fp)
        except OSError:
            size = 0
        st.text(f"{sub_indent}{f}  {size} bytes")
