from rich.console import Console
from rich.panel import Panel
import os
import time

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

panel = Panel(
    "Script Ini saya Tutup,Mungkin Kamu Berminat Untuk Mencoba Yang Premium-Call?, Premium-Call Sudah Lengkap spam wa,call,sms,email\nMinat Hubungi 0895404759092 ,\n\nMAAF YAH UNTUK YANG FREE SAYA BELUM BISA UPDATE MUNGKIN NEXT BULAN DEPAN UPDATE SCRIPT TERBARU FREE, KAMI UPDATE CALL OPEN SOURCE SIAPA TAU KALIAN MAU FREE KUNJUNGI YOUTUBE SAYA : https://youtube.com/@VindraGanzz",
    title="[bold cyan]INFO[/bold cyan]",
    border_style="bright_blue"
)

console.print(panel)
