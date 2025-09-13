
# ========== 完成形のイメージ （オリジナル）==========

# テーマ：テストの平均点を計算するプログラム

# テストの点数を1つずつ入力してもらいリストに格納
# 0以下を入力したら終了
# 数字以外を入力したら再入力
# リストの文字列を整数に変換
# sum len を使って平均点を計算する。
# 平均点数を表示する。

# ========== 完成形のイメージ （Chat GPT）==========

# 改善後の完成形イメージ（整理版）

# ユーザーに点数を1つずつ入力してもらう（0以下で終了）
# 入力値を int() に変換してリストに追加
# 数字以外なら「整数を入力してください」と表示して再入力
# 終了後、リストの合計と要素数から平均を計算
# 平均点を表示する（小数点1桁で表示）

# ========== 擬似コード （オリジナル）==========

# score = [] リストの変数を作成

# for i in range(): 繰り返し点数を入力
#     score = int(input("点数を入力してください。（0以下を入力すると終了）：")).strip()
#     if score <= 0: もし入力された点数が0以下なら
#         「0以下が入力されたので入力を終了します。」と表示
#         break
#     elif 入力した値が数字以外なら
#         「整数を入力してください。」と表示
#         continue

# total = sum(score) 合計点数を計算
# count = len(score) リストの個数を計算
# average = total / count 合計点数をリストの個数で割って平均点数を算出

# 「あなたの平均点数は{average}です。」と表示

# ========== 擬似コード （Chat GPT）==========

# scores = []   # 点数を入れるリストを用意

# while True:
#     s = input("点数を入力してください（0以下で終了）：").strip()
#     try:
#         score = int(s)            # 整数に変換
#     except ValueError:
#         「整数を入力してください」と表示
#         continue                  # 再入力へ

#     if score <= 0:
#         「0以下が入力されたので終了します」と表示
#         break
#     else:
#         scores.append(score)      # リストに追加

# total = sum(scores)               # 合計点数
# count = len(scores)               # 入力数
# average = total / count           # 平均点数

# 「あなたの平均点数は {average:.1f} です」と表示


# ========== Pythonコード ==========

# scores = []

# while True:
#     s = input("点数を入力してください（0以下で終了）：").strip()
#     try:
#         score = int(s)
#     except ValueError:
#         print("整数を入力してください。")
#         continue

#     if score <= 0:
#         print("0以下が入力されたため終了します。")
#         break
#     else:
#         scores.append(score)

# if len(scores) > 0:
#     total = sum(scores)
#     count = len(scores)
#     average = total / count

#     print("=" * 40)
#     print(f"点数の一覧：{scores}")
#     print(f"合計点数は {total}点 で、平均点数は {average:.1f}点 です")
#     print("=" * 40)
# else:
#     print("有効な点数が入力されたかったため、結果を表示できません。")

# ========== Pythonコード（関数化ver.） ==========

def get_scores():
    scores = []
    while True:
        s = input("点数を入力してください。(0以下で終了)：").strip()
        try:
            score = int(s)
        except ValueError:
            print("数字を入力してください。")
            continue

        if score <= 0:
            print("0以下が入力されたので終了します。")
            break
        else:
            scores.append(score)
    return scores

def calc_stats(scores):
    if not scores:
        return 0, 0, None
    total = sum(scores)
    count = len(scores)
    average = total / count
    return total, count, average

def show_result(scores, total, count, average):
    print("=" * 40)
    if average is None:
        print("無効な値が入力されたため、結果を表示できません。")
    else:
        print(f"点数の一覧：{scores}")
        print(f"合計点数は {total}点、 平均点数は {average:.1f}点 です。")
    print("=" * 40)

def main():
    scores = get_scores()
    total, count, average = calc_stats(scores)
    show_result(scores, total, count, average)

if __name__ == "__main__":
    main()
# ========== 修正・改善点 ==========

# ========== 総括 ==========