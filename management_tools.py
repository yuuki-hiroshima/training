
# ========== プログラムの要件（目的） ==========

# - 成績データ（**科目名・点数**）を**CSV**で保存・読み込みできるようにする。
# - 起動時にCSVを読み込み、**一覧・件数・平均（小数第1位・四捨五入）**を表示する。
# - 画面のメニューで
#     1. 追加（同じ科目は**上書き**）
#     2. 削除（科目名で1件削除）
#     3. 保存して終了 
#         を選べる。
        
# - 保存時は `data/scores.csv` に**ヘッダー付き**で上書き保存（`subject,score`）。
# - （拡張）同内容を `data/scores.json` にも保存する。
# - **科目名の表示順は毎回固定**（科目名を五十音順＝`sorted`）。

# ========== 完成形のイメージ（オリジナル） ==========

# ========== 完成形のイメージ（Chat GPT） ==========

#  入力の流れ

# 1. プログラム起動。
# 2. `data/` フォルダが無ければ作成。
# 3. `data/scores.csv` が無ければ**新規作成扱い**（ヘッダーだけ用意）。
# 4. CSVを読み込み、内部では「**科目名→点数**」の辞書（`scores_by_subject`）として保持。
# 5. 一覧・件数・平均を表示。
# 6. メニュー表示 → ユーザーが「1: 追加 / 2: 削除 / 3: 保存して終了」を選ぶ。
#     - **追加**：
#         - 科目名入力（**空なら追加モード終了**）。前後空白は削除。
#         - 点数入力（**整数0以上**のみ。文字なら再入力）。
#         - 既に同名科目があれば**上書き**。
#         - くり返し入力可能。
#     - **削除**：
#         - 科目名を1件入力。存在すれば削除、無ければ「見つからない」。
#     - **保存して終了**：
#         - `data/scores.csv` を**ヘッダー付き**で上書き保存（UTF-8 / `newline=""`）。
#         - （拡張）`data/scores.json` にも保存。
#         - 終了。
# 7. どの操作の後も、再度**一覧・件数・平均**を表示して最新状態を確認できる。

#  ルール・注意

# - **点数は整数0以上**。負の数・空文字・文字列は受け付けない（再入力）。
# - CSVの読込時、点数は**文字列→整数**に変換。
# - 表示は**科目名でソート**して出す（毎回順番が同じ）。
# - ファイルの文字コードは**UTF-8**、CSVは**`newline=""`*を付ける。
# - 実行場所はスクリプトと同じ階層を想定。相対パス `data/scores.csv` を使う。
    
#     （もし `/training/data/…` 固定にしたい場合は、コード中のパス定数だけ変えればOK）

# ========== 擬似コード（オリジナル） ==========

# ========== 擬似コード（Chat GPT） ==========

# **主要な変数名（候補）**

# - `DATA_DIR = "data"`（データフォルダ）
# - `CSV_PATH = DATA_DIR + "/scores.csv"`（CSVの保存先）
# - `JSON_PATH = DATA_DIR + "/scores.json"`（JSONの保存先・拡張）
# - `scores_by_subject: dict[str, int]`（内部管理：科目→点数の辞書）

# ---

# ## 0) 準備

# - `data/` が無ければ作成する
# - `data/scores.csv` が無ければ、**ヘッダー行だけ**書いて作成する（`subject,score`）

# ## 1) 読み込み（CSV → 辞書）

# - `scores_by_subject = {}` を用意
# - CSVを開く（`"r", encoding="utf-8", newline=""`）
# - `csv.DictReader` で1行ずつ読む
#     - `subject = row["subject"]` の前後空白を削除
#     - `score = int(row["score"])` に変換（変換できない行はスキップしてよい）
#     - `subject` が空でなければ `scores_by_subject[subject] = score` に格納（同名科目があれば**最後の値が有効**）

# ## 2) 表示（一覧・件数・平均）

# - `subjects_sorted = sorted(scores_by_subject.keys())`
# - 各科目について `科目名: 点数` を表示
# - `count = 件数（len(scores_by_subject)）`
# - `total = 点数の合計（sum(scores_by_subject.values())）`
# - `average = round(total / count, 1)`（**0件のとき**は平均の代わりに「データなし」と表示）

