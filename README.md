# 💜 Incentivo Bot — Discord

> Bot de apoio emocional para servidores Discord. Monitora o chat e, ao identificar palavras de desânimo, responde automaticamente com mensagens de encorajamento.

---

## 💡 Como funciona

1. O bot monitora todas as mensagens do servidor em tempo real
2. Ao detectar palavras-chave de desânimo (ex: "triste", "cansado", "desistir"...)
3. Responde automaticamente com uma mensagem de encorajamento personalizada
4. Hospedado na nuvem com uptime contínuo via **Uptime Robot**

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

---

## ▶️ Como executar localmente

**Pré-requisitos:** Python 3, conta de desenvolvedor no Discord

```bash
# Clone o repositório
git clone https://github.com/najuiamnc/Incentivo-Bot

# Instale as dependências
pip install discord.py flask

# Configure o token do bot
# Crie um arquivo .env com:
# TOKEN=seu_token_aqui

# Execute
python bot.py
```

> ⚠️ Nunca compartilhe seu token publicamente. Use variáveis de ambiente.

---

## ⚙️ Configuração do Bot no Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Crie uma nova aplicação e adicione um bot
3. Copie o token e salve no `.env`
4. Convide o bot para o seu servidor com as permissões necessárias

---

## ☁️ Deploy na Nuvem

O bot está hospedado gratuitamente e mantido ativo via **Uptime Robot**, que faz pings periódicos no endpoint Flask para evitar que o serviço durma.

---

## 👩‍💻 Autora

Feito com 💜 por [Julia Amancio](https://github.com/najuiamnc)  
[![Portfolio](https://img.shields.io/badge/Portfólio-000?style=flat&logo=github&logoColor=white)](https://najuiamnc.github.io/portfolio-pessoal/)

