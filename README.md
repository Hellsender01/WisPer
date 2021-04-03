# Windows Persistence

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/en-in/windows)
[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
```ruby
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
                              
```
 
\
**Wisper** helps to maintain access to windows machine and have some other cool features like UAC Disable,Firewall Disable,Dumping Credentials,etc.


![](images/screenshot.png)

# Basic Introduction

- **Wisper** use **pypsexec** library of python to interact with target system and run command on that
- Provided user should have **Administrator** privilages
- Best part is **Antivirus does not pick this up**
- Wisper install and enable **Openssh Server** and configure it to run on startup
- Wisper enable **RDP** and configure the firewall for RDP And SSH 
- It **Disables RealTime Monitoring and Firewall**
- Also **Disable UAC and Bypass Powershell Execution Policy**
- Another cool feature is, WisPer **gather all possible credentials** on target machine
- After everthing is done or something broke down inbetween, **Wisper automatically cleans up everthing**   

# Help

 > -t or --target     ➤ Target System IPv4 Address \
 > -u or --user       ➤  Username To Authenticate With \
 > -p or --password   ➤ Password To Authenticate With \
 > -v or --version    ➤ To Show Current WisPer Version \
 > -h or --help       ➤ To Show Below Message
 
 ![](images/help.png)
 
 # Installation
 ```sh
 git clone https://github.com/Hellsender01/WisPer
 cd Wisper/
 python -m pip install -r requirements.txt
 ./wisper.py -h
 ```
 
 # Supported Windows Versions
 
  - Windows 10
  - Windows 8
  - Windows 7
  - Windows Server(Above 2008 R2)

**If you want to help with any of this, you can do it using github issues or you can submit a pull request.**

## Advisory

WisPer should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.

## License

MIT License

# Acknowledgments

[@jborean93](https://github.com/jborean93)  - [pypsexec](https://github.com/jborean93/pypsexec) \
[@AlessandroZ](https://github.com/AlessandroZ) - [Lazagne](https://github.com/AlessandroZ/LaZagne)