# ## 3) メニュー（ループ）

# - `while True:`
#     - メニュー表示：「1: 追加 / 2: 削除 / 3: 保存して終了」
#     - `choice = input("番号を入力：").strip()`
#     - **分岐**
#         - `choice == "1"` → **追加モード**へ
#         - `choice == "2"` → **削除モード**へ
#         - `choice == "3"` → **保存して終了**へ
#         - その他 → 「1/2/3 を選んでください」と再表示

# ### 3-1) 追加モード

# - `while True:`
#     - `subject = input("科目名（空で追加終了）：").strip()`
#     - `if subject == "": break`（追加モード終了）
#     - `score_str = input("点数（0以上の整数）：").strip()`
#     - **点数の検証**
#         - `try: score = int(score_str)`
#         - `except: 「整数を入力」→ continue`
#         - `if score < 0: 「0以上を入力」→ continue`
#     - `scores_by_subject[subject] = score`（新規追加 or 上書き）
#     - 「追加（or 上書き）しました」と表示
# - 追加モードを抜けたら、**2) 表示**を呼ぶ

# ### 3-2) 削除モード

# - `target = input("削除する科目名（空でキャンセル）：").strip()`
# - `if target == "":` → 「キャンセルしました」
# - `elif target in scores_by_subject:` → `del scores_by_subject[target]`、「削除しました」
# - `else:` → 「見つかりませんでした」
# - その後、**2) 表示**を呼ぶ

# ### 3-3) 保存して終了

# - **CSV保存**
#     - CSVを `"w", encoding="utf-8", newline=""` で開く
#     - `csv.writer` でヘッダー行 `["subject","score"]` を書く
#     - `for subject in sorted(scores_by_subject.keys()):`
#         - `writer.writerow([subject, scores_by_subject[subject]])`
# - **（拡張）JSON保存**
#     - `rows = [{"subject": s, "score": scores_by_subject[s]} for s in sorted(...) ]`
#     - `"w", encoding="utf-8"` で開いて `json.dump(rows, f, ensure_ascii=False, indent=2)`
# - 「保存しました。終了します。」と表示
# - `break` でメインループを抜けてプログラム終了

# ========== Pythonコード（オリジナル） ==========

# ========== Pythonコード（Chat GPT（CSVのみ）） ==========

# ## 0) 準備：CSVの場所を決める。初回起動時にCSVがなければヘッダーだけ作る。

# import os
# import csv

# data_dir = "data"
# os.makedirs(data_dir, exist_ok=True)

# csv_path = os.path.join(data_dir, "scores.csv")

# if not os.path.exists(csv_path):
#     with open(csv_path, "w", encoding="utf-8", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["subject", "score"])
#         print("scores.csv を新規作成しました（ヘッダーのみ）。")

# ## 1) 読み込み（CSV → 辞書）：CSVを開いて全行読み込み、辞書に保存する。

# scores_by_subject = {}

# with open(csv_path, "r", encoding="utf-8", newline="") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         subject = row["subject"].strip()
#         if subject == "":
#             continue
#         try:
#             score = int(row["score"])
#         except ValueError:
#             continue
#         scores_by_subject[subject] = score

# ## 2) 表示（一覧・件数・平均）：科目名でソートして毎回同じ順番にする
# # 各モード終了後に最新状態を表示するために関数化

# def show_summary(scores_by_subject):
#     subjects_sorted = sorted(scores_by_subject.keys())
#     print("=== 現在の成績 ===")
#     for subj in subjects_sorted:
#         print(f"  {subj}: {scores_by_subject[subj]} 点")

#     count = len(scores_by_subject)
#     if count == 0:
#         print("データがありません。")
#     else:
#         total = sum(scores_by_subject.values())
#         average = round(total / count, 1)
#         print(f"件数: {count} / 合計: {total} / 平均: {average}")

# show_summary(scores_by_subject)

# ## 3) メニュー（ループ）

