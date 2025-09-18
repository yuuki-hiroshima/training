
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

## 0) 準備：CSVの場所を決める。初回起動時にCSVがなければヘッダーだけ作る。

import os
import csv

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

csv_path = os.path.join(data_dir, "scores.csv")

if not os.path.exists(csv_path):
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["subject", "score"])
        print("scores.csv を新規作成しました（ヘッダーのみ）。")

## 1) 読み込み（CSV → 辞書）：CSVを開いて全行読み込み、辞書に保存する。

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

## 2) 表示（一覧・件数・平均）：科目名でソートして毎回同じ順番にする
# 各モード終了後に最新状態を表示するために関数化

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
        print(f"件数: {count} / 合計: {total} / 平均: {average}")

show_summary(scores_by_subject)

## 3) メニュー（ループ）

while True:
    print("\n--- メニュー ---")
    print("1) 追加  2) 削除  3) 保存して終了")
    choice = input("番号を入力してください:").strip()

### 3-1) 追加モード

    if choice == "1":
        while True:
            subject = input("科目名（空で追加モード終了）:").strip()
            if subject == "":
                break

            score_str = input("点数（0以上の整数）:").strip()
            try:
                score = int(score_str)
            except ValueError:
                print("整数を入力してください。")
                continue

            if score < 0:
                print("0以上の数を入力してください。")
                continue

            scores_by_subject[subject] = score
            print(f"登録しました: {subject} = {score}")
        
        show_summary(scores_by_subject)

### 3-2) 削除モード

    elif choice == "2":
        target = input("削除する科目名（空でキャンセル）:").strip()
        if target == "":
            print("キャンセルされました。")
        elif target in scores_by_subject:
            del scores_by_subject[target]
            print(f"削除しました:{target}")
        else:
            print("見つかりませんでした。")

        show_summary(scores_by_subject)
    
### 3-3) 保存して終了

    elif choice == "3":
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["subject", "score"])
            for subj in sorted(scores_by_subject.keys()):
                writer.writerow([subj, scores_by_subject[subj]])
            
        print("保存しました。終了します。")
        break
    
    else:
        print("1 / 2 / 3 のいずれかを入力してください。")

# ========== Pythonコード（Chat GPT（CSV＋JSON）） ==========

# =========================
# 成績マネージャー（CSV + JSON版）
# 変更点が分かるように ★印 を付けています
# 各行に役割コメントを付け、初学者でも追いやすくしています
# =========================

import os                      # フォルダ・ファイルの存在確認や作成に使う
import csv                     # CSVの読み書きに使う
import json                    # JSONの読み書きに使う  # ★追加

# ---------- 0) 準備 ----------
data_dir = "data"                                  # データ保存用のフォルダ名
os.makedirs(data_dir, exist_ok=True)               # 無ければ作る／あってもエラーにしない

csv_path = os.path.join(data_dir, "scores.csv")    # CSVファイルのパス
json_path = os.path.join(data_dir, "scores.json")  # JSONファイルのパス  # ★追加

# CSVが無い初回は、ヘッダーだけ書いて作成
if not os.path.exists(csv_path):
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)                     # CSVの“書き手”を用意
        writer.writerow(["subject", "score"])      # 1行目にヘッダーを書き込む
        print("scores.csv を新規作成しました（ヘッダーのみ）。")

# ---------- 1) 読み込み（CSV → 辞書） ----------
scores_by_subject = {}                             # 科目名→点数 の辞書（内部表現）

with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)                     # 1行を {"subject":..., "score":...} で返す
    for row in reader:                             # 行を1件ずつ取り出す
        subject = row["subject"].strip()           # 科目名の前後の空白を除去
        if subject == "":                          # 空の科目は無効
            continue
        try:
            score = int(row["score"])              # "90"→90 に変換（文字列→整数）
        except ValueError:                         # 文字など不正な値はスキップ
            continue
        scores_by_subject[subject] = score         # 登録 or 上書き

