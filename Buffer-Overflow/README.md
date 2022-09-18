# Buffer overflow (Stack Based Exploitation)
step by step guide to performing a buffer overflow attack

## Definitions
1. ESP - Extended Stack Pointer. This points to top of stack
2. EBP - Extended Base Pointer. This points to the base of the stack.
3. EIP - Extended Instruction Pointer. This points to (holds the address of)first byte of the next instruction to be executed.
4. Shellcode - small piece of code used as the payload in the exp;oitaion of a software vulnerability.

## Tools to be Used
1. Victim Machine: Windows 10. I will be using Windows 10 Enterprise, so you can head over to this [link](https://www.microsoft.com/en-us/evalcenter/download-windows-10-enterprise) and download the ISO image. Ensure to download the 32-bit edition.
2. Vulnerable Software: Vulnserver. This software will allows us to exploit the software and gain root. It can be found [here](https://github.com/stephenbradshaw/vulnserver/blob/master/vulnserver.exe)
3. Attacker Machine: Kali Linux which can be found [here](https://www.kali.org/get-kali/?hmsr=joyk.com&utm_source=joyk.com&utm_medium=referral#kali-virtual-machines)
4. Debugger: Immunity Debugger. On our Victim machine we will also be running Immunity Debugger. It can be downloaded from [here](https://softfamous.com/postdownload-file/immunity-debugger/24148/9572/)
 
Note: For this walkthrough I'll be using Virtual Box. So you can install the victim and attacker machine in virtual box for following purposes. Ensure that you have disabled the Windows Security Defender to allow vulnserver to run on Windows. Also, ensure your Windows machine is not behind NAT.


## Lets get our hands dirty now.

Open your Windows machine then open you Kali Linux machine. On your Windows machine run Immunity Debugger as administrator and run vulnserver as administrator also. Go to Immunity debugger and on the top left click on the file menu and attach vulnserver to it.Ensure Immnunity Debugger is running by clicking on the red play button. We are then going to connect to vulnserver using our kali machine. Fire up a terminal and run ```nc -nv your_victim_machine_ip 9999```. Enter the command HELP to see available commands. This should look like this 


![connection](Buffer-Overflow/screenshots/Screenshot_2022-09-18_08_08_54.png)

As we can see vulnserver server provides us with a couple of commands so what we are going to do next is attempt to find which one is vulnerable.

1. **Spiking**

This is a method that we are going to use to find vulnerable parts of vulnserver. We are going to use the ```generic_send_tcp``` tool to assist us in spiking.  The usage of the tool is as shown ```generic_send_tcp host port spike_script SKIPVAR SKIPSTR```. The host will be the IP address of victim machine. The port is 9999 by default. Ideally in Spiking you spike multiple commands. Here we are going to spike the ```TRUN``` command since I already know it's a vulnerable one. I have provided the spike script for the TRUN command. When you run that command you will notice that Immunity Debugger immediately starts blinking. Your vulnserver has actually crashed. We see an access violation as shown on Immunity Debugger which means that ```TRUN``` is actually vulnerable. If we look at the registers we can pick out some information. 
![registers after spiking](Buffer-Overflow/screenshots/spike.png).

 We sent TRUN command with a bunch of As. Imagine these As going into a buffer space. Normally, the As should fill in the buffer space, but as we see they have overflown and gone over the ESP, EBP and EIP registers. If we can control the EIP we can point it to malicious code so lets go to fuzzing as the next step. 

2. **Fuzzing** 

Similar to spiking but fuzzing is a method that we are going to use to send a bunch of characters to the vulnerable program and see whether we can break it. Here we will be using a Python script. I have provided the script. Remember to restart vulnserver and immunity debugger and reattach vulnserver to immunity debugger any time you crash vulnserver. Make sure everything is running. After running your fuzzing script, check Immunity debugger and you will see that it displays access violation and stops after some seconds. This means we have successfully fuzzed the TRUN command.
Hit ```ctrl C ``` to cancel at check the number of bytes it took to crash the program. This varies but you should see something like this.

![fuzzing](Buffer-Overflow/screenshots/Screenshot_2022-09-18_12-06-54.png)

3. Finding the offset
If we do break our program we want to know at what point the program crashed

4. Overwriting the EIP
We are going to use the Offset to overwrite the EIP

5. Finding Bad Characters 
Once we have the EIP controlled we want to have a few house clean up things. One is finding bad characters. This doesn't have to make sense right now.

6. Finding the right module
This is also anoteher house clean up method.

7. Generating the shellcode
We can now generate the shellcode. This malicious payload that is going to allow us to gain a reverse shell. We will point the EIP to the malicious shellcode
8. Root!
Finally we are going to gain the root.
