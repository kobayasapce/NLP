import requests
import json
import tkinter as tk


# 填入API_KEY与SECRET_KEY
API_KEY = "3wXSLC0yB4ATo62EVMlM1O6L"
SECRET_KEY = "qpplFELSN5aujjMqSbGY20zmIBv2j5X8"


def Communication():
    input_text = entry.get()  # 获取输入框输入内容
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": input_text
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # 输出AI回答结果
    data = json.loads(response.text)
    output_text = data['result']
    entry.delete(0, tk.END)
    text.insert(tk.INSERT, input_text)
    text.insert(tk.INSERT, '\n')
    text.insert(tk.INSERT, output_text)
    text.insert(tk.INSERT, '\n')

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
def Exit():
    window.quit()

if __name__ == '__main__':

    # 创建窗口
    window = tk.Tk()
    window.title("对话窗口")
    window.geometry('500x400')
    window.resizable(False,False)


    # 创建输入框
    entry = tk.Entry(window)
    entry.place(x=25, y=300, width=450, height=50)

    # 创建发送按钮
    button_sent = tk.Button(window, text="发送", command=Communication)
    button_sent.place(x=400, y=350, height=50, width=75)

    # 创建退出按钮
    button_exit = tk.Button(window, text="退出", command=Exit)
    button_exit.place(x=325, y=350, height=50, width=75)

    # 创建文本显示框
    text = tk.Text(window, width=450, height=50)
    text.place(x=25, y=0, width=450, height=300)

    # 创建滚动条
    text_scrollbar = tk.Scrollbar(window)
    text_scrollbar.place(x=475, y=0, width=10, height=300)
    text_scrollbar.config(command=text.yview)
    text.config(yscrollcommand=text_scrollbar.set)

    window.mainloop()

