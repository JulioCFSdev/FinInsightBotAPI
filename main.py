from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a API do Google
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

# Inicializar o FastAPI
app = FastAPI()

# Definir o modelo de dados para entrada
class NewsAnalysisRequest(BaseModel):
    company: str
    news: str

# Rota para listar modelos suportados (opcional)
@app.get("/models")
def get_models():
    models = []
    try:
        for model in genai.list_models():
            if 'generateContent' in model.supported_generation_methods:
                models.append(model.name)
        return {"models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rota principal para análise de sentimento
@app.post("/analyze-sentiment")
def analyze_sentiment(request: NewsAnalysisRequest):
    try:
        # Construir o texto de entrada para o modelo
        menssage_text = f"""
        Conduct a sentiment analysis of a news story about the company's context and rate the sentiment on a scale of 0 to 10, from negative to positive.
        Company: {request.company}
        News: {request.news}"""
        
        # Gerar a resposta usando o modelo da Google
        response = model.generate_content(menssage_text)
        
        # Retornar a resposta gerada
        return {"sentiment_analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ponto de entrada da aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
