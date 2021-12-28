"""
Matt Crow

Use GlobalProtect VPN to connect to vpn.csus.edu
!!! disconnect when done
see '^' icon in taskbar
"""



from socket import *



HOST = "gaia.ecs.csus.edu" # didn't work for "smtp.saclink.csus.edu"
PORT = 25
ADDR = (HOST, PORT)
BUFFER_SIZE = 4096
EMAIL = "mattcrow@csus.edu" # you can change this to your own email for testing



def run():
    conn = socket(AF_INET, SOCK_STREAM) # TCP connection
    conn.connect(ADDR)

    # construct email
    headers = "\n".join([
        "subject: Simple Mail Transfer Protocol"
    ])
    body = " ".join([
        "This is a test of SMTP through socket programming.",
        "Notice how it is marked as spam, as SMTP is not validated.",
        "We need more complex protocols than this."
    ])
    msgs = [
        f'HELO there',
        f'MAIL FROM:{EMAIL}',
        f'RCPT TO:{EMAIL}',
        "DATA",
        f'{headers}\n\n{body}\n.', # Don't forget the end-of-msg symbol!
        "QUIT"
    ]

    for msg in msgs:
        print(f'Sending {msg}...')
        conn.send(f'{msg}\n'.encode())
        resp = conn.recv(BUFFER_SIZE).decode()
        print(resp)

    conn.close()



if __name__ == "__main__":
    run()
