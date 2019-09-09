import pandas as pd
import numpy as np
cb = [
  [ 1,1,1,1,1,1,1,1,1 ],
  [ 1,1,1,1,1,1,0,0,1 ],
  [ 1,1,1,1,1,1,1,1,1 ],
  [ 1,1,1,1,1,1,1,1,1 ],
  [ 1,1,0,1,1,1,1,1,1 ], # i = 4
  [ 1,1,1,1,1,1,1,1,1 ],
  [ 1,1,1,1,1,1,1,0,1 ],
  [ 1,1,0,1,1,1,1,1,1 ],
  [ 1,0,1,1,1,0,1,1,1 ]
]



score_dict = {}
df_cb = pd.DataFrame(cb)

for size_of_square in range (2, len(df_cb) + 1):
    
    row_iterator = df_cb.iterrows()
    target_sq = size_of_square ** 2
    box_passed = False
    box_counter_col = 0
    tot_sq = 0
    cols_list = list(df_cb.columns)

    
    for i, row in row_iterator:
        if i != df_cb.index[-1] and (i + size_of_square) <= len(cb):
            target_cols = []

            for col_outer in cols_list:
                if col_outer != cols_list[-1] and (col_outer + size_of_square) <= len(cb):
                    for col in range(col_outer, col_outer + size_of_square):

                        if df_cb.iloc[i, col] != 1:
                            box_passed = False
                            box_counter_col = 0
                            tot_sq = 0
                            target_cols = []
                            break
                        else:
                            box_passed = True
                            box_counter_col += 1
                            tot_sq += 1
                            target_cols.append(col)

                        if box_counter_col == size_of_square:
                                    
                            for index_counter in range(i + 1, i + size_of_square):

                                if box_passed == False:
                                    box_counter_col = 0
                                    target_cols = []
                                    tot_sq = 0
                                    break

                                for column_counter in target_cols:
                                    if df_cb.iloc[index_counter, column_counter] != 1:
                                        box_passed = False
                                        tot_sq = 0
                                        box_counter_col = 0
                                        break
                                    elif df_cb.iloc[index_counter, column_counter] == 1:
                                        tot_sq += 1
                                        box_passed = True

                            if box_passed == False:
                                box_counter_col = 0
                                target_cols = []
                                tot_sq = 0

                        if tot_sq == target_sq:
                            box_counter_col = 0
                            tot_sq = 0
                            target_cols = []
                            try:
                                score_dict[size_of_square] += 1

                            except:
                                score_dict[size_of_square] = 1
print(score_dict)
