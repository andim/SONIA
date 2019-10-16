#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:38:07 2019

@author: administrator
"""

import os
from sonia_length_pos import SoniaLengthPos

work_folder = './' # where data files are and output folder should be

data_file = work_folder + 'data_seqs.txt' # file with data sequences
gen_file = work_folder + 'gen_seqs.txt' # file with generated sequences if not generated internally
output_folder = work_folder + '../' # location to save model

# %%
epochs = 30  # maximum epochs to run

# %%  loading lists of sequences with gene specification
with open(data_file) as f: # this assume data sequences are in semi-colon separated text file, with gene specification
    data_seqs = [x.strip().split(';') for x in f]

gen_seqs = []

if not sample_gen:
    with open(gen_file) as f:  # this assume data sequences are in a
        gen_seqs = [x.strip().split(';') for x in f]

# creates the model object, load up sequences and set the features to learn
qm = SoniaLengthPos(data_seqs=data_seqs, gen_seqs=gen_seqs)

# %% inferring the model

qm.infer_selection(epochs=epochs)


# %% saving the model
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)
qm.save_model(output_folder + 'SONIA_model_example')