
# ========== 完成形のイメージ（オリジナル） ==========

# 入力：
#     ・クラス名簿A：{"山田", "佐藤", "田中", "山田"}
#     ・クラス名簿B：{}"佐藤", "鈴木", "高橋", "佐藤"}

# 出力：
#     •	A（重複なし）
#     •	B（重複なし）
#     •	共通者（A ∩ B）
#     •	Aだけ（A − B）
#     •	Bだけ（B − A）

# ルール：
#     ・文字列中の空白は全て削除
#     ・sortedで名前順に並び替えをする

# ========== 完成形のイメージ（Chat GPT） ==========

# ========== 擬似コード（オリジナル） ==========

# 入力：
#     norm_a = {"山田", "佐藤", "田中", "山田"}.strip()
#     norm_b = {"佐藤", "鈴木", "高橋", "佐藤"}.strip()

# エラー処理：
#     空文字を削除した結果エラーになったら捨てる

# 集合へ変換：
#     set_a =
#     set_b =

# 集合演算：
#     common =
#     only_a =
#     only_b =

# 表示前：
#     sortedで並び替え

# 出力；
#     A（重複なし）、B（重複なし）、共通、Aだけ、Bだけ

# ========== 擬似コード（Chat GPT） ==========

# 入力（元データ）
# 	•	raw_a = {"山田", "佐藤", "田中", "山田"}
# 	•	raw_b = {"佐藤", "鈴木", "高橋", "佐藤"}

# 正規化（空白削除・空文字除外）
# 	•	norm_a = raw_a の各要素について：前後と途中の空白を全部取り除く → 空でなければ残す
# 	•	norm_b = raw_b の各要素について：同上

# 集合へ変換（重複削除）
# 	•	set_a = set(norm_a)
# 	•	set_b = set(norm_b)

# 集合演算
# 	•	common = set_a と set_b の共通（A ∩ B）
# 	•	only_a = set_a から set_b を引く（A − B）
# 	•	only_b = set_b から set_a を引く（B − A）

# 表示前（順番を固定）
# 	•	out_a = set_a を 名前順に並べたリスト（sorted）
# 	•	out_b = set_b を 名前順に並べたリスト
# 	•	out_common = common を 名前順に並べたリスト
# 	•	out_only_a = only_a を 名前順に並べたリスト
# 	•	out_only_b = only_b を 名前順に並べたリスト

# 出力
# 	•	A（重複なし）：out_a
# 	•	B（重複なし）：out_b
# 	•	共通者：out_common
# 	•	Aだけ：out_only_a
# 	•	Bだけ：out_only_b

# ========== Pythonコード（オリジナル） ==========

# テーマ：重複がある名簿を set に変換して“重複が消える”体験をはっきりさせる

raw_a = ["山田", "佐藤", "田中", "山田"]
raw_b = ["佐藤", "鈴木", "高橋", "佐藤"]

norm_a = {"".join(name.split()) for name in raw_a if "".join(name.split())}
norm_b = {"".join(name.split()) for name in raw_b if "".join(name.split())}

common = norm_a & norm_b
only_a = norm_a - norm_b
only_b = norm_b - norm_a

out_a = sorted(norm_a)
out_b = sorted(norm_b)
out_common = sorted(common)
out_only_a = sorted(only_a)
out_only_b = sorted(only_b)

print(f"Aのクラス（重複なし）：{out_a}")
print(f"Bのクラス（重複なし）：{out_b}")
print(f"両クラスの共通者：{out_common}")
print(f"Aだけにいる生徒：{out_only_a}")
print(f"Bにだけいる生徒：{out_only_b}")

# ========== Pythonコード（Chat GPT・内包表記あり） ==========

# =========================
# 名簿クリーナー（set基礎）
# 要件：指定の変数名（raw_a/raw_b/norm_a/norm_b/set_a/set_b/common/only_a/only_b
#       /out_a/out_b/out_common/out_only_a/out_only_b）をすべて使用
# 各行に役割コメント＋初登場の関数の簡単説明＋変数名の理由を併記
# =========================

raw_a = ["山田", "佐藤", "田中", "山田"]  # Aクラスの元名簿（重複あり）/ 変数名: raw_a = raw(加工前) + a(クラスA)
raw_b = ["佐藤", "鈴木", "高橋", "佐藤"]  # Bクラスの元名簿（重複あり）/ 変数名: raw_b = raw(加工前) + b(クラスB)

