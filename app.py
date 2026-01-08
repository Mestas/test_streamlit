import os, pathlib, streamlit as st

# @st.cache_data(show_spinner=False)
# def walk_stats(root="/"):
#     """返回 (文件夹数, 文件数, 总字节数)"""
#     dirs = files = size = 0
#     for p, dir_list, file_list in os.walk(root):
#         dirs += len(dir_list)
#         files += len(file_list)
#         for f in file_list:
#             try:
#                 size += os.path.getsize(os.path.join(p, f))
#             except OSError:
#                 pass
#     return dirs, files, size

# d, f, b = walk_stats()
# st.metric("文件夹数", d)
# st.metric("文件数", f)
# st.metric("已用磁盘空间", f"{b/1024/1024:.2f} MB")

root = "/git-core"
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
    st.write(f"{indent}📂 {os.path.basename(dirpath)}/  {total/1024/1024:,} MB")
