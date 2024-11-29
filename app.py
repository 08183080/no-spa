import os
import tkinter as tk
from tkinter import scrolledtext, font
def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def get_spa_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def display_text():
    # 清空之前的文本
    text_area.delete('1.0', tk.END)
    
    # 获取列表框中选中的文件路径
    selected_index = file_list.curselection()
    if not selected_index:
        return
    path = file_list.get(selected_index)
    
    # 读取并显示文件内容
    text = get_spa_text(path)
    text_area.insert(tk.END, text)

# 创建主窗口
root = tk.Tk()
root.title('spa冷静器')

# 设置字体样式
custom_font = font.Font(family="Helvetica", size=12)  # 你可以根据需要更改字体类型和大小

# 创建文件列表框
file_list = tk.Listbox(root, width=50, height=15)
file_list.pack(side=tk.LEFT, fill=tk.BOTH)

# 创建滚动文本区域
text_area = scrolledtext.ScrolledText(root, width=50, height=15, font=custom_font)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)  # padx和pady为文本区域添加边距

# 获取文件路径并添加到列表框
for path in get_all_file_paths('D:\\no-spa\\data'):
    file_list.insert(tk.END, path)

# 创建按钮，点击后显示文件内容
button = tk.Button(root, text="显示文件内容", command=display_text, font=custom_font)
button.pack(side=tk.BOTTOM, fill=tk.X)

# 启动事件循环
root.mainloop()