# 正規化ステップ：名前中の空白（前後・途中・全角含む）をすべて除去し、空文字は捨てる
# split(): 文字列を空白で区切ってリストにする（空白自体は消える）
# "".join([...]): 区切った要素を空文字で連結し直す＝空白が完全に取り除かれた文字列になる
norm_a = ["".join(name.split()) for name in raw_a if "".join(name.split())]  # 変数名: norm_a = normalize(正規化後) + a
norm_b = ["".join(name.split()) for name in raw_b if "".join(name.split())]  # 変数名: norm_b = normalize(正規化後) + b

# 集合へ変換（重複削除が自動で行われる）
# set(リスト): リストから集合を作る（重複が消え、順序の概念がなくなる）
set_a = set(norm_a)  # 変数名: set_a = set(集合) + a
set_b = set(norm_b)  # 変数名: set_b = set(集合) + b

# 集合演算で関係を抽出
# &: 共通（積集合）、-: 片方だけ（差集合）
common = set_a & set_b   # 両クラスに共通で在籍する人 / 変数名: common = 共通要素
only_a = set_a - set_b   # Aだけにいる人 / 変数名: only_a = only(のみ) + a
only_b = set_b - set_a   # Bだけにいる人 / 変数名: only_b = only(のみ) + b

# 表示前に順番を固定（setは順序がないため、そのままprintすると並びが毎回変わることがある）
# sorted(集合): 要素を昇順に並べ替えた「リスト」を返す（安定した見た目になる）
out_a = sorted(set_a)           # A（重複なし）を名前順リストに / 変数名: out_a = output(出力用) + a
out_b = sorted(set_b)           # B（重複なし）を名前順リストに / 変数名: out_b = output + b
out_common = sorted(common)     # 共通者を名前順リストに / 変数名: out_common = output + common
out_only_a = sorted(only_a)     # Aだけの人を名前順リストに / 変数名: out_only_a = output + only_a
out_only_b = sorted(only_b)     # Bだけの人を名前順リストに / 変数名: out_only_b = output + only_b

# 出力（確認しやすい日本語の見出しで表示）
print(f"A（重複なし）：{out_a}")       # print: 画面に表示する
print(f"B（重複なし）：{out_b}")
print(f"共通者：{out_common}")
print(f"Aだけ：{out_only_a}")
print(f"Bだけ：{out_only_b}")

# ========== Pythonコード（Chat GPT・内包表記なし・関数あり） ==========

def normalize_name(s):
    # 役割：名前文字列から前後・途中を含むすべての空白を取り除く
    # s.split(): 文字列を「空白で区切って」リストにする。空白自体はここで消える（例：" 山 田 " -> ["山","田"]）
    # "".join(...): リストの要素を「空文字」で結合して1つの文字列に戻す（例：["山","田"] -> "山田"）
    # なぜこの書き方？ -> strip() だと前後の空白しか消せないため、split()+join() で「途中の空白」もまとめて除去する
    parts = s.split()
    no_spaces = "".join(parts)
    return no_spaces

# ---------- 入力（元データ） ----------
raw_a = ["山田", "佐藤", "田中", "山田"]  # 変数名の理由：raw_a = raw(未加工) + a(クラスA)
raw_b = ["佐藤", "鈴木", "高橋", "佐藤"]  # 変数名の理由：raw_b = raw(未加工) + b(クラスB)

# ---------- 正規化（空白削除・空文字除外） ----------
norm_a = []  # 変数名の理由：norm_a = normalize(正規化後) + a
for name in raw_a:                              # 1件ずつ処理（内包表記は使わない）
    cleaned = normalize_name(name)              # 空白をすべて除去した文字列にする
    if cleaned != "":                           # 空文字は無効データとして除外
        norm_a.append(cleaned)                  # リストに追加（list.append: 末尾に要素を1つ足すメソッド）

norm_b = []  # 変数名の理由：norm_b = normalize(正規化後) + b
for name in raw_b:
    cleaned = normalize_name(name)
    if cleaned != "":
        norm_b.append(cleaned)

# ---------- 集合へ変換（重複削除） ----------
# set(リスト): リストから集合を作る。集合は「重複を自動的に1つにまとめる」性質を持つ
set_a = set(norm_a)  # 変数名の理由：set_a = set(集合) + a
set_b = set(norm_b)  # 変数名の理由：set_b = set(集合) + b

# ---------- 集合演算 ----------
# &: 積集合（共通して入っている要素）
# -: 差集合（片方にだけ入っている要素）
common = set_a & set_b  # 両クラスに共通の人 / 変数名：common = 共通
only_a = set_a - set_b  # Aだけにいる人
only_b = set_b - set_a  # Bだけにいる人

