import numpy as np
import warnings
warnings.filterwarnings('ignore')

class pat:
    # b / ((c + d)/2) * 100
    def profit_chddud(df_name,a,b,c,d,e):
        for i in range(len(df_name)-1):
            if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
                # b(-), c(-), d(-)
                if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])+abs(df_name.iloc[i][d]))/2))*100)*-1 # 절대값 변환
                # b(-), c(+), d(-) 일때
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                    # 절대값 변환 후 양수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)* -1 
                    else:
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # b(-), c(-), d(+) 일때
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                    # 절대값 변환 후 음수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
                # b(-), c(+), d(+)
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
                # a(+), b(+), c(-)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                    # 절대값 변환 후 양수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(-), c(+)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(-), c(-)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(+), c(+)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # 분모 또는 분자가 0인 경우
                elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                    df_name.loc[i,e] = 0
                # 둘다 결측치인 경우
                else:
                    df_name.loc[i,e] = np.nan
            elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
                # b(-), c(-), d(-)
                if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])+abs(df_name.iloc[i][d]))/2))*100)*-1 # 절대값 변환
                # b(-), c(+), d(-) 일때
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                    # 절대값 변환 후 양수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)* -1 
                    else:
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # b(-), c(-), d(+) 일때
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                    # 절대값 변환 후 음수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
                # b(-), c(+), d(+)
                elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
                # a(+), b(+), c(-)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                    # 절대값 변환 후 양수일 때
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(-), c(+)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                    if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                    else:
                        df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(-), c(-)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # a(+), b(+), c(+)
                elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                # 분모 또는 분자가 0인 경우
                elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                    df_name.loc[i,e] = 0
                # 둘다 결측치인 경우
                else:
                    df_name.loc[i,e] = np.nan
                    
# 증가율 함수
def pct (df_name,a,b,c,d):
    for i in range(len(df_name)-1):
        if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
            # 분모,분자가 - 인 상황
            if df_name.iloc[i][a] < 0 and df_name.iloc[i][b] < 0:
                if 0 < (((abs(df_name.iloc[i][a])/abs(df_name.iloc[i][b]))*100)-100) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][a])/abs(df_name.iloc[i][b]))*100)-100)
            #분모 +, 분자 - 인 상황
            elif df_name.iloc[i][a] < 0 and df_name.iloc[i][b] > 0:
                if -0.01 < (((abs(df_name.iloc[i][a])/df_name.iloc[i][b])*100)-100)*-1 < 0: # 전년에 양수였다가 음수로 하락이기 때문에  -1을 곱한elif
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][a])/df_name.iloc[i][b])*100)-100)*-1
            # 분모 -, 분자 + 인 상황
            elif df_name.iloc[i][a] > 0 and df_name.iloc[i][b] < 0:
                if 0.01 < (((df_name.iloc[i][a]/abs(df_name.iloc[i][b]))*100)-100) < 0:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][a]/abs(df_name.iloc[i][b]))*100)-100)
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][a] > 0 and df_name.iloc[i][b] > 0:
                if 0 < (((df_name.iloc[i][a]/df_name.iloc[i][b])*100)-100) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][a]/df_name.iloc[i][b])*100)-100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][a] == 0 or df_name.iloc[i][b] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
        elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
            # 분모,분자가 - 인 상황
            if df_name.iloc[i][a] < 0 and df_name.iloc[i][b] < 0:
                if 0 < (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100)-100) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100)-100)
            #분모 +, 분자 - 인 상황
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0:
                if -0.01 < (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100)-100)*-1 < 0: # 전년에 양수였다가 음수로 하락이기 때문에  -1을 곱한elif
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100)-100)*-1
            # 분모 -, 분자 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0:
                if 0.01 < (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100)-100) < 0:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100)-100)
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0:
                if 0 < (((df_name.iloc[i][b]/df_name.iloc[i][c])*100)-100) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/df_name.iloc[i][c])*100)-100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
                
