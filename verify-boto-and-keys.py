import subprocess
import boto

def keyCommand():
    output = subprocess.check_output("curl http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key",shell=True)
    return output

def main():
    name = input("Enter number for command: ")
    if name == 1:
       output = keyCommand()
       print(output)
       key = output.split(":")
       accessKey = key[0]
       print accessKey
       secretKey = key[1]
       print secretKey
       print boto.Version

if __name__ == "__main__":
    main()
