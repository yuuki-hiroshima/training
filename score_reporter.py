
# ========== 完成形のイメージ（オリジナル） ==========

# ========== 完成形のイメージ（Chat GPT） ==========

# ・ねらい（1〜2行）：テストの合計点数、平均点数を出力するプログラムの作成。追加で「並び替え」「同点処理」「上位3番目までの情報取得」。
# ・入力の流れ（終了ルール含む）：科目と点数を交互に入力。strip()後に空、だと終了。点数に文字が入力された場合は再入力。
# ・出力の内容：合計点数、平均点数、上位3つの科目と点数を表示
# ・仕様の選択：
# 	・平均は小数第1位まで。端数処理は四捨五入する。
# 	・上位3位（同点含む）の同点扱い。点数（降順）が同じなら、科目名の五十音順で並べる
# 	・同じ科目名が入力されたら上書きにする。
# 	・strip後に値が空なら終了
# 	・点数の範囲はチェックしない（100以上も可能）
# 	・0点も登録可能にする
# 	・負の点数は再入力にする
# 	・入力が1つもなければ終了メッセージを表示
# 	・同点時の並びは、科目名の文字列の昇順（漢字）
# ・想定する例（2〜4科目でOK）：
# 	・入力例：
# 科目名を入力（空で終了）：数学
# 点数を入力：90
# 科目名を入力（空で終了）：英語
# 点数を入力：90
# 科目名を入力（空で終了）：国語
# 点数を入力：70
# 科目名を入力（空で終了）：
	
# 	・期待する表示（ざっくりでOK）：
# 	=== 結果 ===
# 点数一覧（高い順）
#   英語: 90
#   数学: 90
#   国語: 70
# 同率1位：英語, 数学（90点）
# 上位3件：
#   1) 英語 90
#   2) 数学 90
#   3) 国語 70
# 合計: 250 / 科目数: 3 / 平均: 83.3

# ========== 擬似コード（オリジナル） ==========

# ========== 擬似コード（Chat GPT） ==========

# 空の「成績表」（辞書）を用意する
# 入力ループを開始
    # 科目名を入力→strip()で前後空白を除去
    # 科目名が空なら入力を終了
    # 点数を入力
        # 数字でない → 再入力
        # 負の数 → 再入力
        # 0以上の整数なら受け付け
    # 辞書に「科目名→点数」を入れる（同じ科目名は上書き）
# 登録件数が0なら「データなし」を表示して終了
# 合計・件数・平均を計算（平均は小数第1位表示／四捨五入扱い）
# 「点数の降順、点数が同じなら科目名の昇順」で並べ替えた一覧を用意
# 同率1位（最高点の科目すべて）を抽出
# **上位3位（同点含む）**を作る
    # 並べ替え済み一覧から、3位の点数をしきい値とし、
    # その点数以上の科目をすべて含める（件数が3未満ならあるだけ）
# 出力する
    # 点数一覧（高い順）
    # 同率1位（科目名すべてと点数）
    # 上位3位（同点含む）
    # 合計 / 科目数 / 平均

# ========== Pythonコード（オリジナル） ==========

# scores = {}

# while True:
#     subject = input("科目名を入力してください：").strip()
#     if subject == "":
#         print("科目名が空白のため終了します。")
#         break
    
#     try:
#         score = int(input("点数を入力してください。").strip())
#     except ValueError:
#         print("数字を入力してください。")
#         continue

#     if score < 0:
#         print("0以上の数字を入力してください。")
#         continue

#     scores[subject] = score

# if not scores:
#     print("取り扱うデータがないため、結果を表示できません。")
# else:
#     total = sum(scores.values())
#     count = len(scores)
#     avg = total / count
#     average = round(avg, 1)

#     sort_scores = sorted(scores.items(), key=lambda item:(-item[1], item[0]))   # 辞書型ではなく、タプルのリストとして格納される。

#     max_score = max(scores.values())

#     winners = []                                # 理由: 空のリストを用意して、見つかった科目名を順に入れていく
#     for subject, point in sort_scores:          # （科目名, 点数）のペアを1件ずつ確認
#         if point == max_score:                  # その点数が最高点と同じなら
#             winners.append(subject)             # winners に科目名を追加する
#     winners = sorted(winners)                   # 追加した科目名を昇順に

# #   上を内包表記した場合
# #   winners = [subject for subject, point in scores.items() if point == max_score]

#     if len(sort_scores) >= 3:                   # 上位3位の「しきい値（3位の点数）」を決める
#         third_score = sort_scores[2][1]         # 3番目の要素の点数（インデックス2）（変数名は3位の点数という意味）
#     else:
#         third_score = float('-inf')             # 3件未満なら、あるだけ全部を対象にするため最小値を設定

#     top_with_tie = [pair for pair in sort_scores if pair[1] >= third_score] # pair は ("科目名", 点数)。変数名は「上位（top）」＋「同点を含む（with_tie）」

#     print("=" * 30)
#     print("点数一覧（高い順）")
#     for subject, point in sort_scores:
#         print(f" {subject}: {point}点")
#     print(f"同率1位:{', '.join(winners)} {max_score}点")
#     print("上位3件（同点含む）：")
#     for i, (subject, point) in enumerate(top_with_tie, start=1):
#         print(f"{i}) {subject}: {point}点")
#     print(f"科目数:{count} / 合計点数:{total}点 / 平均点数:{average}点")

# ========== Pythonコード（Chat GPT） ==========

# ========== Pythonコード（関数化ver.） ==========

def read_scores():
    scores = {}
    while True:
        subject = input("科目名を入力してください：").strip()
        if subject == "":
            print("空白が入力されたので終了します。")
            break

        try:
            score = int(input("点数を入力してください：").strip())
        except ValueError:
            print("整数を入力してください。")
            continue

        if score < 0:
            print("0以上の整数を入力してください。")
            continue

        scores[subject] = score

    return scores

def calc_stats(scores):
    total = sum(scores.values())
    count = len(scores)
    avg = total / count
    average = round(avg,1)
    max_score = max(scores.values())
    return total, count, average, max_score

def sort_by_score(scores):
    ranked = sorted(scores.items(), key=lambda item:(-item[1], item[0]))
    return ranked

def find_winners(scores, max_score):
    winners = [subject for subject, point in scores.items() if point == max_score]
    winners = sorted(winners)
    return winners

def top_n_with_ties(ranked, n=3):
    if len(ranked) >= n:
        threshold = ranked[n-1][1]
    else:
        threshold = float('-inf')
    
    top_with_tie = [pair for pair in ranked if pair[1] >= threshold]
    return top_with_tie

def print_report(total, count, average, max_score, ranked, winners, top_with_tie):
    print("=" * 30)
    print("点数一覧（高い順）")
    for subject, point in ranked:
        print(f" {subject}: {point}点")
    print(f"同率1位:{', '.join(winners)} {max_score}点")
    print("上位3位（同点含む）")
    for i, (subject, point) in enumerate(top_with_tie, start=1):
        print(f"{i}) {subject}: {point}点")
    print(f"科目数:{count} 合計点数:{total}点 平均点数:{average}点")
    print("=" * 30)

def main():
    scores = read_scores()
    if not scores:
        print("表示できるデータがありません。")
    else:
        total, count, average, max_score = calc_stats(scores)
        ranked = sort_by_score(scores)
        winners = find_winners(scores, max_score)
        top_with_tie = top_n_with_ties(ranked)
        print_report(total, count, average, max_score, ranked, winners, top_with_tie)

if __name__ == "__main__":
    main()

# ========== 修正・改善点 ==========

# ========== 総括 ==========