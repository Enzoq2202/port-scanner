import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import socket

def scan_port(host, port, output_text):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            service = get_service(port)
            output_text.insert(tk.END, f"Porta {port} aberta - Serviço: {service}\n")
        sock.close()
    except Exception as e:
        pass
    finally:
        output_text.see(tk.END)

def get_service(port):
    services = {
        20: "FTP-DATA",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        67: "DHCP Server",
        68: "DHCP Client",
        69: "TFTP",
        80: "HTTP",
        110: "POP3",
        119: "NNTP",
        123: "NTP",
        135: "MS RPC",
        137: "NetBIOS Name Service",
        138: "NetBIOS Datagram",
        139: "NetBIOS Session Service",
        143: "IMAP",
        161: "SNMP",
        162: "SNMP Trap",
        179: "BGP",
        194: "IRC",
        443: "HTTPS",
        445: "Microsoft-DS",
        465: "SMTPS",
        514: "Syslog",
        515: "LPD",
        587: "SMTP Submission",
        631: "IPP (CUPS)",
        636: "LDAPS",
        873: "RSYNC",
        993: "IMAPS",
        995: "POP3S",
        1080: "SOCKS",
        1433: "MSSQL",
        1434: "MSSQL Monitor",
        1521: "Oracle DB",
        1723: "PPTP",
        1883: "MQTT",
        2049: "NFS",
        2375: "Docker",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5900: "VNC",
        5984: "CouchDB",
        6379: "Redis",
        6667: "IRC",
        8000: "HTTP-Alt",
        8080: "HTTP Proxy",
        8443: "HTTPS-Alt",
        9000: "SonarQube",
        9092: "Kafka",
        9200: "Elasticsearch",
        11211: "Memcached"
    }
    return services.get(port, "Serviço Desconhecido")

def port_scan(host, start_port, end_port, output_text, progress_bar):
    output_text.delete(1.0, tk.END)
    total_ports = end_port - start_port + 1
    output_text.insert(tk.END, f"Escaneando {host} de {start_port} até {end_port}...\n")
    progress_bar['value'] = 0
    progress_bar['maximum'] = total_ports

    for port in range(start_port, end_port + 1):
        scan_port(host, port, output_text)
        progress_bar.step(1)
        root.update_idletasks()

    
    output_text.insert(tk.END, "\nEscaneamento concluído.\n")
    messagebox.showinfo("Informação", "O escaneamento foi concluído!")

def start_scan():
    host = entry_host.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    if not host:
        messagebox.showerror("Erro", "O campo de host não pode estar vazio!")
        return

    port_scan(host, start_port, end_port, output_text, progress_bar)

# interface gráfica
root = tk.Tk()
root.title("Escaneamento de Portas TCP")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Host/IP:").grid(row=0, column=0, padx=5, pady=5)
entry_host = tk.Entry(frame)
entry_host.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Porta Inicial:").grid(row=1, column=0, padx=5, pady=5)
entry_start_port = tk.Entry(frame)
entry_start_port.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Porta Final:").grid(row=2, column=0, padx=5, pady=5)
entry_end_port = tk.Entry(frame)
entry_end_port.grid(row=2, column=1, padx=5, pady=5)

button_scan = tk.Button(frame, text="Iniciar Escaneamento", command=start_scan)
button_scan.grid(row=3, columnspan=2, pady=10)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)

# Adicionando a barra de progresso
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

root.mainloop()
