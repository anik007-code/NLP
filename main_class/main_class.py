import pandas as pd
from matplotlib import pyplot as plt

from configs.config_data import TRUE_DATA, FAKE_DATA


class FakeNews:
    def __init__(self):
        self.true = TRUE_DATA
        self.fake = FAKE_DATA
        self.main_data = []
        self.run()

    def run(self):
        self.print_data()

    def print_data(self):
        true_data = pd.read_csv(self.true)
        # self.main_data.append(data1)
        # print(true_data)
        fake_data = pd.read_csv(self.fake)
        # print(type(fake_data))
        # Generate labels True/Fake under new Target Column in 'true_data' and 'fake_data'
        true_data['Target'] = ['True'] * len(true_data)
        fake_data['Target'] = ['Fake'] * len(fake_data)

        # Merge 'true_data' and 'fake_data', by random mixing into a single df called 'data'
        self.data = true_data.append(fake_data).sample(frac=1).reset_index().drop(columns=['index'])
        # Target column is made of string values True/Fake, let's change it to numbers 0/1 (Fake=1)
        self.data['label'] = pd.get_dummies(self.data.Target)['Fake']
        print(self.data.shape)
        print(self.data.head())

        # Checking if our data is well-balanced
        label_size = [self.data['label'].sum(), len(self.data['label']) - self.data['label'].sum()]
        a = plt.pie(label_size, explode=[0.1, 0.1], colors=['firebrick', 'navy'], startangle=90, shadow=True,
                    labels=['Fake', 'True'], autopct='%1.1f%%')
        print(a)
    # def data_train_test_split(self):
    #     # Train-Validation-Test set split into 70:15:15 ratio
    #     # Train-Temp split
    #     train_text, temp_text, train_labels, temp_labels = train_test_split(data['title'], self.data['label'],
    #                                                                         random_state=2018,
    #                                                                         test_size=0.3,
    #                                                                         stratify=self.data['Target'])
    #     # Validation-Test split
    #     val_text, test_text, val_labels, test_labels = train_test_split(temp_text, temp_labels,
    #                                                                     random_state=2018,
    #                                                                     test_size=0.5,
    #                                                                     stratify=temp_labels)
