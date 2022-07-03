import pandas as pd

tabel1 = pd.read_excel(
    './PNT Somatropin 1 ian 2020 - 31 dec 2021 complet.xlsx', 'la initiere')

tabel2 = pd.read_excel('./unique_names.xlsx', 'uniques')

idsToRemoveFromTable2016 = []
name_dict = {}

# for index, name in tabel2016['numele'].iteritems():
#     if(isinstance(name, str)):
#         print(name)
#         name_dict[name.lower()] = index

# print(name_dict)

# for ind, name_x in initiere['numele'].iteritems():
#     for name_y in name_dict:
#         if(name_x in name_y):
#             idsToRemoveFromTable2016.append(name_dict[name_y])

# print(idsToRemoveFromTable2016)
# tabel2016.drop(idsToRemoveFromTable2016, axis=0, inplace=True)

for ind, name_x in tabel1['numele'].iteritems():
    for index, gender in tabel1['sex'].iteritems():
        if(ind == index):
            initials = ''.join([x[0].upper() for x in name_x.split()])
            gen = 'F' if gender == 0 else 'M'
            tabel1['numele'][ind] = initials + '-' + str(gen)
# tabel2016.to_excel('./unique_names.xlsx', 'uniques')
tabel1.to_excel('./withIds/replaced_names_pnt_initials.xlsx', 'initiere')

for ind, name_x in tabel2['numele'].iteritems():
    for index, gender in tabel2['SEX'].iteritems():
        if(ind == index and isinstance(name_x, str)):
            initials = ''.join([x[0].upper() for x in name_x.split()])
            tabel2['numele'][ind] = initials + '-' + str(gender)

tabel2.to_excel('./withIds/replaced_names_initials.xlsx', 'initiere')
