###############################################################################
# Odev-04
###############################################################################
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# Görev: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan
# özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.

def cat_summary(dataframe,col_name,plot=False,num_of_square_rows=1):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    for i in range(num_of_square_rows):
        print("##############################################################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe)
        plt.show(block=True)


# Görev: check_df(), cat_summary() fonksiyonlarına4 bilgi(uygunsa) barındırannumpytarzıdocstring yazınız. (task, params, return, example)

def cat_summary(dataframe,col_name,plot=False,num_of_square_rows=1):
    """

    Parameters:
    -----------
    dataframe: dataframe
        Değişken isimleri alınmak istenilen dataframe
    col_name: str

    plot: bool

    num_of_square_rows: int

    Returns:
    --------
    None

    Examples:
    ---------

    """
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    for i in range(num_of_square_rows):
        print("##############################################################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe)
        plt.show(block=True)



