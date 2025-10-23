from langchain_gigachat import GigaChat
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

API_KEY = "MDE5YTBiNjUtMjIwZi03NmY0LTkzY2QtZTFkODQyODQ1N2YxOjI3M2IxNTJiLWU0ZmItNDBmZS1hMzg0LWViMTU0N2M5MzNlNQ=="

llm = GigaChat(credentials= API_KEY,verify_ssl_certs=False)
system_prompt = SystemMessage(content="""""")
history = []

while True:
    user_input= input("Ваш запрос: ")
    if not user_input.strip():
        continue
    user_prompt = HumanMessage(content= user_input)
    history.append(user_prompt)
    messages = [system_prompt,user_prompt]+history
    response = llm.invoke(messages)
    ai_response_message = AIMessage(content=response.content)
    history.append(ai_response_message)
    print(f"{response.content}")
