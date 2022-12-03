import os
import sys
import openai
import json
import argparse


def MAIN(args):
  if(args.apikey):
    openai.api_key = args.apikey
    print("[+] Using API_KEY: **-***************************")
  else:
    print("[-] No API Key was given")
    print("[-] Exiting")
    sys.exit()
  #
  if(args.question):
    question = args.question
    print("[+] Asking Question: {0}".format(args.question))
  else:
    print("[-] No Question was given")
    print("[-] Exiting")
    sys.exit()
  #
  print("[+] Model: {0}".format(args.model))
  print("[+] Temperature: {0}".format(args.temperature))
  print("[+] Max Tokens: {0}".format(args.maxtokens))
  print("[+] Top P: {0}".format(args.topp))
  print("[+] Frequency Penalty: {0}".format(args.frequencypenalty))
  print("[+] Presence Penalty: {0}".format(args.presencepenalty))
  #
  print("[+] Sending question to ChatGPT...")
  #
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

