#!/usr/bin/python

import numpy as np
import pandas as pd
from model.topic_model import model
from view.exploratory import explore

def topic_model(
    df,
    max_df=0.95,
    min_df=0.2,
    num_components=20,
    random_state=1,
    alpha=.1,
    l1_ratio=.5,
    init='nndsvd',
    num_words=20,
    num_topics=40,
    max_iter=5,
    learning_method='online',
    learning_offset=50.,
    auto=False,
    directory='viz',
    rotation=90,
    flag_lda=True,
    flag_nmf=True,
    plot=True,
    vectorize_stopwords='english',
    auto=False
):
    '''

    implement topic model.

    '''

    if flag_lda:
        lda = model(
            df=df,
            max_df=max_df,
            min_df=min_df,
            num_topics=num_topics,
            max_iter=max_iter,
            learning_method=learning_method,
            learning_offset=learning_offset,
            random_state=random_state,
            vectorize_stopwords=vectorize_stopwords,
            auto=False
        )
        topic_words = lda.get_topic_words(
            feature_names=lda.get_feature_names(),
            num_words=num_words
        )

        if plot:
            explore(
                pd.DataFrame(
                    topic_words,
                    columns=['topics', 'words']
                ),
                target='words',
                sent_cases={'topics': [x[0] for x in topic_words]}
            )

    if flag_nmf:
        nmf = model(
            df=df,
            max_df=max_df,
            min_df=min_df,
            num_components=num_components,
            random_state=random_state,
            alpha=alpha,
            l1_ratio=l1_ratio,
            init=init,
            vectorize_stopwords=vectorize_stopwords,
            auto=False
        )
        topic_words = nmf.get_topic_words(
            feature_names=nmf.get_feature_names(),
            num_words=num_words
        )

        if plot:
            explore(
                pd.DataFrame(
                    topic_words,
                    columns=['topics', 'words']
                ),
                target='words',
                sent_cases={'topics': [x[0] for x in topic_words]}
            )