# while True:
#     print("\n--- メニュー ---")
#     print("1) 追加  2) 削除  3) 保存して終了")
#     choice = input("番号を入力してください:").strip()

# ### 3-1) 追加モード

#     if choice == "1":
#         while True:
#             subject = input("科目名（空で追加モード終了）:").strip()
#             if subject == "":
#                 break

#             score_str = input("点数（0以上の整数）:").strip()
#             try:
#                 score = int(score_str)
#             except ValueError:
#                 print("整数を入力してください。")
#                 continue

#             if score < 0:
#                 print("0以上の数を入力してください。")
#                 continue

#             scores_by_subject[subject] = score
#             print(f"登録しました: {subject} = {score}")
        
#         show_summary(scores_by_subject)

# ### 3-2) 削除モード

#     elif choice == "2":
#         target = input("削除する科目名（空でキャンセル）:").strip()
#         if target == "":
#             print("キャンセルされました。")
#         elif target in scores_by_subject:
#             del scores_by_subject[target]
#             print(f"削除しました:{target}")
#         else:
#             print("見つかりませんでした。")

#         show_summary(scores_by_subject)
    
# ### 3-3) 保存して終了

#     elif choice == "3":
#         with open(csv_path, "w", encoding="utf-8", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(["subject", "score"])
#             for subj in sorted(scores_by_subject.keys()):
#                 writer.writerow([subj, scores_by_subject[subj]])
            
#         print("保存しました。終了します。")
#         break
    
#     else:
#         print("1 / 2 / 3 のいずれかを入力してください。")

# # ========== Pythonコード（Chat GPT（CSV＋JSON）） ==========

# # =========================
# # 成績マネージャー（CSV + JSON版）
# # 変更点が分かるように ★印 を付けています
# # 各行に役割コメントを付け、初学者でも追いやすくしています
# # =========================

# import os                      # フォルダ・ファイルの存在確認や作成に使う
# import csv                     # CSVの読み書きに使う
# import json                    # JSONの読み書きに使う  # ★追加

# # ---------- 0) 準備 ----------

# data_dir = "data"                                           # データ保存用フォルダ名（変数名の意図: *_dir は「フォルダ」を表す）
# os.makedirs(data_dir, exist_ok=True)                        # フォルダが無ければ作成。exist_ok=True で既にあってもエラーにしない

# csv_path = os.path.join(data_dir, "scores.csv")             # フォルダ＋ファイル名をOSに合わせて安全に連結（ファイルの“道”＝パス）
# json_path = os.path.join(data_dir, "scores.json")           # JSONの保存先パス（変数名の意図: *_path は「ファイルのフルパス」）

# if not os.path.exists(csv_path):                            # CSVファイルが存在しない初回起動かどうかを判定
#     with open(csv_path, "w", encoding="utf-8", newline="") as f:  # 新規作成/上書きモードで開く。UTF-8、日本語OK。newline="" は余計な空行防止
#         writer = csv.writer(f)                              # CSVの書き手を用意（リストを1行として書ける）
#         writer.writerow(["subject", "score"])               # 1行目にヘッダーを書き込む（列名を明示）
#         print("scores.csv を新規作成しました（ヘッダーのみ）")     # 状況表示（※「作成しました」に誤字あり）

# # ---------- 1) 読み込み（CSV → 辞書） ----------

# scores_by_subject = {}                                      # 科目→点数 を保持する辞書（内部表現）

# with open(csv_path, "r", encoding="utf-8", newline="") as f:  # 読み込みモードで開く（UTF-8 / newline=""）
#     reader = csv.DictReader(f)                              # 1行を {"subject": "...", "score": "..."} の辞書で返す読み手
#     for row in reader:                                      # CSV各行を1件ずつ処理
#         subject = row["subject"].strip()                    # 科目名の前後空白を削除（入力ブレに強くする）
#         if subject == "":                                   # 空文字（空行など）は無効
#             continue                                        # この行をスキップして次へ
#         try:
#             score = int(row["score"])                       # "90" → 90 に変換（文字列→整数）
#         except ValueError:                                  # 数字に変換できない不正値（例: "九十"）は
#             continue                                        # 取り込まずにスキップ
#         scores_by_subject[subject] = score                  # 登録（同じ科目があれば上書き）