# ---------- 表示前（順番を固定） ----------
# set は順序がないため、そのまま表示すると並び順が毎回変わることがある
# sorted(集合): 要素を昇順に並べ替えた「リスト」を返す（見た目が毎回一定になって安心）
out_a = sorted(set_a)           # 変数名の理由：out_a = output(出力用) + a
out_b = sorted(set_b)           # 同上
out_common = sorted(common)     # 共通者の名前順リスト
out_only_a = sorted(only_a)     # Aだけの名前順リスト
out_only_b = sorted(only_b)     # Bだけの名前順リスト

# ---------- 出力 ----------
print(f"A（重複なし）：{out_a}")       # print: 標準出力に表示する関数
print(f"B（重複なし）：{out_b}")
print(f"共通者：{out_common}")
print(f"Aだけ：{out_only_a}")
print(f"Bだけ：{out_only_b}")

# ========== Pythonコード（Chat GPT・内包表記なし・関数なし） ==========

# =========================
# 名簿クリーナー（set基礎）内包表記なし・関数定義なし版
# 使う変数名：raw_a/raw_b/norm_a/norm_b/set_a/set_b/common/only_a/only_b
#            /out_a/out_b/out_common/out_only_a/out_only_b
# 各行に役割コメント＋初使用メソッドの説明＋変数名の理由を記載
# =========================

# ---------- 入力（元データ） ----------
raw_a = ["山田", "佐藤", "田中", "山田"]   # Aクラス元名簿（重複あり）/ 変数名: raw_a = raw(未加工) + a(クラスA)
raw_b = ["佐藤", "鈴木", "高橋", "佐藤"]   # Bクラス元名簿（重複あり）/ 変数名: raw_b = raw(未加工) + b(クラスB)

# ---------- 正規化（空白削除・空文字除外） ----------
norm_a = []                                   # 正規化後のA名簿（まだリスト）/ 変数名: norm_a = normalize + a
i = 0                                         # ループ用のカウンタ（読みやすいように明示）
while i < len(raw_a):                         # whileで1件ずつ処理（内包表記を使わないための書き方）
    name = raw_a[i]                           # 1人取り出し
    parts = name.split()                      # split(): 文字列を空白で区切ってリスト化（空白はここで消える）
    no_spaces = "".join(parts)                # "".join(リスト): 要素を空文字で連結＝前後＆途中の空白がすべて除去された文字列
    if no_spaces != "":                       # 空白しかなかった等で空文字になった場合は除外
        norm_a.append(no_spaces)              # list.append(): リストの末尾に要素を1つ追加
    i += 1                                    # 次の人へ

norm_b = []                                   # 正規化後のB名簿（リスト）/ 変数名: norm_b = normalize + b
j = 0
while j < len(raw_b):
    name = raw_b[j]
    parts = name.split()                      # A側と同じ正規化（空白を完全除去）
    no_spaces = "".join(parts)
    if no_spaces != "":
        norm_b.append(no_spaces)
    j += 1

# ---------- 集合へ変換（重複削除が自動で行われる） ----------
set_a = set(norm_a)                           # set(リスト): 重複が自動で1つにまとまる / 変数名: set_a = set + a
set_b = set(norm_b)                           # 同上 / 変数名: set_b = set + b

# ---------- 集合演算（関係を抽出） ----------
common = set_a & set_b                        # &: 積集合＝両方にいる人 / 変数名: common（共通）
only_a = set_a - set_b                        # -: 差集合＝Aだけにいる人 / 変数名: only_a
only_b = set_b - set_a                        # -: 差集合＝Bだけにいる人 / 変数名: only_b

# ---------- 表示前（順番を固定） ----------
# setは順序の概念がないため、見た目を安定させるためにsorted()で並び替えたリストを作る
out_a = sorted(set_a)                         # A（重複なし）を名前順リスト化 / 変数名: out_a = output + a
out_b = sorted(set_b)                         # B（重複なし）を名前順リスト化 / 変数名: out_b
out_common = sorted(common)                   # 共通者の名前順リスト / 変数名: out_common
out_only_a = sorted(only_a)                   # Aだけの名前順リスト / 変数名: out_only_a
out_only_b = sorted(only_b)                   # Bだけの名前順リスト / 変数名: out_only_b

# ---------- 出力 ----------
print(f"A（重複なし）：{out_a}")             # print: 画面に表示する標準関数
print(f"B（重複なし）：{out_b}")
print(f"共通者：{out_common}")
print(f"Aだけ：{out_only_a}")
print(f"Bだけ：{out_only_b}")

# ========== 修正・改善点 ==========

# ========== 総括 ==========