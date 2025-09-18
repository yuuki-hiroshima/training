
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


## 0) 準備

- `data/` が無ければ作成する
- `data/scores.csv` が無ければ、**ヘッダー行だけ**書いて作成する（`subject,score`）

## 1) 読み込み（CSV → 辞書）

- `scores_by_subject = {}` を用意
- CSVを開く（`"r", encoding="utf-8", newline=""`）
- `csv.DictReader` で1行ずつ読む
    - `subject = row["subject"]` の前後空白を削除
    - `score = int(row["score"])` に変換（変換できない行はスキップしてよい）
    - `subject` が空でなければ `scores_by_subject[subject] = score` に格納（同名科目があれば**最後の値が有効**）

## 2) 表示（一覧・件数・平均）

- `subjects_sorted = sorted(scores_by_subject.keys())`
- 各科目について `科目名: 点数` を表示
- `count = 件数（len(scores_by_subject)）`
- `total = 点数の合計（sum(scores_by_subject.values())）`
- `average = round(total / count, 1)`（**0件のとき**は平均の代わりに「データなし」と表示）

## 3) メニュー（ループ）

- `while True:`
    - メニュー表示：「1: 追加 / 2: 削除 / 3: 保存して終了」
    - `choice = input("番号を入力：").strip()`
    - **分岐**
        - `choice == "1"` → **追加モード**へ
        - `choice == "2"` → **削除モード**へ
        - `choice == "3"` → **保存して終了**へ
        - その他 → 「1/2/3 を選んでください」と再表示

### 3-1) 追加モード

- `while True:`
    - `subject = input("科目名（空で追加終了）：").strip()`
    - `if subject == "": break`（追加モード終了）
    - `score_str = input("点数（0以上の整数）：").strip()`
    - **点数の検証**
        - `try: score = int(score_str)`
        - `except: 「整数を入力」→ continue`
        - `if score < 0: 「0以上を入力」→ continue`
    - `scores_by_subject[subject] = score`（新規追加 or 上書き）
    - 「追加（or 上書き）しました」と表示
- 追加モードを抜けたら、**2) 表示**を呼ぶ

### 3-2) 削除モード

- `target = input("削除する科目名（空でキャンセル）：").strip()`
- `if target == "":` → 「キャンセルしました」
- `elif target in scores_by_subject:` → `del scores_by_subject[target]`、「削除しました」
- `else:` → 「見つかりませんでした」
- その後、**2) 表示**を呼ぶ

### 3-3) 保存して終了

- **CSV保存**
    - CSVを `"w", encoding="utf-8", newline=""` で開く
    - `csv.writer` でヘッダー行 `["subject","score"]` を書く
    - `for subject in sorted(scores_by_subject.keys()):`
        - `writer.writerow([subject, scores_by_subject[subject]])`
- **（拡張）JSON保存**
    - `rows = [{"subject": s, "score": scores_by_subject[s]} for s in sorted(...) ]`
    - `"w", encoding="utf-8"` で開いて `json.dump(rows, f, ensure_ascii=False, indent=2)`
- 「保存しました。終了します。」と表示
- `break` でメインループを抜けてプログラム終了

# ========== Pythonコード（Chat GPT） ==========

# ========== 修正・改善点 ==========

# ========== 総括 ==========