# # ---------- 表示用の関数（共通化） ----------

# def show_summary(scores_by_subject):                        # 現在の一覧・件数・平均を表示する関数
#     subjects_sorted = sorted(scores_by_subject.keys())      # 科目名でソート（毎回同じ順で表示）
#     print("=== 現在の成績 ===")                               # 見出し
#     for subj in subjects_sorted:                            # 科目名を1つずつ取り出して
#         print(f"  {subj}: {scores_by_subject[subj]}点")     # 科目名と点数を表示（点数は辞書から取得）

#     count = len(scores_by_subject)                          # 登録件数（科目数）
#     if count == 0:                                          # 0件のときは平均を出さない
#         print("データがありません。")                          # データ無しメッセージ
#     else:
#         total = sum(scores_by_subject.values())             # 点数（値）の合計を計算する。keys ではなく values を合計
#         average = round(total / count, 1)                   # 平均＝合計/件数 を小数第1位で四捨五入
#         print(f"件数: {count} / 合計: {total}点 / 平均: {average}点")  # まとめ表示

# # ---------- 保存系の関数（CSV/JSON） ----------

# def save_to_csv(scores_by_subject, csv_path):                      # 役割: 「科目→点数」の辞書を CSV にヘッダー付きで保存する
#     with open(csv_path, "w", encoding="utf-8", newline="") as f:   # open: 書き込みモード。"utf-8"で日本語OK、newline=""は余計な空行防止
#         writer = csv.writer(f)                                     # csv.writer: 行（リスト）をCSV形式で書く“書き手”を作る
#         writer.writerow(["subject", "score"])                      # 1行目にヘッダーを書き込む（列名を明示）
#         for subj in sorted(scores_by_subject.keys()):              # 並びを固定するために科目名で昇順ソート（毎回同じ順で出力）
#             writer.writerow([subj, scores_by_subject[subj]])       # データ行を書き込む（[科目名, 点数]）。点数は自動で文字列として保存される

# def save_to_json(scores_by_subject, json_path):                    # 役割: 「科目→点数」の辞書を JSON に保存する
#     rows = []                                                      # JSONに書き出す前の中間リスト（行=辞書の形にそろえる）
#     for subj in sorted(scores_by_subject.keys()):                  # 表示と同じく科目名でソート（順序を安定させる）
#         rows.append({"subject": subj, "score": scores_by_subject[subj]})  # 1件ぶんの辞書を作ってリストに追加
#     with open(json_path, "w", encoding="utf-8") as f:              # JSONファイルを開く（書き込み）。UTF-8で日本語OK
#         json.dump(rows, f, ensure_ascii=False, indent=2)           # json.dump: Pythonオブジェクト→JSON文字列にして保存
#                                                                     # ensure_ascii=False: 日本語を \uXXXX にせずそのまま保存
#                                                                     # indent=2: 見やすいように2スペースで整形（人間が読みやすい）

# def load_to_json(json_path):                            # 役割: JSONファイルからデータを読み出し、「科目→点数」の辞書にして返す。変数名: json_path=JSONファイルのパス
#     if not os.path.exists(json_path):                   # os.path.exists: ファイル/フォルダの存在確認（無ければ False）
#         print("scores.json が見つかりません。")            # 役割: 利用者への通知（※typo: 正しくは 'scores.json'） 
#         return {}                                       # 役割: データが無い時は空の辞書を返して終了（呼び出し側で「データなし」として扱える）

#     with open(json_path, "r", encoding="utf-8") as f:   # open(...,"r"): 読み込みモード。encoding="utf-8": 日本語対応。with: 自動クローズ
#         data = json.load(f)                             # json.load: JSONテキスト → Pythonの型（リスト/辞書）にパース。変数名 data=読み込んだ生データ

