# AWS Lambda
## Este repositório contém código python que retorna se uma frase é um palindromo ou não.

## Índice
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)
- [Agradecimentos](#agradecimentos)

URL para testes: https://uumykwl4shwyvdgiydjnyx4j340mwawf.lambda-url.us-east-2.on.aws/

# Requisitos:
- Postman
- AWS Lambda

# Instalação
- Faça um clone do repositório atual:
 ```bash
https://github.com/MarianaLuca/AWS-Lambda-Palindromo.git
```
- Abra o console da AWS
- Cria uma lambda com nome de sua preferência
- Crie uma URL para a lambda

# Uso
## Após os passos acima, faça o seguinte:

- Abra o Postman
- Utilize a url fornecida da lambda
- Envie uma requisição POST com o seguinte corpo
- De o comando para inicializar a fila:
 ```
{
    "frase": "anaaa"
}
```

Podem existir dois retornos:
```
 status: 200
 Não é um palindromo!
```


```
 status: 200
 É um palindromo!
```

# Contribuição
Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue para discutir suas mudanças.

# Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](link para o arquivo) para detalhes.

# Contato
Mariana Luca Rocha - mluca2564@gmail.com

LinkedIn - https://www.linkedin.com/in/mariana-luca-rocha-157a90219/

# Agradecimentos
Pedro Matias de Araujo - pela sujestão do trabalho 

ChatGPT - pela ajuda com os erros sem solução rsrs 


