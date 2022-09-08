import subprocess, os, time, sys

compile_arguments = ["-std=c99","-pedantic","-Wall","-Werror"]

default_main = '''#include <stdio.h>

int main(){
  printf("Hello World!\\n");
  return 0;
}'''

curr_path = os.getcwd()

help_message = '''Cargo for C (CFC) v0.2 by Fenway Powers
  Description:
    automatic compiler and runner for gcc
    the path where cfc.py is located must NOT have ANY spaces.
  Usage:
    python3 cfc.py [argument]
  Arguments:
    create: get started with cfc.
    build: compile your source files.
    run: compile and run your source files.'''

def create():
  if "src" not in os.listdir():
    os.mkdir("src")
  
  if len(os.listdir("src")) == 0:
    subprocess.run(["touch","src/main.c"])
    with open(curr_path + "/src/main.c", "w") as f:
      f.write(default_main)
    
  if "target" not in os.listdir():
    os.mkdir("target")

def build():
  if "src" not in os.listdir() or "target" not in os.listdir():
    create()

  folder_name = curr_path.split("/")
  folder_name = folder_name[-1]

  temp = ""
  for i in folder_name:
    if i == " ":
      temp += "_"
    else:
      temp += i
  
  folder_name = temp

  print("   Compiling with arguments: " + str(compile_arguments))

  command = ["gcc","-o",curr_path+"/target/"+folder_name]
  for i in compile_arguments:
    command.append(i)
  command.append(curr_path+"/src/*.c")

  command_str = ""
  for i in command:
    command_str += i + " "

  start_time = time.time()

  subprocess.Popen(command_str, shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)

  end_time = time.time()
  time_lapsed = end_time - start_time
  print("   Compiled in " + str(time_lapsed)[0:6] + "s!\n")

  return folder_name

def run():
  folder_name = build()
  time.sleep(.1)
  subprocess.run("./target/"+folder_name,shell=True)

if " " in curr_path:
  print("Error: The path where cfc.py is located must NOT have ANY spaces.")
  sys.exit(0)

if (len(sys.argv) > 1):
  if sys.argv[1] == "create" or sys.argv[1] == "c":
    create()
  elif sys.argv[1] == "build" or sys.argv[1] == "b":
    build()
  elif sys.argv[1] == "run" or sys.argv[1] == "r":
    run()
  else:
    print(help_message)
else:
  print(help_message)