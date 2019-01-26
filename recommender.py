import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# fetch data and format it
data = fetch_movielens(min_rating=4.0)

# print training and testing data
print(repr(data['train']))
print(repr(data['test']))


# creating the model.
model = LightFM(loss='warp')

# warp means (weighted approximate rank pairwise)

# train the model
model.fit(data['train'], epochs=25, num_threads=3)


def sample_recommendations(model, data, user_ids):

    # number of users and movies in training data
    n_users, n_items = data['train'].shape

    # generating recommendations for each user which we have created.
    for user_id in user_ids:
        # movie they already like.
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        # movies our model predict which they will like.
        scores = model.predict(user_id, np.arange(n_items))
        # rank them in order of most liked to lease
        top_items = data['item_labels'][np.argsort(-scores)]

        # printing the results.
        print('User %s' % user_id)
        print('\t Known Positives.')

        for x in known_positives[:5]:
            print(x)

        # printing the predictions
        for x in top_items[:3]:
            print(x)

# calling the predictions functions
sample_recommendations(model, data, [3, 25, 450])

