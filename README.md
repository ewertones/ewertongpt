# EwertonGPT

🇺🇸 EwertonGPT is a school project that implements a CLI in many languages (C, C++, Java, Python) that allows users to interact with the ChatGPT-4 model developed by OpenAI. It provides a simple way to ask questions and receive responses generated by the model. I'm lazy, so everything below is in Portuguese, which I need to use to deliver it.

🇧🇷 EwertonGPT é um projeto escolar que implementa uma CLI em várias linguagens (C, C++, Java, Python) e que permite a usuários interagirem com o modelo ChatGPT-4 desenvolvido pela OpenAI. Ele providencia uma maneira simples de se fazer perguntas e receber as respostas geradas pelo modelo.

## Instruções

Por ter sido criado em diferentes linguagens, cada uma tem seus comandos para que possam ser rodados na sua máquina local, porém primeiramente, são necessários os seguintes passos:

1. Clone o projeto com:

```bash
git clone git@github.com:ewertones/ewertongpt
```

2. Exporte a credencial de acesso à API da OpenAI (senão tiver, gere uma ou peça ao autor 😃). Se usar Windows, substitua `export` por `set`:

```bash
export OPENAI_SECRET="sua-chave-aqui"
```

### Python

3. Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

4. Rode o programa:

```bash
python3 ./python/gpt.py
```
