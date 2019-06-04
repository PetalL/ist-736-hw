#!/usr/bin/python

import re
from pathlib import Path
from algorithm.topic_model import Model as alg

def model(
    df,
    key_text='text',
    max_df=1.0,
    min_df=1,
    model_type=None,
    random_state=1,
    alpha=.1,
    l1_ratio=.5,
    init='nndsvd',
    num_topics=10,
    max_features=500,
    max_iter=5,
    learning_method='online',
    learning_offset=50.,
    vectorize_stopwords='english',
    stopwords=[],
    auto=False,
    ngram=1
):
    '''

    return topic model categorization.

    '''

    if not auto:
        model = alg(
            df=df,
            auto=False,
            key_text=key_text,
            stopwords=stopwords,
            ngram=ngram
        )
        model.vectorize(
            max_df=max_df,
            min_df=min_df,
            max_features=max_features,
            model_type=None,
            stopwords=vectorize_stopwords
        )

    else:
        model = alg(
            df=df,
            key_text=key_text,
            stopwords=stopwords,
            ngram=ngram
        )

    if model_type == 'nmf':
        model.train(
            num_topics=num_topics,
            random_state=random_state,
            alpha=alpha,
            l1_ratio=l1_ratio,
            init=init
        )

    else:
        model.train(
            num_topics=num_topics,
            max_iter=max_iter,
            learning_method=learning_method,
            learning_offset=learning_offset,
            random_state=random_state
        )

    return(model)