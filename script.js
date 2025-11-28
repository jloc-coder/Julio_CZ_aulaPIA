document.getElementById('sendButton').addEventListener('click', askAI);

async function askAI() {
    const promptInput = document.getElementById('promptInput');
    const outputDiv = document.getElementById('output');
    const prompt = promptInput.value;

    if (!prompt.trim()) {
        outputDiv.innerHTML = "<p class='error'>Por favor, digite uma pergunta.</p>";
        return;
    }

    // 1. Mostrar status de carregamento e desabilitar o botão
    outputDiv.innerHTML = "<p class='loading'>⌛ O Gemini está processando...</p>";
    document.getElementById('sendButton').disabled = true;

    // URL do endpoint Flask
    const url = 'http://127.0.0.1:5000/ask_gemini';

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt }) // Envia a pergunta em JSON
        });

        const data = await response.json();

        if (response.ok) {
            // 2. Exibe a resposta
            outputDiv.innerHTML = `<p><strong>Resposta do Gemini:</strong></p>${data.response}`;
        } else {
            // 3. Lida com erros do servidor (e.g., chave API inválida)
            outputDiv.innerHTML = `<p class='error'>Erro do Servidor Flask: ${data.error || 'Erro desconhecido'}</p>`;
        }
    } catch (error) {
        // 4. Lida com erros de rede (e.g., Flask não está rodando)
        outputDiv.innerHTML = `<p class='error'>Erro de conexão: Verifique se o servidor Flask está ativo (rodando na porta 5000).</p>`;
        console.error('Erro de rede:', error);
    } finally {
        // Reabilita o botão no final
        document.getElementById('sendButton').disabled = false;
    }
}