# 수익성 계산
def profit (df_name,a,b,c,d):
    for i in range(len(df_name)-1):
        if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
            # 분모, 분자가 - 인 상황
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0:
                df_name.loc[i,d] = (((abs(df_name.iloc[i][b]) - abs(df_name.iloc[i][c]))/df_name.iloc[i][b])*100) # 분모 -
            # a - (-b) / a 일때
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0:
                df_name.loc[i,d] = (((df_name.iloc[i][b] - abs(df_name.iloc[i][c]))/df_name.iloc[i][b])*100) # b 절대값 변환
            # -a - b / -a 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0:
                df_name.loc[i,d] = (((abs(df_name.iloc[i][b]) - df_name.iloc[i][c])/df_name.iloc[i][b])*100) # a 아무대나 절대값 하나
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0:
                df_name.loc[i,d] = (((df_name.iloc[i][b] - df_name.iloc[i][c])/df_name.iloc[i][b])*100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
        elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
            # 분모, 분자가 - 인 상황
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0:
                df_name.loc[i,d] = (((abs(df_name.iloc[i][b]) - abs(df_name.iloc[i][c]))/df_name.iloc[i][b])*100) # 분모 -
            # a - (-b) / a 일때
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0:
                df_name.loc[i,d] = (((df_name.iloc[i][b] - abs(df_name.iloc[i][c]))/df_name.iloc[i][b])*100) # b 절대값 변환
            # -a - b / -a 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0:
                df_name.loc[i,d] = (((abs(df_name.iloc[i][b]) - df_name.iloc[i][c])/df_name.iloc[i][b])*100) # a 아무대나 절대값 하나
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0:
                df_name.loc[i,d] = (((df_name.iloc[i][b] - df_name.iloc[i][c])/df_name.iloc[i][b])*100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
                
def profit_tns(df_name,a,b,c,d):
    for i in range(len(df_name)-1):
        if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
            # 분모,분자가 - 인 상황
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0:
                if 0 < (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100)) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100))
            #분모 +, 분자 - 인 상황
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0:
                if -0.01 < (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100))*-1 < 0: # 전년에 양수였다가 음수로 하락이기 때문에  -1을 곱한elif
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100))*-1
            # 분모 -, 분자 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0:
                if 0.01 < (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100)) < 0:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100))
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0:
                if 0 < (((df_name.iloc[i][b]/df_name.iloc[i][c])*100)) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/df_name.iloc[i][c])*100))
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
        elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
            # 분모,분자가 - 인 상황
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0:
                if 0 < (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100)) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/abs(df_name.iloc[i][c]))*100))
            #분모 +, 분자 - 인 상황
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0:
                if -0.01 < (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100))*-1 < 0: # 전년에 양수였다가 음수로 하락이기 때문에  -1을 곱한elif
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((abs(df_name.iloc[i][b])/df_name.iloc[i][c])*100))*-1
            # 분모 -, 분자 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0:
                if 0.01 < (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100)) < 0:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/abs(df_name.iloc[i][c]))*100))
            # 분모, 분자가 + 인 상황
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0:
                if 0 < (((df_name.iloc[i][b]/df_name.iloc[i][c])*100)) < 0.01:
                    df_name.loc[i,d] = 0.01
                else:
                    df_name.loc[i,d] = (((df_name.iloc[i][b]/df_name.iloc[i][c])*100))
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0:
                df_name.loc[i,d] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,d] = np.nan
                
# b / ((c + d)/2) * 100
def profit_chddud(df_name,a,b,c,d,e):
    for i in range(len(df_name)-1):
        if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
            # b(-), c(-), d(-)
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])+abs(df_name.iloc[i][d]))/2))*100)*-1 # 절대값 변환
            # b(-), c(+), d(-) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)* -1 
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # b(-), c(-), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                # 절대값 변환 후 음수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
            # b(-), c(+), d(+)
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
            # a(+), b(+), c(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(-), c(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(-), c(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(+), c(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                df_name.loc[i,e] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,e] = np.nan
        elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
            # b(-), c(-), d(-)
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])+abs(df_name.iloc[i][d]))/2))*100)*-1 # 절대값 변환
            # b(-), c(+), d(-) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)* -1 
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # b(-), c(-), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                # 절대값 변환 후 음수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
            # b(-), c(+), d(+)
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)*-1
            # a(+), b(+), c(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(-), c(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(-), c(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # a(+), b(+), c(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2))*100)
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                df_name.loc[i,e] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,e] = np.nan
                
# b / ((c - d)/2)
def activity_tnsdns(df_name,a,b,c,d,e):
    for i in range(len(df_name)-1):
        if df_name.iloc[i][a] == df_name.iloc[i+1][a]:
            # b(-), c(-), d(-) 일때
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-abs(df_name.iloc[i][d]))/2)))*-1 # 절대값 변환
            # b(-), c(+), d(-) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))* -1 
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(-), c(-), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                # 절대값 변환 후 음수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-df_name.iloc[i][d])/2)))*-1
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
            # b(-), c(+), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-df_name.iloc[i][d])/2)))*-1
            # b(+), c(+), d(-) 일때
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(+), c(-), d(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
            # b(+), c(-), d(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(+), c(+), d(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2)))
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                df_name.loc[i,e] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,e] = np.nan
        elif df_name.iloc[i][a] == df_name.iloc[i-1][a]:
            # b(-), c(-), d(-) 일때
            if df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-abs(df_name.iloc[i][d]))/2)))*-1 # 절대값 변환
            # b(-), c(+), d(-) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))* -1 
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(-), c(-), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                # 절대값 변환 후 음수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-df_name.iloc[i][d])/2)))*-1
                else:
                    df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
            # b(-), c(+), d(+) 일때
            elif df_name.iloc[i][b] < 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((abs(df_name.iloc[i][b])/((abs(df_name.iloc[i][c])-df_name.iloc[i][d])/2)))*-1
            # b(+), c(+), d(-) 일때
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] < 0:
                # 절대값 변환 후 양수일 때
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(+), c(-), d(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] > 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-df_name.iloc[i][d])/2)))
            # b(+), c(-), d(-)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] < 0 and df_name.iloc[i][d] < 0:
                if abs(df_name.iloc[i][c]) > abs(df_name.iloc[i][d]):
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
                else:
                    df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]-abs(df_name.iloc[i][d]))/2)))
            # b(+), c(+), d(+)
            elif df_name.iloc[i][b] > 0 and df_name.iloc[i][c] > 0 and df_name.iloc[i][d] > 0:
                df_name.loc[i,e] = ((df_name.iloc[i][b]/((df_name.iloc[i][c]+df_name.iloc[i][d])/2)))
            # 분모 또는 분자가 0인 경우
            elif df_name.iloc[i][b] == 0 or df_name.iloc[i][c] == 0 or df_name.iloc[i][d] == 0:
                df_name.loc[i,e] = 0
            # 둘다 결측치인 경우
            else:
                df_name.loc[i,e] = np.nan