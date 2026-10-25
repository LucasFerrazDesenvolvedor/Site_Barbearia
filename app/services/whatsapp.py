import httpx
from app.config import settings

async def send_whatsapp_confirmation(client_phone: str, message: str) -> bool:
    """Envia mensagem de confirmação via WhatsApp API de terceiros."""
    if not settings.WHATSAPP_API_URL or not settings.WHATSAPP_TOKEN:
        print(f"[Simulação WhatsApp] Para: {client_phone} | Msg: {message}")
        return True

    payload = {
        "number": client_phone,
        "message": message
    }
    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(settings.WHATSAPP_API_URL, json=payload, headers=headers)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Erro ao enviar WhatsApp: {e}")
            return False