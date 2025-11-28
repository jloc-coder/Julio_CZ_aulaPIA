# Tudo acima foi adicionado afim de ocultar a APIKEY
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import sys
import os

app = Flask(__name__)
CORS(app)

# Configuração da API Key
# MUDANÇA CRÍTICA: Não use a chave hardcoded.
# Use a variável de ambiente (A chave deve ser exportada no terminal antes de rodar o Flask)
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
except Exception as e:
    print(f"Erro na configuração inicial do Gemini: {e}")
    sys.exit(1)

# Rota que o Frontend chamará
@app.route('/ask_gemini', methods=['POST'])
def ask_gemini():
    # 1. Pega a pergunta enviada pelo site (JSON)
    data = request.get_json()
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({"error": "Nenhuma pergunta fornecida."}), 400

    print(f"Recebido prompt: {user_prompt}")
    
    # 2. Gera o conteúdo usando o modelo
    try:
        response = model.generate_content(user_prompt)
        
        # 3. Retorna a resposta para o navegador
        return jsonify({
            "response": response.text
        })
    except Exception as e:
        print(f"Erro na geração de conteúdo: {e}")
        return jsonify({"error": "Erro ao se comunicar com o modelo Gemini."}), 500

if __name__ == '__main__':
    # Define a porta 5000 para rodar o servidor
    app.run(debug=True)