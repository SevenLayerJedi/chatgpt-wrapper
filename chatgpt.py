import os
import sys
import io
import openai
import json
import argparse


class bcolors:
  # Taken from stackoverflow
  # https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def MAIN(args):
  OBLIGATORY_BANNER()
  if(args.apikey):
    openai.api_key = args.apikey
    print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Using API_KEY: " + bcolors.ENDC + "**-***************************" + bcolors.ENDC)
  else:
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "No API Key was given" + bcolors.ENDC)
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "Exiting..." + bcolors.ENDC)
    sys.exit()
  #
  if(args.question):
    question = args.question
    print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Asking Question: " + bcolors.ENDC + "{0}".format(args.question) + bcolors.ENDC)
  else:
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "No Question was given" + bcolors.ENDC)
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "Exiting..." + bcolors.ENDC)
    sys.exit()
  #
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Model: " + bcolors.ENDC + "{0}".format(args.model) + bcolors.ENDC)
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Temperature: " + bcolors.ENDC + "{0}".format(args.temperature) + bcolors.ENDC)
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Max Tokens: " + bcolors.ENDC + "{0}".format(args.maxtokens) + bcolors.ENDC)
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Top P: " + bcolors.ENDC + "{0}".format(args.topp) + bcolors.ENDC)
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Frequency Penalty: " + bcolors.ENDC + "{0}".format(args.frequencypenalty) + bcolors.ENDC)
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Presence Penalty: " + bcolors.ENDC + "{0}".format(args.presencepenalty) + bcolors.ENDC)
  #
  print("[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + bcolors.OKCYAN + "Sending question to ChatGPT..." + bcolors.ENDC)
  #
  try:
    response = openai.Completion.create(
      model=args.model,
      prompt=question,
      temperature=args.temperature,
      max_tokens=args.maxtokens,
      top_p=args.topp,
      frequency_penalty=args.frequencypenalty,
      presence_penalty=args.presencepenalty
    )
    #
    rText = response['choices'][0]['text']
    print(rText)
    print("")
  except openai.error.AuthenticationError:
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "ERROR: BAD API KEY" + bcolors.ENDC)
  except Exception as e:
    print("[" + bcolors.FAIL + "-" + bcolors.ENDC + "] " + bcolors.FAIL + "ERROR: {0}".format(e) + bcolors.ENDC)


def OBLIGATORY_BANNER():
  print("")
  with open('banner', mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    for l in lines:
      print(bcolors.OKGREEN + l.rstrip() + bcolors.ENDC)
    print(bcolors.HEADER + "\t\tPython wrapper created by: Keith Smith" + bcolors.ENDC)
    print(bcolors.HEADER + "\t\t\tsmith.itpro@gmail.com" + bcolors.ENDC)
    print(bcolors.HEADER + "\t\t\thttps://twitter.com/SevenLayerJedi" + bcolors.ENDC)
    print("")


if __name__ == "__main__":
  my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@',
  formatter_class=argparse.RawTextHelpFormatter)
  my_parser.add_argument('-a',
                      '--apikey',
                      nargs='?',
                      const="",
                      type=str,
                      default="",
                      help='OpenAI API Key \n')
  my_parser.add_argument('-m',
                      '--model',
                      nargs='?',
                      const="text-davinci-003",
                      type=str,
                      default="text-davinci-003",
                      help='OpenAI Model. Available models: \n' +
											'\ttext-davinci-003 \n' +
                      '\ttext-curie-001 \n' +
                      '\ttext-babbage-001 \n' +
                      '\ttext-ada-001 \n' +
                      '\ttext-davinci-002 \n' +
                      '\ttext-davinci-001')
  my_parser.add_argument('-t',
                      '--temperature',
                      nargs='?',
                      const=.7,
                      type=float,
                      default=.7,
                      help='The temperature controls the randomness. \n' +
											'\tAcceptable Values: 0-1 \n' + 
                      '\tDefault Value: 0.7')
  my_parser.add_argument('-mt',
                      '--maxtokens',
                      nargs='?',
                      const=256,
                      type=int,
                      default=256,
                      help='One token is roughly 4 characters \n' +
                      '\Acceptable Values: 0-2048 or 4000 \n' +
											'\tDefault Value: 256')
  my_parser.add_argument('-tp',
                      '--topp',
                      nargs='?',
                      const=1,
                      type=int,
                      default=1,
                      help='Controls diversity via nucleus sampling \n' +
                      '\tAcceptable Values: 0-1 \n' +
											'\tDefault Value: 1')
  my_parser.add_argument('-fp',
                      '--frequencypenalty',
                      nargs='?',
                      const=0,
                      type=int,
                      default=0,
                      help='How much to penalize new tokens based on their existing frequency \n' +
                      '\tAcceptable Values: 0-2 \n' +
											'\tDefault Value: 0')
  my_parser.add_argument('-pp',
                      '--presencepenalty',
                      nargs='?',
                      const=0,
                      type=int,
                      default=0,
                      help='How much to penalize new tokens based on whether they appear in text so far\n' +
                      '\tAcceptable Values: 0-2 \n' +
											'\tDefault Value: 0')
  my_parser.add_argument('-q',
                      '--question',
                      nargs='?',
                      const="",
                      type=str,
                      default="",
                      help='The question you have for ChatGPT \n' +
                      '\tExample: \n' +
                      '\tWhat is the answer to life 42?')
  my_parser.add_argument('--about',
                      help='Wrapper created by Keith Smith \n' +
                      '\tsmith.itpro@gmail.com')
  my_parser.add_argument('-v',
                      '--verbose',
                      action='store_true',
                      help='Output verbose information to the screen')
  args = my_parser.parse_args()
  MAIN(args)

