# Sistema de Monitoramento e Gerenciamento com Psutil

Este é um programa simples em Python que utiliza a biblioteca `psutil` para monitorar e gerenciar recursos do sistema como CPU, memória, disco, rede, processos e status da bateria. O programa apresenta um menu interativo para que o usuário escolha a funcionalidade desejada.

---

## Funcionalidades

1. **Monitoramento do uso da CPU**  
   Exibe a porcentagem de uso da CPU para cada núcleo.

2. **Monitoramento do uso da memória**  
   Mostra informações sobre a memória total, disponível e a porcentagem em uso.

3. **Monitoramento de disco**  
   Detalha o uso da partição raiz, incluindo capacidade total, espaço usado e disponível.

4. **Gerenciamento de rede**  
   Exibe os dados enviados e recebidos pela rede em gigabytes.

5. **Gerenciamento de processos**  
   Lista os processos em execução com informações como PID, nome e usuário associado. Permite pausar a listagem em blocos de 10 processos.

6. **Verificação do status da bateria**  
   Mostra o nível de bateria restante e se o dispositivo está carregando.

0. **Sair**  
   Encerra o programa.

---

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca `psutil` instalada

Para instalar a biblioteca, execute:  
```bash
pip install psutil
```

---

## Como usar

1. Clone o repositório ou copie o código.
2. Execute o script no terminal:
   ```bash
   python nome_do_arquivo.py
   ```
3. Siga as instruções exibidas no menu interativo.

---

## Exemplo de Uso

### Monitoramento do uso da CPU:
```plaintext
Porcentagem de uso da CPU por núcleo: 
Núcleo 1: 25.3%
Núcleo 2: 18.7%
```

### Monitoramento de Disco:
```plaintext
Uso do disco na partição raiz:
Total: 256.00 GB
Usado: 128.00 GB
Livre: 128.00 GB
Porcentagem de uso: 50.00%
```
---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma [issue](https://github.com/seu-usuario/seu-repositorio/issues) ou enviar um [pull request](https://github.com/seu-usuario/seu-repositorio/pulls).

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
## Contato
Criado por: Francis Monteles  
Email: <quasedev@protonmail.com>  
LinkedIn: [Francis Monteles](https://www.linkedin.com/in/francis-monteles/)