from langchain_openai import ChatOpenAI
from utils import get_chat_response
import streamlit as st
from langchain.memory import ConversationSummaryBufferMemory

st.title("🤖 Cloned-ChatGPT") # 给网页起一个标题
with st.sidebar:
    user_openai_api_key = st.text_input("Please input your API keys:",type="password")# api密钥输入框
    checkbox_api = st.checkbox("❓ I have no API keys")# 如果用户没有API密钥，向用户提供API密钥网站
    if checkbox_api:
        st.markdown("""🔑Method to get API keys:
                    https://api.aigc369.com/register?aff=87kh """)

model = ChatOpenAI(model = "gpt-3.5-turbo",
                   openai_api_key = user_openai_api_key,
                   openai_api_base="https://api.aigc369.com/v1")# 用于总结和解析的模型

# 使用会话状态保留用户之间的对话记忆
if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationSummaryBufferMemory(return_messages = True,llm=model)# 初始化记忆，传入第二个参数llm为model
    st.session_state["messages"] = [{"role":"ai",
                                    "content":"嘿！我是小助手Cloned-ChatGPT🥰，有啥想聊的？"}]# 初始化消息，使用户能接收到AI的消息
# 显示出历史对话的内容
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])# streamlit中的chat_message方法，第一个传入角色，第二个传入消息内容

prompt = st.chat_input()# 用户输入的信息

if prompt:
    if not user_openai_api_key:
        st.info("❗ Please provide your openai api key")# 如果用户没有提供api密钥，则写出提示语句
        st.stop()
    st.session_state["messages"].append({"role":"human",
                                         "content":prompt})# 将用户刚刚输入的信息保存在messages中
    st.chat_message("human").write(prompt)# 显示用户刚刚输入的信息

    with st.spinner("🧠 AI is accelerating its thinking..."):
        response = get_chat_response(prompt,user_openai_api_key,st.session_state["memory"])# AI在加载的时候，给出消息提示。当加载完成，给出AI的回复

    msg = {"role":"ai",
           "content":response}
    st.session_state["messages"].append(msg)# 将AI回复的消息保存在messages中
    st.chat_message("ai").write(response)



