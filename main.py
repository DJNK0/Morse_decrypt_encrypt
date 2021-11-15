#!/usr/bin/env
__author__ = "David Kampmeier"
__license__ = "MIT"
__version = "1.0"


morse = {
  "a":'.-',
  "b":'-...',
  "c":'-.-.',
  "d":'-..',
  "e":'.',
  "f":'..-.',
  "g":'--.',
  "h":'....',
  "i":'..',
  "j":'.---',
  "k":'-.-',
  "l":'.-..',
  "m":'--',
  "n":'-.',
  "o":'---',
  "p":'.--.',
  "q":'--.-',
  "r":'.-.',
  "s":'...',
  "t":'-',
  "u":'..-',
  "v":'...-',
  "w":'.--',
  "x":'-..-',
  "z":'..--'
}

def encrypt(string):
  string = string.lower()
  answer = ''
  for char in string:
    if char == ' ':
      answer += '\\'
    if char.isalpha(): 
      answer += morse[char] + " "
    else:
      answer += char
  return answer

def decrypt(string):
  answer = ' '
  reverse_morse = {value: key for (key, value) in morse.items()}
  string = string.split(' ')

  for char in string:
    if char == "\\":
      answer += ' '
    elif char != '':
      answer += reverse_morse[char]
    else:
      answer += ' '
  return answer
    
string = '-.. . ..-- . \ .-.. . ... \ .. ... \ ..-- . . .-. \ .. -. - . .-. . ... .- -. -'
print((decrypt(string)))
