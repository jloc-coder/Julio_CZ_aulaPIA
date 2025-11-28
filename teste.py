import google.generativeai as genai
import sys

try:
    api_key = "api_key"
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Erro ao configurar o SDK do Geminai:{e}")
    sys.exit(1)
    
# Inicializando o MODELO
# Vamos usar o gemini -pro para geração de testo
print ("Inicializando o modelo...")
try:
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
except Exception as e:
    print(f"Erro ao configurar o SDK do Geminai:{e}")
    sys.exit(1)
    
# Gerar conteúdo (O "Hello World")
print ("Gerando conteúdo...")
response = model.generate_content(input("Qual sua pergunta? "))

# Exibir as respostas
print("\n --- Resposta do GEMINI ---")
print(response.text)
print("--------------------------------")