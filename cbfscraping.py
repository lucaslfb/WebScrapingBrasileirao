import requests
import pandas as pd
from io import StringIO

pd.set_option('display.expand_frame_repr', False)

header = {'User-Agent': 'Your User-Agent'}

url = 'https://www.cbf.com.br/futebol-brasileiro'
request = requests.get(url, headers=header)

html_content = request.text
html_stringio = StringIO(html_content.strip())
data = pd.read_html(html_stringio)

df = pd.DataFrame(data[0])

# Ordena os times com mais cartões vermelhos. Jogos inclusos.
df_red_cards = df.iloc[:5].loc[:, ['Posição', 'J', 'CV']].sort_values('CV', ascending=False)
print(f"5 times com mais cartões vermelhos:\n{df_red_cards.to_string(index=False)}\n---------------")

# Ordena os times com mais gols. Jogos inclusos
df_goal_difference = df.iloc[:5].loc[:, ['Posição', 'J', 'GP']].sort_values('GP', ascending=False)
print(f"5 times com mais gols:\n{df_goal_difference.to_string(index=False)}\n---------------")
