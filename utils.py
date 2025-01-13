from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


def get_chat_response(prompt, openai_api_key, memory):
    # 创建 ChatOpenAI 模型实例
    # model="gpt-3.5-turbo" 指定使用 GPT-3.5-turbo 模型
    # openai_api_key 提供 OpenAI 的 API 密钥
    # openai_api_base 指定 API 的基础地址
    model = ChatOpenAI(model="gpt-3.5-turbo",
                    openai_api_key=openai_api_key,
                    openai_api_base="https://api.aigc369.com/v1")
    # 创建 ConversationChain 实例
    # 将之前创建的 ChatOpenAI 模型实例和传入的 memory 作为参数
    # memory 存储对话的历史信息，用于为对话提供上下文
    chain = ConversationChain(llm=model, memory=memory)
    # 使用 ConversationChain 实例调用输入，传入一个包含输入信息的字典 {"input": prompt}
    # 这里使用 | 运算符可能是为了结合模型和链进行处理，具体依赖于相应的库实现
    response = chain.invoke({"input": prompt})
    # 返回响应结果中名为 "response" 的部分，可能是实际的回复内容
    return response["response"]
