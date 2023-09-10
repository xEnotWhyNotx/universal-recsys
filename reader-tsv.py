import pandas as pd


cosm_train = pd.read_csv('cosmetic_train.tsv', sep = '\t')
cosm_val = pd.read_csv('cosmetic_val.tsv', sep = '\t')
cosm_val_targ = pd.read_csv('cosmetic_val_target.tsv', sep = '\t')
mark_train = pd.read_csv('supermarket_train.tsv', sep = '\t')
mark_val = pd.read_csv('supermarket_val.tsv', sep = '\t')
mark_val_targ = pd.read_csv('supermarket_val_target.tsv', sep = '\t')


print(cosm_train.head(2))
print(cosm_val.head(2))
print(cosm_val_targ.head(2))
print(mark_train.head(2))
print(mark_val.head(2))
print(mark_val_targ.head(2))