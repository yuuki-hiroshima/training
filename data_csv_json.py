
# ========== フォルダを作る → CSVがなければヘッダーだけ作る ==========

# ---------- 「data」というフォルダと「scores.csv」というcsvファイルが作成される ----------

import os            # ファイルやフォルダ操作に使う標準モジュール
import csv           # CSVを安全に読み書きする標準モジュール

data_dir = "data"    # 変数名の理由：データ用フォルダの場所。分かりやすく "data"
os.makedirs(data_dir, exist_ok=True)  # フォルダが無ければ作る。exist_ok=Trueなら既にあってもエラーにしない

csv_path = os.path.join(data_dir, "scores.csv")  # 変数名の理由：CSVファイルの“完全なパス”

if not os.path.exists(csv_path):                 # 初回起動などでCSVが無い場合
    # "w"=新規作成/上書き、encoding="utf-8"=日本語対応、newline=""=CSVのお約束（余計な空行を防ぐ）
    with open(csv_path, "w", encoding="utf-8", newline="") as f:  
        writer = csv.writer(f)                   # writer: 行ごとにリストを書き出す道具
        writer.writerow(["subject", "score"])    # ヘッダー行を1回だけ書く
        @[and

# ========== 1件だけ追加する例 ==========

# ---------- 「scores.csv」にリストで["英語", 90]が追記される ----------

# "a" は append（追記）。既存の内容を残したまま最後に1行足す。
with open(csv_path, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)              # 行=リスト で書ける
    writer.writerow(["英語", 90])       # 1行追加：科目, 点数（点数は文字列でもOKだが、後でintに直して使う）

# ========== 読み込み（全件を取り出す例） ==========

# ---------- 実行したが特に何も起きない ----------

rows = []                                # 変数名の理由：読み込んだ行（辞書）をためる“行たち”
with open(csv_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)           # 1行を {"subject": "...", "score": "..."} の辞書で返す
    for row in reader:
        row["score"] = int(row["score"]) # CSVは文字列で入ってくるため、計算向けに整数へ直す
        rows.append(row)                 # 行のリストに追加

# rows は 例： [{"subject":"英語","score":90}, {"subject":"数学","score":70}, ...]


# ========== JSONはその形のまま保存（拡張） ==========

# ---------- 辞書やリストをそのまま保存/復元できるので構造を保ちたいときに便利 ----------

import json                               # JSONの読み書き用標準モジュール
json_path = os.path.join(data_dir, "scores.json")  # JSONの保存先

# 保存（書き出し）
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)  # ensure_ascii=Falseで日本語をそのまま、indentで見やすく

# 読み込み（読み戻し）
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)                   # data は Pythonのリスト/辞書としてそのまま使える
