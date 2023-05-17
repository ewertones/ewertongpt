#!/usr/bin/env python3
"""CLI para interação do usuário com o ChatGPT-4

Autor: Ewerton Evangelista de Souza
Data: 2023-05-17
"""
import os
import requests
from requests.exceptions import Timeout


class GPTWrapper:
    """Classe que gerencia a interação com o servidor da OpenAI"""

    def __init__(self, name: str, model: str = "gpt-4", timeout: int = 60):
        self.openai_url = "https://api.openai.com/v1"
        self.openai_secret = os.getenv("OPENAI_SECRET")
        self.openai_model = model
        self.timeout_secs = timeout
        self.headers = {"Authorization": f"Bearer {self.openai_secret}"}
        self.name = name

    @staticmethod
    def clear_screen() -> None:
        """Limpa a tela do terminal, Windows, Linux ou Mac"""
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

    def run(self) -> None:
        """Função principal que lida com a interação do usuário e o servidor"""
        msgs = [
            {
                "role": "system",
                "content": (
                    "You are called EwertonGPT, you were created by Ewerton."
                    " You are answering questions for a user called"
                    f" {self.name}. In your next message, present yourself."
                ),
            }
        ]
        data = {
            "model": self.openai_model,
            "messages": msgs,
            "temperature": 0.7,
        }

        self.clear_screen()
        print(f"Bem-vindo ao EwertonGPT, {self.name}!")

        while True:
            user_input = input(f"\n{self.name} >> ")
            msgs.append({"role": "user", "content": user_input})

            try:
                req = requests.post(
                    f"{self.openai_url}/chat/completions",
                    json=data,
                    timeout=self.timeout_secs,
                    headers=self.headers,
                )
            except Timeout:
                print("\nNão foi possível se conectar ao servidor!")
                return

            if req.status_code == 200:
                response_json = req.json()
                answer = response_json["choices"][0]["message"]["content"]
                print(f"\nEwertonGPT >> {answer}")
                msgs.append({"role": "assistant", "content": answer})
            else:
                print("\nVocê configurou a chave de acesso?")
                return


if __name__ == "__main__":
    username = input("Qual o seu nome? ")
    GPTWrapper(username).run()
