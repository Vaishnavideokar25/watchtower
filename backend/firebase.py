import os
import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": os.environ["watchtower-backend"],
        "private_key": os.environ["-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCWlQO9WgxXZZma\nNunWNaB+w/FjoYeO1lWz8cWZsw/mpO9AnT+pTswiGNXsDWngYA5W4It9zn2kHVbR\n0zbeZjfQL6t9tGVK8IjTEUf1DYyGzko+KbcWoETio59hoiqP/7dK/6ZLbatSYgDq\nkSaHNULoqrZkDJeQXoXU33QptF0EkVoQR5QTBzyoE686+/3I4+Jf4UZAK3Q5+7nm\nKGr/dI1G6Lf+lIaMFpivCgtllDNzN54RxolbRAkaGN64hgmZo1asyowjkYkyLXW6\ntUGPgEOBTywkof7uv0qBiXxA4iBVuYLT4Yo8NcbFpY0Nhl3P11y/L1jZn0E8KC22\nlNSINui7AgMBAAECggEAFvF+f9/UCI707+/VAivql9YAFhebAXL73O6GFoyXbCOO\nRrCO7huQ89MH6S8EBklsdeVBq7oGH7bOryq47fryHxjcTstpMZljp5E2/woA8ttE\nqaMOf/aMeGHI24XraURjp5w7OLvtgiBnllXmYmyFlNDJ+IWIpFkamBwx5VbTY2oM\nI4AgJdh3e9vdYfVBvuU8XqseMbK/7v/jB1cuYLMwXl7ndLuLukmmvusvMzD8OYfr\njuD9Q3ps0fTzJQZ+3NHJ+lyRFkTMxYju6w3tHGC+Gke1WX28UFEuZ/fv2XdIo3Kp\n80sfgMVwsDLgIHhVEz6OcyI/MhtHaWsLVgwS/N7w6QKBgQDUjETIaJw28rRJZXFv\nZ65QcX9CgAZF9uLQrC+kjHUrXg5NkquL9DlGLcYZpXaCC6kpu8AHXghdLwcUJrFb\nkO1RzBZNvvNBqnmHk8JpsVzXAx1elwHz0WgE8Youvg08+Vw0i8PQlb1n25WzTLOD\nRVKjLFX9RY+t+C/SmYmIPG4jkwKBgQC1XcDkM4KJNL30TfFRS5Wz4JPbWeFG+5ZG\nrlIaMjKq+Vf9tB38GOZIGC4wKta7P6/bfgs4qu7UTMDGdJ0WprjLBgshIeaC2I6n\nsE3C4DtHmbiMcUf1htnPfJTFrMvV5TU8zFnMXj0pqY6hglwWm2WsXZh5cw26mcdl\nLHeZ89MvOQKBgQCtXtEIK5QomeYG7FEPzyF3imyEgMsdLJmsHpcqAEvemPTPv7Bg\nE1DYdqPc7YNx5jMQ0I19NO1bnO2IOVt31gpOK0uSFQx05qoEtbjh34Nb+rVtH32/\nNHNFfQP6xpkjwD6+ubZ6oHmDirBcNVdD3zrd0F8/nQrqm8PeY9C0KJ6qMwKBgE9A\nnq+ZiqsmLvN4s8DQhKRLuJCboAOCoNJWDm6ADQAFYVvtv0SQJODQIC7QKXE9jT0e\nwQyMNTz0JTETeCmTxSCCjY523+HBe+Tu96v2jDDnjWthfQ5fVQKD8AbJUXEwbakZ\nqwvRCm0QONF+w3rlgPJnG9/GVPN7i1Q8sC7ICzqRAoGBAKB2qoBKOQw6kTGgXmo8\nYpmVbmj5dw7kj+amhTR2s0k/1Bq661lTO/cT2phnfkGWX6YljiI4UJaW2AJh46dN\no37GmmRM+JrkBg8WHK5iNfVKD8gmD4quq2rbmCA1uyiY7iH2BHykRxQq4o+1O0Ky\nY16nhPJAsSxE0xBC6rhWpNsJ\n-----END PRIVATE KEY-----\n"].replace("\\n", "\n"),
        "client_email": os.environ["firebase-adminsdk-fbsvc@watchtower-backend.iam.gserviceaccount.com"],
        "token_uri": "https://oauth2.googleapis.com/token"
    })
    firebase_admin.initialize_app(cred)