# ---------- 表示用の関数（共通化） ----------
def show_summary(scores_by_subject):
    """現在の一覧・件数・平均を表示する（見やすさのために関数化）"""
    subjects_sorted = sorted(scores_by_subject.keys())    # 科目名でソート（毎回同じ順に表示）
    print("=== 現在の成績 ===")
    for subj in subjects_sorted:                          # 科目を1件ずつ表示
        print(f"  {subj}: {scores_by_subject[subj]} 点")

    count = len(scores_by_subject)                        # 科目数
    if count == 0:                                        # 0件なら平均は出さない
        print("データがありません。")
    else:
        total = sum(scores_by_subject.values())           # 合計点
        average = round(total / count, 1)                 # 平均（小数第1位で四捨五入）
        print(f"件数: {count} / 合計: {total} / 平均: {average}")

# ---------- 保存系の関数（CSV/JSON） ----------
def save_to_csv(scores_by_subject, csv_path):             # ★新規関数
    """辞書の内容をCSVにヘッダー付きで上書き保存する"""
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)                            # CSVの“書き手”
        writer.writerow(["subject", "score"])             # ヘッダー行
        for subj in sorted(scores_by_subject.keys()):     # 見やすいように科目名でソートして出力
            writer.writerow([subj, scores_by_subject[subj]])

def save_to_json(scores_by_subject, json_path):           # ★新規関数
    """辞書の内容をJSONに保存する（人間が読みやすい整形つき）"""
    rows = []                                             # JSONには「行のリスト」で保存
    for subj in sorted(scores_by_subject.keys()):         # 科目名でソートして安定化
        rows.append({"subject": subj, "score": scores_by_subject[subj]})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)  # 日本語そのまま＋インデントで整形

def load_from_json(json_path):                            # ★新規関数
    """JSONから読み込み、辞書（科目→点数）に変換して返す"""
    if not os.path.exists(json_path):                     # JSONが無いときは空を返す
        print("scores.json が見つかりません。")
        return {}
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)                               # data は [{"subject":..,"score":..}, ...]
    result = {}
    for row in data:
        subj = str(row.get("subject", "")).strip()        # subject を取り出し、前後空白を除去
        if subj == "":
            continue
        try:
            sc = int(row.get("score", 0))                 # score を整数化（無ければ0想定）
        except ValueError:
            continue
        result[subj] = sc                                 # 登録 or 上書き
    return result

# ---------- 起動時の表示 ----------
show_summary(scores_by_subject)                           # 現在の状態を確認表示

# ---------- 3) メニュー（追加／削除／保存して終了／JSON読込） ----------
while True:
    print("\n--- メニュー ---")
    print("1) 追加  2) 削除  3) 保存して終了  4) JSONから読み込み（上書き）")   # ★変更（4 を追加）
    choice = input("番号を入力してください: ").strip()

    if choice == "1":                                     # 追加モード
        while True:
            subject = input("科目名（空で追加モード終了）: ").strip()
            if subject == "":
                break
            score_str = input("点数（0以上の整数）: ").strip()
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
        show_summary(scores_by_subject)                   # 追加後の状態を表示

    elif choice == "2":                                   # 削除モード
        target = input("削除する科目名（空でキャンセル）: ").strip()
        if target == "":
            print("キャンセルしました。")
        elif target in scores_by_subject:
            del scores_by_subject[target]
            print(f"削除しました: {target}")
        else:
            print("見つかりませんでした。")
        show_summary(scores_by_subject)                   # 削除後の状態を表示

    elif choice == "3":                                   # 保存して終了
        save_to_csv(scores_by_subject, csv_path)          # CSVへ保存  # ★変更（関数化）
        save_to_json(scores_by_subject, json_path)        # JSONへ保存 # ★追加
        print("CSV と JSON に保存しました。終了します。")
        break                                             # ループを抜ける

    elif choice == "4":                                   # JSONから読み込み（上書き）  # ★追加
        loaded = load_from_json(json_path)                # JSONを読み込む（辞書で戻る）
        if loaded:                                        # 読み込みに成功したら
            scores_by_subject = loaded                    # 今のデータをJSONの内容で上書き
            print("JSONから読み込みました（現在データを置き換え）。")
            show_summary(scores_by_subject)               # 置き換え結果を表示
        else:
            print("JSONの読み込みをスキップしました。")    # 何も無い or エラー時

    else:
        print("1 / 2 / 3 / 4 のいずれかを入力してください。")  # 無効入力の案内
# ========== 修正・改善点 ==========

# ========== 総括 ==========