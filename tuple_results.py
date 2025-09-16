
# ========== 完成形のイメージ（オリジナル） ==========

# 点数リストを作成 [90, 80. 70]
# 点数リストが空の場合は (0,0,0.0) を返す
# 合計点数を計算
# テストの件数をカウント
# 平均点数を計算
# 平均点数の表示は小数点第1位で四捨五入
# 上記までを関数 (compute_summary) にする
# 1つのタプルで、total, count, average を返す

# ========== 完成形のイメージ（Chat GPT） ==========

# ========== 擬似コード（オリジナル） ==========

# scores_list = [90, 80, 70] 「整数のリスト」

# if not scores_list:
#     「表示できるデータはありません」と表示
#     return (0, 0, 0.0)

# def compute_summary(scores_list): 関数を作成
#     total = sum(scores_list) 合計点数を計算
#     count = len(scores_list) 件数をカウント
#      avg = total / count      平均点数を計算
#     average = round(avg, 1)  平均点数の表示は小数点第1位で四捨五入
#     return total, count, average を返す

# total, count, average = compute_summary(scores_list) 1つのタプルで total, count, average, を返す。

# ========== 擬似コード（Chat GPT） ==========

	# •	関数名：compute_summary（合計・件数・平均の要約を返す）
	# •	受け取るもの：整数リスト scores_list
	# •	手順：
	# 1.	scores_list が空なら (0, 0, 0.0) を返す
	# 2.	total = sum(scores_list)
	# 3.	count = len(scores_list)
	# 4.	avg = total / count
	# 5.	average = round(avg, 1)（小数第1位で四捨五入）
	# 6.	(total, count, average) を1つのタプルで返す
	# •	使い方：total, count, average = compute_summary(scores_list)

# ========== Pythonコード（オリジナル） ==========

# scores_list = [90, 80, 70]

# def compute_summary(scores_list):
#     if not scores_list:
#         return (0, 0, 0.0)
#     total = sum(scores_list)
#     count = len(scores_list)
#     avg = total / count
#     average = round(avg, 1)
#     return total, count, average

# total, count, average = compute_summary(scores_list)

# print(f"点数の合計は {total}点です。")
# print(f"件数は {count}件で、平均は {average}点でした。")

# ========== Pythonコード（Chat GPT） ==========

scores_list = [90, 80, 70]

def compute_summary(scores_list: list[int]) -> tuple[int, int, float]:
    # ドキュメンテーション文字列（docstring）
    """
    点数のリストを受け取り、(合計, 件数, 平均) を返す関数。
    - 引数: scores_list … 整数のリスト。例: [90, 80, 70]
    - 空リストなら (0, 0, 0.0) を返す
    - 平均は小数第1位で四捨五入する
    """
    # 変数名の理由: scores_list は「点数（scores）のリスト」で中身が想像しやすい
    if not scores_list:              # リストが空なら
        return (0, 0, 0.0)           # (合計0, 件数0, 平均0.0) を返す方針に統一

    total = sum(scores_list)         # 合計点数を計算（sum はリスト合計を出す標準関数）
    count = len(scores_list)         # 件数（要素数）を計算（len は長さを返す標準関数）
    avg = total / count              # 平均値を計算
    average = round(avg, 1)          # 小数第1位で四捨五入（例: 83.333→83.3）

    return total, count, average     # 戻り値は3つ組（タプル）で返す

total, count, average = compute_summary(scores_list)

print(f"点数の合計は {total}点です。")
print(f"件数は {count}件で、平均は {average}点でした。")

if __name__ == "__main__":                   # スクリプトとして実行されたときだけ実行
    help(compute_summary)                    # ← 関数「定義の後」に置く（docstringが表示される）
    
# ========== 修正・改善点 ==========

# ========== 総括 ==========