#     result = {}                                         # 役割: 返却用の空辞書を用意。変数名 result=最終結果（subject→score）
#     for row in data:                                    # 役割: dataを1件ずつ処理。想定: row は {"subject":..., "score":...} の辞書
#         subj = str(row.get("subject", "")).strip()      # dict.get: 無ければ""。str: 型ぶれ対策。strip: 前後空白除去。変数名 subj=subjectの略
#         if subj == "":                                  # 役割: 科目名が空なら不正データとしてスキップ
#             continue                                    # 役割: 次の行へ

#         try:
#             sc = int(row.get("score", 0))               # 役割: scoreを取り出し整数化（無ければ0）。変数名 sc=scoreの略
#         except ValueError:                              # 役割: 数字に変換できない（"九十"など）ケースを安全に無視
#             continue                                    # 役割: その行は取り込まず次へ

#         result[subj] = sc                               # 役割: 結果辞書に登録（同じ科目が複数あれば“最後の値で上書き”）
#     return result                                       # 役割: 取り込み完了。科目→点数の辞書を返す

# # ---------- 起動時の表示 ----------

# show_summary(scores_by_subject)                           # 現在の状態を確認表示

# # ---------- 3) メニュー（追加／削除／保存して終了／JSON読込） ----------

# while True:                                               # 無限ループでメニューを繰り返し表示（終了時は break で抜ける）
#     print("\n--- メニュー ---")                            # 見出し（1行空けて読みやすく）
#     print("1) 追加  2) 削除  3) 保存して終了  4) JSONから読み込み（上書き）")  # 操作の選択肢を提示
#     choice = input("番号を入力してください：").strip()         # ユーザー入力を取得。strip()で前後の空白を除去

#     if choice == "1":                                     # 「追加」モードに入る
#         while True:                                       # 追加は連続で行いたいので内部ループ
#             subject = input("科目名（空で追加モード終了）：").strip()  # 科目名を入力。前後空白は削除
#             if subject == "":                             # 空文字なら追加モード終了
#                 break
#             score_str = input("点数（0以上の整数）：").strip()  # 点数は文字列で受け取る（このあと整数化）
#             try:
#                 score = int(score_str)                    # 文字列→整数に変換（"90" -> 90）
#             except ValueError:                            # 数字以外が入った場合はエラー
#                 print("整数を入力してください。")               # 再入力を促す
#                 continue                                  # この1件はスキップして追加モードを継続
#             if score < 0:                                 # 負の数は許可しない
#                 print("0以上の数を入力してください。")
#                 continue
#             scores_by_subject[subject] = score            # 辞書に登録（同じ科目があれば上書き）
#             print(f"登録しました: {subject} = {score}点")     # フィードバック表示
#         show_summary(scores_by_subject)                   # 追加モード終了後、最新の一覧・件数・平均を表示

#     elif choice == "2":                                   # 「削除」モードに入る
#         target = input("削除する科目名（空でキャンセル）：").strip()  # 削除対象の科目名を入力
#         if target == "":                                  # 空なら削除をキャンセル
#             print("キャンセルしました。")
#         elif target in scores_by_subject:                 # 辞書にその科目が存在するかチェック
#             del scores_by_subject[target]                 # 存在すれば削除
#             print(f"削除しました: {target}")              # フィードバック表示
#         else:
#             print("見つかりませんでした。")                   # 入力した科目がない場合のメッセージ
#         show_summary(scores_by_subject)                   # 削除後の一覧・件数・平均を表示

#     elif choice == "3":                                   # 「保存して終了」
#         save_to_csv(scores_by_subject, csv_path)          # CSVに上書き保存（ヘッダー付き・UTF-8・newline=""）
#         save_to_json(scores_by_subject, json_path)        # JSONにも保存（人間が読みやすい整形）
#         print("CSV と JSON に保存しました。終了します。")      # 終了メッセージ
#         break                                             # メインループを抜けて終了

#     elif choice == "4":                                   # 「JSONから読み込み（上書き）」
#         loaded = load_to_json(json_path)                  # JSONを読み込んで辞書を受け取る（空なら {}）
#         if loaded:                                        # 空でなければ（1件以上データがあれば）
#             scores_by_subject = loaded                    # 現在の成績データを読み込んだ内容で置き換え
#             print("JSONから読み込みました（現在データを置き換え）。")  # フィードバック表示
#             show_summary(scores_by_subject)               # 置き換え後の一覧・件数・平均を表示
#         else:
#             print("JSONの読み込みをスキップしました。")       # 何もなければスキップ通知

