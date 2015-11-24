#!/usr/bin/python

import sys, getopt

def main(argv):
   target_user = 'BarackObama'
   output_file = 'default.csv'
   K = 3
   try:
      opts, args = getopt.getopt(argv,"ht:o:k:",[])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt == '-t':
         target_user = arg
      elif opt == 'o':
         output_file = arg
      elif opt == '-k':
         K = int(arg)
   print 'Target user is @' + target_user
   print 'Output file is "' + output_file + '"'
   print 'Size of KMer is %i' % K
   return

def usage():
   print 'Usage: model_test.py -t <target_user> -o <output_file>'
   return

if __name__ == "__main__":
   main(sys.argv[1:])