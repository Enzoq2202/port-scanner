# Escaneador de Portas TCP

Este é um projeto simples em Python que permite realizar o escaneamento de portas TCP em um determinado host ou IP. A aplicação possui uma interface gráfica amigável para facilitar o uso.

## Funcionalidades

- **Escaneamento de portas TCP:** Verifica se as portas estão abertas em um host especificado.
- **Interface gráfica moderna:** Interface fácil de usar e visualmente agradável.
- **Barra de progresso:** Indica o progresso do escaneamento em tempo real.
- **Identificação de serviços:** Mostra o serviço associado a portas conhecidas.

## Requisitos

- Python 3.x
- Tkinter (instalado por padrão na maioria das distribuições Python)

###  Como usar


```bash
git clone https://github.com/Enzoq2202/port-scanner
```


### Navegue até seu repositório e execute o script

``` bash
python port_scanner.py
```

### A interface será aberta. Em seguida, preencha os campos conforme abaixo:

- **Host/IP**: Insira o IP ou hostname do alvo (ex: 127.0.0.1)

- **Porta Inicial**: Defina a porta inicial para o escaneamento (ex: 20).

- **Porta Final**: Defina a porta final para o escaneamento (ex: 1000).
- Após o preenchimento, clique em "**Iniciar Escaneamento**" para começar. O progresso será mostrado na barra de progresso, e as portas abertas serão listadas na caixa de saída.








