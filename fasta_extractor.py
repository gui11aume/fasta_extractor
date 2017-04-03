#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

'''
Invoke as
python fasta_extractor.py <fname.fasta> <start> <length>
'''

def seq_from_fasta_file(f, qname, start, length):
   '''
   Read the whole file in memory. This can be dangerous if
   the file is big.
   '''

   # Read it all.
   txt = f.read()
   
   # Split on fasta header
   for item in txt.split('>'):
      # Separate header from newline-delimited
      # sequence (proseq) and join the sequence.
      try:
         header, proseq = item.split('\n', 1)
         seq = proseq.replace('\n', '')
      except ValueError:
         continue
      if header.rstrip().startswith(qname):
         print seq[(start-1):(start+length)]
         return

if __name__ == '__main__':
   fasta  = sys.argv[1]
   qname  = sys.argv[2]
   start  = int(sys.argv[3])
   length = int(sys.argv[4])
   with open(fasta) as f:
      seq_from_fasta_file(f, qname, start, length)

