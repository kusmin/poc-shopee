import os
from shopee_api import generate_auth_link, get_access_token, refresh_access_token, make_api_call

# Defina suas credenciais de ambiente aqui ou como variáveis de ambiente
# os.environ["SHOPEE_PARTNER_ID"] = "SEU_PARTNER_ID"
# os.environ["SHOPEE_PARTNER_KEY"] = "SUA_PARTNER_KEY"

# Exemplo de uso:
# 1. Gerar link de autorização
# redirect_url = "https://sua-url-de-redirecionamento.com"
# auth_link = generate_auth_link(redirect_url)
# print(f"Link de Autorização: {auth_link}")

# 2. Obter Access Token (após o vendedor autorizar e você receber o código)
# main_account_id = "ID_DA_CONTA_PRINCIPAL" # Se aplicável
# code = "CODIGO_DE_AUTORIZACAO_RECEBIDO"
# try:
#     token_response = get_access_token(main_account_id, code)
#     print(f"Access Token Response: {token_response}")
#     access_token = token_response["access_token"]
#     refresh_token = token_response["refresh_token"]
#     shop_id = token_response["shop_id"]
# except Exception as e:
#     print(f"Erro ao obter Access Token: {e}")

# 3. Refresh Access Token (quando o access token expirar)
# try:
#     refreshed_token_response = refresh_access_token(shop_id, refresh_token)
#     print(f"Refreshed Token Response: {refreshed_token_response}")
#     access_token = refreshed_token_response["access_token"]
#     refresh_token = refreshed_token_response["refresh_token"]
# except Exception as e:
#     print(f"Erro ao atualizar Access Token: {e}")

# 4. Exemplos de chamadas da API
# Substitua com seus valores reais após a autenticação
# ACCESS_TOKEN = "SEU_ACCESS_TOKEN"
# SHOP_ID = "SEU_SHOP_ID"

# def get_shop_info(access_token, shop_id):
#     path = "/api/v2/shop/get_shop_info"
#     try:
#         response = make_api_call(path, access_token, shop_id)
#         print(f"Shop Info: {response}")
#         return response
#     except Exception as e:
#         print(f"Erro ao obter informações da loja: {e}")

# def get_item_list(access_token, shop_id):
#     path = "/api/v2/product/get_item_list"
#     params = {
#         "page_size": 10,
#         "offset": 0
#     }
#     try:
#         response = make_api_call(path, access_token, shop_id, params=params)
#         print(f"Item List: {response}")
#         return response
#     except Exception as e:
#         print(f"Erro ao obter lista de itens: {e}")

# def get_order_detail(access_token, shop_id, order_sn_list):
#     path = "/api/v2/order/get_order_detail"
#     params = {
#         "order_sn_list": ",".join(order_sn_list)
#     }
#     try:
#         response = make_api_call(path, access_token, shop_id, params=params)
#         print(f"Order Detail: {response}")
#         return response
#     except Exception as e:
#         print(f"Erro ao obter detalhes do pedido: {e}")

# Exemplo de execução (descomente e preencha com seus dados reais para testar)
# if __name__ == "__main__":
#     # Certifique-se de que as variáveis de ambiente SHOPEE_PARTNER_ID e SHOPEE_PARTNER_KEY estão definidas
#     # ou descomente as linhas acima para defini-las diretamente no código (não recomendado para produção)
#     if not os.getenv("SHOPEE_PARTNER_ID") or not os.getenv("SHOPEE_PARTNER_KEY"):
#         print("Por favor, defina as variáveis de ambiente SHOPEE_PARTNER_ID e SHOPEE_PARTNER_KEY.")
#     else:
#         # Exemplo de como usar as funções (requer credenciais e autorização prévia)
#         # auth_link = generate_auth_link("https://sua-url-de-redirecionamento.com")
#         # print(f"Link de Autorização: {auth_link}")

#         # Para testar as chamadas da API, você precisará de um access_token e shop_id válidos
#         # obtidos através do processo de autorização.
#         # get_shop_info(ACCESS_TOKEN, SHOP_ID)
#         # get_item_list(ACCESS_TOKEN, SHOP_ID)
#         # get_order_detail(ACCESS_TOKEN, SHOP_ID, ["SEU_ORDER_SN_AQUI"])


