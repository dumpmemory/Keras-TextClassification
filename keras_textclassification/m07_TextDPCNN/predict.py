# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/6/12 14:11
# @author   :Mo
# @function :

import pathlib
import sys
import os

project_path = str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent)
sys.path.append(project_path)

import numpy as np

from keras_textclassification.conf.path_config import path_embedding_random_char
from keras_textclassification.conf.path_config import path_model_fast_text_baiduqa_2019
from keras_textclassification.etl.text_preprocess import PreprocessText
from keras_textclassification.m07_TextDPCNN.graph import DPCNNGraph as Graph

if __name__=="__main__":
    hyper_parameters = {'model': {'label': 17,
                                  'batch_size': 64,
                                  'embed_size': 300,
                                  'filters': 3,  # 固定feature maps(filters)的数量
                                  'top_ks': [],  # 这里无用
                                  'filters_num': 256,
                                  'channel_size': 1,
                                  'dropout': 0.5,
                                  'decay_step': 100,
                                  'decay_rate': 0.9,
                                  'epochs': 20,
                                  'len_max': 50,
                                  'vocab_size': 20000,  # 这里随便填的，会根据代码里修改
                                  'lr': 1e-3,
                                  'l2': 0.0000032,
                                  'activate_classify': 'softmax',
                                  'embedding_type': 'random',  # 还可以填'random'、 'bert' or 'word2vec"
                                  'is_training': False,
                                  'model_path': path_model_fast_text_baiduqa_2019,
                                  'rnn_type': 'GRU',
                                  # type of rnn, select 'LSTM', 'GRU', 'CuDNNGRU', 'CuDNNLSTM', 'Bidirectional-LSTM', 'Bidirectional-GRU'
                                  'rnn_units': 650,  # large 650, small is 300
                                  'len_max_word': 26,
                                  # only DPCNN
                                  'pooling_size_strides': [3, 2],  # 固定1/2池化
                                  'droupout_spatial': 0.2,
                                  'activation_conv': 'linear',  # Shortcut connections with pre-activation
                                  'layer_repeats': 5,
                                  'self.full_connect_unit': 256,
                                  },
                        'embedding': {'embedding_type': 'random',
                                      'corpus_path': path_embedding_random_char,
                                      'level_type': 'char',
                                      'embed_size': 300,
                                      'len_max': 50,
                                      'len_max_word': 26
                                      },
                        }
    pt = PreprocessText
    graph = Graph(hyper_parameters)
    graph.load_model()
    ra_ed = graph.word_embedding
    ques = '你好呀'
    ques_embed = ra_ed.sentence2idx(ques)
    pred = graph.predict(np.array([ques_embed]))
    pre = pt.prereocess_idx(pred[0])
    print(pre)
    while True:
        print("请输入: ")
        ques = input()
        ques_embed = ra_ed.sentence2idx(ques)
        print(ques_embed)
        pred = graph.predict(np.array([ques_embed]))
        pre = pt.prereocess_idx(pred[0])
        print(pre)