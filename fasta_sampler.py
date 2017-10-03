#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import sys

'''
Invoke as
python fasta_sampler.py
'''

def load_fasta_file_as_dict(f):
   '''
   Read the whole file in memory. This can be dangerous if
   the file is big.
   '''

   gen = dict()

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
      gen[header.rstrip()] = seq.strip()

   return gen


def sample(gen, totsize, size):
   '''
   Choose at random a sequence of given size from the genome.
   '''

   pos = random.randint(0, totsize-1)
   for seqname,seq in gen.items():
      if pos > len(seq): pos -= len(seq)
      else: break
   return seqname, pos, seq[pos:(pos+size)]



if __name__ == '__main__':
   fasta  =     sys.argv[1]
   number = int(sys.argv[2])
   size   = int(sys.argv[3])
   with open(fasta) as f:
      gen = load_fasta_file_as_dict(f)
   totsize = sum([len(a) for a in gen.values()])
   for iter in range(number):
      print '>%s_%d\n%s' % sample(gen, totsize, size)

