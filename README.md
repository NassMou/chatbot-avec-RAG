# chatbot-avec-RAG
hatbot capable de répondre à des questions en s’appuyant sur un document PDF fourni par l’utilisateur, grâce à un LLM (type GPT) combiné à une stratégie RAG

#Chatbot RAG avec votre document PDF

Un assistant intelligent basé sur GPT-3.5 capable de répondre à vos questions à partir d’un document PDF que vous uploadez. Le système utilise la technique de **RAG (Retrieval-Augmented Generation)** pour combiner recherche d'information et génération de texte.


##Fonctionnalités

- Upload de documents PDF
- Extraction automatique du texte
- Découpage intelligent (chunking)
- Recherche sémantique avec FAISS
- Génération de réponse via GPT-3.5 (OpenAI)


##Lancer l'application

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/rag-chatbot.git
cd rag-chatbot
