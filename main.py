import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


cosm_val = pd.read_csv("gardening_train.tsv", sep='\t')
cosm_val_targ = pd.read_csv("gardening_test.tsv", sep='\t')
cod = pd.crosstab(cosm_val['receipt_id'], cosm_val['item_id'])

rownames = list(cod.index)
cosm = pd.DataFrame(cosine_similarity(cod))
# print(cosm.head(10))
cosm.columns = list(cod.index)
print("Кончил")

# function to recommend items to users
def Recommender_System(receipt_id, list_to_dalete):
    #l = []
    pro_count = cosm_val.groupby(['item_id', 'receipt_id']).size().sort_values(ascending=False).unstack().fillna(0)

    # generating recommendations by miltiplying product count with the similarity scores
    recommendations = pd.DataFrame(np.dot(pro_count.values, cosm[receipt_id]), index=pro_count.index,
                                   columns=['score'])

    # filtering top best items.
    #print(recommendations)
    reco = recommendations.sort_values(by='score', ascending=False)

    re = reco.head(25)
    try:
        re = re.drop(list_to_dalete)
    except Exception:
        print("Ошибся")
        return list(re.index)
    return list(re.index)


accuracy_test = []

# print(Recommender_System(14129413683))
for i in cosm_val['receipt_id']:
    listik = np.array(cosm_val['item_id'].loc[cosm_val['receipt_id'] == i])
    rec_list = np.array(Recommender_System(i, listik))
    accuracy_test.append(rec_list[0] == cosm_val["item_id"].loc[cosm_val['receipt_id'] == i])


print(sum(accuracy_test)/len(accuracy_test))

# np.savetxt("numpy-cosi-matrix.csv", cosm.values, delimiter=",")
# cosm.to_csv("cosi-matrix.csv")
# #linear_kernel(cod)

# print(pd.read_csv("cosi-matrix.csv").shape)
# print(pd.read_csv("cosi-matrix.csv").head(1))
