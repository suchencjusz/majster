
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="phi4")
print(llm.invoke('hello'))


# from data.pkobp import PkoBpParser

# t = PkoBpParser('pkobp.csv').load_transactions()

# t = t[::-1]

# # for i in t:

# #     for x in i:
# #         print(x)

# #     print()
