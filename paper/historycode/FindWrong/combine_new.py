import pandas as pd

def combine_data(file1,file2):
    revenue_df = pd.read_csv(file1,encoding='latin1')
    info_df = pd.read_csv(file2,encoding='latin1')
    combine_df = revenue_df.join(info_df,lsuffix='imdb_id',rsuffix='imdbID')
    combine_df.to_csv("Combine_data.csv")


if __name__ == "__main__":
    revenue_data = "Revenue.csv"
    info_data = "Info_data.csv"
    combine_data(revenue_data,info_data)
