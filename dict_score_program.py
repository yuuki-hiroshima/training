
# ========== 完成形のイメージ （オリジナル）==========

# テーマ：辞書型を使ってテストの平均点と最高点を表示する。

# ユーザーが科目と点数を入力してもらい、余白を削除する。
# 0以下の数字が入力されると終了。
# 点数に文字が入力されたらエラーを表示し、再入力。
# 入力された科目と点数を辞書型の変数に格納する。
# value は点数なので計算しやすいように int で整数に変換する。
# sum・len を使い、value の平均点を計算する。
# max を使い 最高点数を取得する。
# 「平均点数は{〇〇}、最高点数は{〇〇}」と表示。

# ========== 完成形のイメージ （Chat GPT）==========

# テーマ：辞書型を使ってテストの平均点と最高点を表示する。

# 1. ユーザーが科目名を入力 → 空白を削除
# 2. ユーザーが点数を入力 → 整数に変換
#    - 数字でなければエラー表示し再入力
#    - 点数が0以下なら入力終了
# 3. 科目名をキー、点数を値として辞書に格納
# 4. すべての入力が終わったら
#    - sum・len で平均点を計算
#    - max を使って最高点の科目と点数を取得
# 5. 「平均点は〇〇点、最高点は（科目）〇〇点です」と表示

# ========== 擬似コード（オリジナル） ==========

# scores = {} 辞書型の変数を作成

# while True:
#     try:
#         i = input strip 科目名を入力+空白除去
#         s = input strip 点数を入力+空白除去
#         score = int(s)
#     except ValueError:
#         print 「整数を入力してください」と表示
#         continue 再入力

#     if score <= 0: もし点数に0以下が入力されたら
#         print 「0以下が入力されたので終了します。」と表示
#         break
#     else:
#         scores[i] = score 取得した科目名と点数を変数に格納
    
# total = sum(score) 合計点数を取得
# count = len(score) 科目数を取得
# average = total / count 平均点数を計算
# max_score = max(score) 最大点数を取得
# index = scores.keys(max_score) 最大点数の科目を取得

# print 「f"平均点数は {average}点 です。"」と表示
# print 「f"最高点数は {index}の {max_score}点 です。"」と表示

# ========== 擬似コード（Chat GPT） ==========

# scores = {}  # 辞書を作成

# while True:
#     try:
#         subject = input("科目名を入力：").strip()
#         s = input("点数を入力：").strip()
#         score = int(s)
#     except ValueError:
#         print("整数を入力してください")
#         continue

#     if score <= 0:  # 点数が0以下なら終了
#         print("0以下が入力されたので終了します。")
#         break
#     else:
#         scores[subject] = score  # 辞書に格納

# # 計算
# total = sum(scores.values())      # 合計点数
# count = len(scores)               # 科目数
# average = total / count           # 平均点数

# max_subject = max(scores, key=scores.get)  # 最高点の科目
# max_score = scores[max_subject]            # 最高点

# # 出力
# print(f"平均点数は {average} 点です。")
# print(f"最高点数は {max_subject} の {max_score} 点です。")


# ========== Pythonコード ==========

# scores = {}

# while True:
#     try:
#         i = input("科目名を入力してください(空白で終了)：").strip()
#         if i == "":
#             print("科目名に空白が入力されたので終了します。")
#             break
#         s = input("点数を入力してください(0を入力で終了)：").strip()
#         score = int(s)
#     except ValueError:
#         print("整数を入力してください。")
#         continue

#     if score <= 0:
#         print("0以下が入力されたので終了します。")
#         break
#     else:
#         scores[i] = score

# if not scores:
#     print("有効な点数が入力されなかったため、結果を表示できません。")
# else:
#     total = sum(scores.values())
#     count = len(scores)
#     average = total / count
#     max_subject = max(scores, key=scores.get)
#     max_score = scores[max_subject]

#     print("=" * 50)
#     print(f"入力された科目と点数一覧：")
#     for subject, point in scores.items():
#         print(f" {subject}: {point}点")
#     print(f"平均点数は {average:.1f}点 です。")
#     print(f"最高点数は {max_subject}の {max_score}点 です。")
#     print("=" * 50)

# ========== Pythonコード（関数化ver.） ==========

def get_scores():
    scores = {}
    while True:
        try:
            i = input("科目名を入力してください（空白なら終了）：")
            if i == "":
                print("入力が空白だったため終了します。")
                break
            s = input("点数を入力してください（0以下なら終了）：")
            score = int(s)
        except ValueError:
            print("整数を入力してください。")
            continue

        if score <= 0:
            print("0以下が入力されたので終了します。")
            break
        else:
            scores[i] = score
    return scores
        
def calc_stats(scores):
    total = sum(scores.values())
    count = len(scores)
    average = total / count

    if [total, count, average] == ["", "", None]:
        return 0, 0, None
    else:
        return total, count, average

def find_max(scores):
    max_subject = max(scores, key=scores.get)
    max_scores = scores[max_subject]

    if [max_subject, max_scores] == ["", ""]:
        return None
    else:
        return max_subject, max_scores

def show_result(scores, total, count, average, max_pair):

    if average is None or max_pair is None:
        print("結果はありません。")
    else:
        print("=" * 50)
        print(f"点数一覧：")
        for subject, point in scores.items():
            print(f" {subject}: {point}点")
        print(f"平均点数は {average:.1f}点 です。")
        print(f"最高点数は {max_pair}点 です。")
        print("=" * 50)

def main():
    scores = get_scores()
    if not scores:
        print("有効な点数が入力されなかったため、結果を表示できません。")
    else:
        total, count, average = calc_stats(scores)
        max_pair = find_max(scores)
        show_result(scores, total, count, average, max_pair)

if __name__ == "__main__":
    main()
    
# ========== 修正・改善点 ==========

# ========== 総括 ==========