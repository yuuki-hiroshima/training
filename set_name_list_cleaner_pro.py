
# ========== プログラムの要件（目的） ==========

# 2つのクラス名簿を作成する
# 重複した名前は排除してほしい
# 各クラスの名簿で共通した名前を知りたい
# 各クラスの名簿で1つ目のクラスにだけいる名前を知りたい
# 各クラスの名簿で2つ目のクラスにだけいる名前を知りたい
# プログラムを起動するたびに、名前順は固定してほしい
# 特定の名前が各クラスにいるのか調べる機能がほしい

# ========== 完成形のイメージ（オリジナル） ==========

# 入力：
#     ・2つのクラス名簿を作成する
# 処理：
#     ・クラス名簿から空白を削除する
#     ・クラス名簿をsetに変換する
#     ・2つのクラス名簿で共通した名前を取り出す
#     ・1つ目のクラス名簿だけに存在する名前を取り出す
#     ・2つ目のクラス名簿だけに存在する名前を取り出す
#     ・取り出したデータをソートして名前順を固定する
#     ・特定の名前を検索できるようにする
# 出力： 
#     ・「各クラスで共通した名前は{A & B}です。」と表示
#     ・「1つ目のクラスにだけ存在する名前は{A - B}です。」と表示
#     ・「2つ目のクラスにだけ存在する名前は{B - A}です。」と表示
#     ・「検索した名前は{どこにいるかを表示}にいます。」or「検索した名前はいません」と表示

# ========== 完成形のイメージ（Chat GPT） ==========

# ========== 擬似コード（オリジナル） ==========

# 入力：
# names_a = [1つ目のクラス名簿（クラスA）]
# names_b = [2つ目のクラス名簿（クラスB）]

# 処理：
# norm_a = {1つ目のクラス名簿から空白をすべて削除。空文字は捨てセットに変換}
# norm_b = {2つ目のクラス名簿から空白をすべて削除。空文字は捨てセットに変換}

# common = norm_a & norm_b 共通した名前を取り出す
# only_a = norm_a - norm_b 1つ目のクラスにだけ存在する名前を取り出す。
# only_b = norm_b - norm_a 2つ目のクラスにだけ存在する名前を取り出す。

# sort_common = sorted(common)    名前の順番を固定
# sort_only_a = sorted(only_a)    名前の順番を固定
# sort_only_b = sorted(only_b)    名前の順番を固定


# search = input("検索したい名前を入力してください(空白で終了)：").strip()    名前を検索する
# if not search:
#     print("空白のため終了します。")
# elif search in norm_a and search in norm_b:
#     print("検索した名前はどちらのクラスにも存在します。")
# elif search in norm_a:
#     print("検索した名前はクラスAに存在します。")
# elif search in norm_b:
#     print("検索した名前はクラスBに存在します。")
# else:
#     print("検索した名前は存在しません。")

# 出力：
# print(f"各クラスで共通した名前は{A & B}です。")
# print(f"1つ目のクラスにだけ存在する名前は{A - B}です。")
# print(f"2つ目のクラスにだけ存在する名前は{B - A}です。")

# ========== 擬似コード（Chat GPT） ==========

# ========== Pythonコード（オリジナル） ==========

# names_a = ["田中", "山田", "鈴木", "鈴木"]
# names_b = ["東風平", "恵比寿", "御手洗", "田中"]

# norm_a = {"".join(name.split()) for name in names_a if "".join(name.split())}
# norm_b = {"".join(name.split()) for name in names_b if "".join(name.split())}

# common = norm_a & norm_b
# only_a = norm_a - norm_b
# only_b = norm_b - norm_a

# sort_common = sorted(common)
# sort_only_a = sorted(only_a)
# sort_only_b = sorted(only_b)

# search = input("検索したい名前を入力してください(空白で終了)：").strip()
# if not search:
#     print("空白のため終了します。")
# elif search in norm_a and search in norm_b:
#     print(f"{search}はA・Bどちらのクラスにも存在します。")
# elif search in norm_a:
#     print(f"{search}はクラスAに存在します。")
# elif search in norm_b:
#     print(f"{search}はクラスBに存在します。")
# else:
#     print(f"{search}という名前は存在しません。")

# print(f"各クラスで共通した名前は{sort_common}です。")
# print(f"1つ目のクラスにだけ存在する名前は{sort_only_a}です。")
# print(f"2つ目のクラスにだけ存在する名前は{sort_only_b}です。")

# ========== Pythonコード（Chat GPT） ==========

names_a = ["田中", "山田", "鈴木", "鈴木"]
names_b = ["東風平", "恵比寿", "御手洗", "田中"]

norm_a = {"".join(name.split()) for name in names_a if "".join(name.split())}
norm_b = {"".join(name.split()) for name in names_b if "".join(name.split())}

common = norm_a & norm_b
only_a = norm_a - norm_b
only_b = norm_b - norm_a

sort_common = sorted(common)
sort_only_a = sorted(only_a)
sort_only_b = sorted(only_b)

search = input("検索したい名前を入力してください(空白で終了)：")
searched = "".join(search.split())
if searched == "":
    print("空白のため終了します。")
else:
    in_a = (searched in norm_a)
    in_b = (searched in norm_b)
    if in_a or in_b:
        print(f"Aにいる：{'はい' if in_a else 'いいえ'} / Bにいる：{'はい' if in_b else 'いいえ'}")
    else:
        print(f"{searched}という名前は存在しません。")

print(f"各クラスで共通した名前は{sort_common}です。")
print(f"1つ目のクラスにだけ存在する名前は{sort_only_a}です。")
print(f"2つ目のクラスにだけ存在する名前は{sort_only_b}です。")

# ========== 修正・改善点 ==========

# ========== 総括 ==========