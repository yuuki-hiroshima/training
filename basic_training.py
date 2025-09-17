
# ---------- 練習用 ----------

# ---------- whileループ ----------

# count = 0           # 変数 count を 0 にする。ここから数えるためのスタート地点。
# while count < 3:    # while文（～の間ずっと）。count が 3 より小さい間、この中の処理を繰り返す。
#     print("Hello")  # 画面に「Hello」と表示する。
#     count += 1      # count に1を足す。（0→1→2→3となる）countが3になると while の条件が False になりループが止まる。

# ---------- whileループ（カウントを可視化） ----------

# count = 0           # 変数 count を 0 にする。ここから数えるためのスタート地点。
# while count < 5:    # while文（～の間ずっと）。count が 5 より小さい間、この中の処理を繰り返す。
#     print("Hello")  # 画面に「Hello」と表示する。
#     count += 2      # count に2を足す。（0→2→4→6となる）countが5を超えると while の条件が False になりループが止まる。

# 1回目: count=0 → Hello → count=2
# 2回目: count=2 → Hello → count=4
# 3回目: count=4 → Hello → count=6（終了）

# ---------- forループ ----------

# for i in range(1, 6):   # (1, 6)なら1〜5まで表示される。
#     print(i)            # forループで range の引数だけ値を表示する。

# ---------- forループ＋enumerate関数 ----------

# fruits = ["apple", "banana", "cherry"]  # リストを変数に格納
# for index, fruit in enumerate(fruits):  # enumerate は引数の（番号, 値）をセットで取り出す。そのため index, fruit の2つの変数が必要
#     print(index, fruit)                 # 結果を出力。 index, fruit は forループの中だけの変数

# ---------- forループでリストを回す ----------

# リストの要素を1つずつ取り出すときは for文 を使う。
# ポイント：リストの要素を「変数」に代入して1つずつ処理できる。

# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# ---------- forループでリストを回す(rangeと組み合わせる) ----------

# インデックス（番号）が必要なときは range(len(list)) を使う方法がある。

# fruits = ["apple", "banana", "cherry"]

# for i in range(len(fruits)):
#     print(i, fruits[i])

# ---------- forループでリストを回す(enumerateと組み合わせる) ----------

# もっと簡単に「番号 + 値」を取り出す方法が enumerate。
# 実務ではこちらのほうがよく使われる。

# fruits = ["apple", "banana", "cherry"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# ---------- forループでリストを回す（条件分岐と組み合わせ） ----------

# リストを回しながら、条件を付けて処理することもできる。
# 以下は、リストから偶数だけを取り出す。

# numbers = [1, 2, 3, 4, 5]

# for n in numbers:
#     if n % 2 == 0:
#         print(n)

# ----------  ----------

# ========== プログラムの要件（目的） ==========

# ========== 完成形のイメージ（オリジナル） ==========

# ========== 完成形のイメージ（Chat GPT） ==========

# ========== 擬似コード（オリジナル） ==========

# ========== 擬似コード（Chat GPT） ==========

# ========== Pythonコード（オリジナル） ==========

# ========== Pythonコード（Chat GPT） ==========

# ========== 修正・改善点 ==========

# ========== 総括 ==========