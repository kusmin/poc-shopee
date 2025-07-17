import os

PARTNER_ID = os.getenv('SHOPEE_PARTNER_ID')
PARTNER_KEY = os.getenv('SHOPEE_PARTNER_KEY')

# Ambiente de Teste Sandbox
BASE_URL = "https://partner.test-stable.shopeemobile.com"
AUTH_URL = f"{BASE_URL}/api/v2/shop/auth_partner"

# Você pode adicionar URLs de produção aqui quando for o caso
# PRODUCTION_BASE_URL = "https://partner.shopeemobile.com"
# PRODUCTION_AUTH_URL = f"{PRODUCTION_BASE_URL}/api/v2/shop/auth_partner"


