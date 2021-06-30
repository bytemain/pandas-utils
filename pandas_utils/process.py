def remove_same_element(list1, list2):
    for li in list2:
        if li not in list1:
            list1.append(li)
    return list1


def labelEncoder(dataframe, cols):
    """
    LabelEncoder args:(dataframe:pandas.DataFrame, cols:list)
    """
    for col in cols:
        c_li = sorted(dataframe[col].unique())
        c_dict = dict(zip(c_li, list(range(len(c_li)))))

        def process_notnum(x):
            return c_dict.get(x, -1)

        dataframe[col] = dataframe[col].apply(lambda x: process_notnum(x))


def testset_labelEncoder(test_dataframe, train_dataframe, cols):
    """
    让测试集也按照训练集的标签来Encoder
    LabelEncoder args:(test_data:pandas.DataFrame, train_dataframe:pandas.DataFrame, cols:list)
    """
    for col in cols:
        test_col_li = sorted(test_dataframe[col].unique())
        train_col_li = sorted(train_dataframe[col].unique())
        c_li = remove_same_element(train_col_li, test_col_li)
        c_dict = dict(zip(c_li, list(range(len(c_li)))))

        def process_notnum(x):
            return c_dict.get(x, -1)

        test_dataframe[col] = test_dataframe[col].apply(lambda x: process_notnum(x))


def normalization(dataframe, type="min-max"):
    """min-max normalization"""
    dataframe = (dataframe - dataframe.min()) / (dataframe.max() - dataframe.min())
    return dataframe
