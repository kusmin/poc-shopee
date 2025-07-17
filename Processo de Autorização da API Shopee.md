# Processo de Autorização da API Shopee

Existem 4 etapas para completar a autorização:
1. Gerar o link de autorização.
2. Adquirir autorizações da(s) loja(s).
3. Usar o código de autorização.
4. Obter e atualizar o `access_token`.

## Geração do Link de Autorização

Para Apps de Sistema Interno do Vendedor, você pode fazer login na Plataforma Aberta > Lista de Apps > clicar em Autorizar > preencher a URL de Redirecionamento para gerar um link de autorização.

Para todos os tipos de Apps, você precisa criar um link de autorização com as seguintes especificações. O link de autorização compreende uma URL de autorização fixa e outros parâmetros necessários.

**URL de Autorização Fixa:**

*   **Ambiente de Produção:** `https://partner.shopeemobile.com/api/v2/shop/auth_partner`
*   **(China Continental) Ambiente de Produção:** `https://openplatform.shopee.cn/api/v2/shop/auth_partner`
*   **Ambiente de Teste Sandbox:** `https://partner.test-stable.shopeemobile.com/api/v2/shop/auth_partner`
*   **(China Continental) Ambiente de Teste Sandbox:** `https://openplatform.test-stable.shopee.cn/api/v2/shop/auth_partner`

## Cálculo do Parâmetro `sign`

O parâmetro `sign` não é apenas um componente do link de autorização, mas também um parâmetro usado para autenticação a cada chamada. Esta seção explica como criar uma string base para o `sign` e calcular a assinatura de autenticação através de HMAC-SHA256.

### Criação da String Base para o `sign`

Existem 3 tipos de APIs que exigem o uso de diferentes parâmetros para criar a string base do `sign` (consistente com seus parâmetros comuns).

Concatene o caminho da API (sem o host) e os parâmetros comuns abaixo em uma única string base para o `sign` na seguinte ordem:

*   **Para APIs de Loja:** `partner_id`, caminho da API, `timestamp`, `access_token`, `shop_id`
*   **Para APIs de Comerciante:** `partner_id`, caminho da API, `timestamp`, `access_token`, `merchant_id`
*   **Para APIs Públicas:** `partner_id`, caminho da API, `timestamp`

### Cálculo da Assinatura de Autenticação

Use HMAC-SHA256 para fazer o hash da string base do `sign`, e use a chave do parceiro (`partner_key`) como chave de criptografia. O valor hash hexadecimal em minúsculas é a assinatura de autenticação.

**(Inclui exemplos de código e exemplos de link de autorização na documentação original)**

