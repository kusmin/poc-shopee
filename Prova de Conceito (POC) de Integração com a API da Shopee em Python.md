# Prova de Conceito (POC) de Integração com a API da Shopee em Python

Este projeto demonstra uma prova de conceito para integração com a API da Shopee usando Python. Ele inclui funções para autenticação (geração de link de autorização, obtenção e atualização de tokens de acesso) e exemplos de chamadas a endpoints comuns da API.

## Estrutura do Projeto

- `config.py`: Contém as configurações da API, como `PARTNER_ID`, `PARTNER_KEY` e URLs base.
- `shopee_api.py`: Implementa a lógica de autenticação (geração de `sign`, `access_token`, `refresh_token`) e uma função genérica para fazer chamadas à API.
- `main.py`: Um arquivo de exemplo que demonstra como usar as funções implementadas em `shopee_api.py`.
- `test_shopee_api.py`: Contém os testes unitários para as funções de autenticação e chamadas da API.

## Configuração do Ambiente

Siga os passos abaixo para configurar e executar o projeto:

1.  **Clone o repositório (ou crie os arquivos manualmente):**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd shopee_api_poc_python
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install requests
    ```

4.  **Configure suas credenciais da API da Shopee:**

    Edite o arquivo `config.py` e preencha com seu `PARTNER_ID` e `PARTNER_KEY`.

    ```python
    # config.py
    PARTNER_ID = "SEU_PARTNER_ID" # Substitua pelo seu Partner ID
    PARTNER_KEY = "SUA_PARTNER_KEY" # Substitua pela sua Partner Key
    ```

    Alternativamente, você pode definir essas variáveis como variáveis de ambiente:

    ```bash
    export SHOPEE_PARTNER_ID="SEU_PARTNER_ID"
    export SHOPEE_PARTNER_KEY="SUA_PARTNER_KEY"
    ```

## Como Usar

O arquivo `main.py` contém exemplos comentados de como usar as funções de integração. Você precisará descomentar e preencher com seus próprios dados (como `redirect_url`, `main_account_id`, `code`, `access_token`, `shop_id`, `refresh_token` e `order_sn_list`) para testar as funcionalidades.

### Fluxo de Autenticação

1.  **Gerar Link de Autorização:**

    ```python
    # No main.py
    # redirect_url = "https://sua-url-de-redirecionamento.com"
    # auth_link = generate_auth_link(redirect_url)
    # print(f"Link de Autorização: {auth_link}")
    ```

    Copie o `auth_link` gerado e abra-o no navegador. O vendedor precisará autorizar seu aplicativo. Após a autorização, você será redirecionado para a `redirect_url` com um `code` e, opcionalmente, um `shop_id` ou `main_account_id` na URL.

2.  **Obter Access Token:**

    Use o `code` obtido na etapa anterior para solicitar o `access_token` e `refresh_token`.

    ```python
    # No main.py
    # main_account_id = "ID_DA_CONTA_PRINCIPAL" # Se aplicável
    # code = "CODIGO_DE_AUTORIZACAO_RECEBIDO"
    # token_response = get_access_token(main_account_id, code)
    # access_token = token_response["access_token"]
    # refresh_token = token_response["refresh_token"]
    # shop_id = token_response["shop_id"]
    ```

3.  **Atualizar Access Token:**

    O `access_token` tem um tempo de vida limitado. Use o `refresh_token` para obter um novo `access_token` quando o atual expirar.

    ```python
    # No main.py
    # refreshed_token_response = refresh_access_token(shop_id, refresh_token)
    # access_token = refreshed_token_response["access_token"]
    # refresh_token = refreshed_token_response["refresh_token"]
    ```

### Exemplos de Chamadas à API

Após obter um `access_token` e `shop_id` válidos, você pode fazer chamadas a outros endpoints da API:

```python
# No main.py
# ACCESS_TOKEN = "SEU_ACCESS_TOKEN" # Substitua pelo seu access token válido
# SHOP_ID = "SEU_SHOP_ID" # Substitua pelo seu shop ID válido

# Obter informações da loja
# get_shop_info(ACCESS_TOKEN, SHOP_ID)

# Listar produtos
# get_item_list(ACCESS_TOKEN, SHOP_ID)

# Obter detalhes de pedidos
# get_order_detail(ACCESS_TOKEN, SHOP_ID, ["SEU_ORDER_SN_AQUI"])
```

## Executando os Testes

Para executar os testes unitários e verificar a corretude das funções:

```bash
python3.11 test_shopee_api.py
```

## Próximos Passos

Esta POC serve como um ponto de partida. Para um projeto de produção, considere:

*   Implementação de um mecanismo robusto para armazenamento e gerenciamento de tokens (banco de dados, cache).
*   Tratamento de erros mais detalhado e logging.
*   Implementação de retries para chamadas de API que falham temporariamente.
*   Exploração de outros endpoints da API da Shopee conforme a necessidade do seu negócio.


