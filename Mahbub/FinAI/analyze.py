import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_community.llms import Ollama

# Load the financial statements
df = pd.read_csv('statements.csv')

# Initialize the LLM
llm = Ollama(model="llama2")

# Create the pandas agent
agent = create_pandas_dataframe_agent(
    llm, 
    df, 
    verbose=True, 
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Example query
response = agent.invoke("What is the total revenue?")
print(response)