#     else:                                                 # 無効な入力（1/2/3/4 以外）
#         print("1 / 2 / 3 / 4 のいずれかを入力してください。")  # 正しい選択を促す

# ========== 学習スペース（書いたら消す） ==========

# 準備

import os
import csv
import json

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

csv_path = os.path.join(data_dir, "scores.csv")
json_path = os.path.join(data_dir, "scores.json")

if not os.path.exists(csv_path):                              
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)                                  
        writer.writerow(["subject", "score"])                   
        print("scores.csv を新規作成sました（ヘッダーのみ）")

# 読み込み

scores_by_subject = {}

with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        subject = row["subject"].strip()
        if subject == "":
            continue
        try:
            score = int(row["score"])
        except ValueError:
            continue
        scores_by_subject[subject] = score

# 表示用の関数

def show_summary(scores_by_subject):
    subjects_sorted = sorted(scores_by_subject.keys())
    print("=== 現在の成績 ===")
    for subj in subjects_sorted:
        print(f"  {subj}: {scores_by_subject[subj]} 点")

    count = len(scores_by_subject)
    if count == 0:
        print("データがありません。")
    else:
        total = sum(scores_by_subject.values())
        average = round(total / count, 1)
        print(f"件数:{count}件 / 合計:{total}点 / 平均: {average}点")

# 保存系の関数

def save_to_csv(scores_by_subject, csv_path):
    with open(csv_path, "w", encoding="utf-8", newline="")as f:
        writer = csv.writer(f)
        writer.writerow(["subject", "score"])
        for subj in sorted(scores_by_subject.keys()):
            writer.writerow([subj, scores_by_subject[subj]])

def save_to_json(scores_by_subject, json_path):
    rows = []
    for subj in sorted(scores_by_subject.keys()):
        rows.append({"subject": subj, "score": scores_by_subject[subj]})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

def load_to_json(json_path):
    if not os.path.exists(json_path):
        print("scores.json が見つかりません。")
        return {}
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = {}
    for row in data:
        subj = str(row.get("subject", "")).strip()
        if subj == "":
            continue
        try:
            sc = int(row.get("score", 0))
        except ValueError:
            continue
        result[subj] = sc
    return result

# 起動時の表示

show_summary(scores_by_subject)

# メニュー

while True:
    print("\n--- メニュー ---")
    print("1) 追加  2) 削除  3) 保存して終了  4) JSONから読み込み（上書き）")
    choice = input("番号を入力してください：").strip()

    if choice == "1":
        while True:
            subject = input("科目名（空で追加モード終了）：").strip()
            if subject == "":
                break
            score_str = input("点数（0以上の整数）：").strip()
            try:
                score = int(score_str)
            except ValueError:
                print("整数を入力してください。")
                continue
            if score < 0:
                print("0以上の数を入力してください。")
                continue
            scores_by_subject[subject] = score
            print(f"登録しました: {subject} = {score}点")
        show_summary(scores_by_subject)

    elif choice == "2":
        target = input("削除する科目名（空でキャンセル）：").strip()
        if target == "":
            print("キャンセルしました。")
        elif target in scores_by_subject:
            del scores_by_subject[target]
            print(f"削除しました: {target}")
        else:
            print("見つかりませんでした。")
        show_summary(scores_by_subject)

    elif choice == "3":
        save_to_csv(scores_by_subject, csv_path)
        save_to_json(scores_by_subject, json_path)
        print("CSV と JSON に保存しました。終了します。")
        break

    elif choice == "4":
        loaded = load_to_json(json_path)
        if loaded:
            scores_by_subject = loaded
            print("JSONから読み込みました（現在データを置き換え）。")
            show_summary(scores_by_subject)
        else:
            print("JSONの読み込みをスキップしました。")

    else:
        print("1 / 2 / 3 / 4 のいずれかを入力してください。")


# ========== 総括 ==========