
# ========== 完成形のイメージ ==========

# テーマ：数字入力プログラム（関数化バージョン）
# ポイント1：ユーザー入力部分、判定部分、合計計算部分に分ける
# ポイント2：メインの処理（main関数）でそれらを呼び出す。

# ユーザーが入力した数字の空白を除去し、整数に変換する1つ目の関数を作成。
# 入力された数字を偶数と奇数に判定する2つ目の関数を作成。
# 1から入力された数字の合計数を算出する3つ目の関数を作成。
# main関数をつかって、上記の関数を制御し以下の処理をする。
# whileループをつかって、プログラムを繰り返し使えるようにする。
# 変数(num)に、1つ目の関数を格納する。
# num <= 0で格納した変数が0以下か判定し、0以下なら
#   「入力された数字が0以下のためプログラムを終了します。」と表示。それ以外は1サイクル動かして再び入力へ戻る（＝while継続）
#    break
# 2つ目の関数を実行し、偶数か奇数かを判定する。
# 3つ目の関数を実行し、1からnumまでの合計数を計算し、変数(total)に格納
# 「1からnumまでの合計数はtotalです。」と表示する。

# ========== 擬似コード（自作） ==========

# def get_number(): ユーザーから入力を受けた数字を整数に変換し、空白を除去する1つ目の関数
#   num = .strip(): ユーザーから数字の入力を受ける
#   try:
#       整数に変換
#   except ValueError
#       「数字を入力してください」と表示
#       return

# def check_even_odd(num): 入力された数字を偶数と奇数に判定する2つ目の関数
#   if num % 2 == 0: 入力された数字を2で割った余りから、偶数か奇数かを判定する。
#       「入力した数字は偶数です。」と表示
#   else:
#       「入力した数字は奇数です。」と表示

# def calc_total(num): 1から入力された数字の合計数を算出する3つ目の関数
#   total = 0 計算する合計数の初期の値
#   for i in range(1, num+1) 1から入力された数字までの合計を計算
#       total += i 1度計算するたびに i を追加

# def main(): main関数をつかって作成した3つの関数を制御
#   whileループでプログラムを繰り返し使えるように構成
#       num = get_number() 1つ目の関数で取得して整数化した値を変数に格納
#       if num <= 0: 入力された数字が0以下でないか判定し、0であれば
#           「入力された数字が0以下のため、プログラムを終了します。」と表示
#            break
#       check_even_odd(num) 2つ目の関数で偶数か奇数かを判定し結果を表示
#       total = calc_total(num) 3つ目の関数で1から入力した数字までの合計を計算
#       「1からnumまでの合計は、totalです。」と表示

# ========== 擬似コード（Chat GPT） ==========

# def get_number():
#     # ユーザーから整数が入るまで繰り返して取得し、整数で返す
#     while True:
#         s = ユーザーから入力を受け取り、strip()で前後の空白を除去
#         try:
#             n = int(s)          # 整数に変換を試す
#             return n            # 成功したら返す
#         except ValueError:
#             「整数を入力してください。」と表示して、再入力へ（while 継続）

# def check_even_odd(num):
#     # 偶数/奇数を判定して表示
#     if num % 2 == 0:
#         「{num} は偶数です。」と表示
#     else:
#         「{num} は奇数です。」と表示

# def calc_total(num):
#     # 1 から num までの合計を返す
#     total = 0
#     for i in range(1, num + 1):   # 上端を含める
#         total += i                 # ★ ここは i を足す
#     return total

# def main():
#     # 何度でも使えるよう、全体を while でループ
#     while True:
#         num = get_number()                 # 必ず整数で返ってくる
#         if num <= 0:
#             「数字が0以下のためプログラムを終了します。」と表示
#             break                          # ループ終了
#         check_even_odd(num)                # 偶数/奇数を表示
#         total = calc_total(num)            # 合計を計算
#         「1から{num}までの合計は {total} です。」と表示
#         # ここで while により先頭へ戻り、再入力できる

# ========== Pythonコード ==========

# def get_number():
#     while True:
#         s = input("数字を入力してください：").strip()
#         try:
#             n = int(s)
#             return n
#         except ValueError:
#             print("整数を入力してください。")

# def check_even_add(num):
#     if num % 2 == 0:
#         print(f"{num} は偶数です。")
#     else:
#         print(f"{num} は奇数です。")

# def calc_total(num):
#     total = 0
#     for i in range(1, num+1):
#         total += i
#     return total

# def main():
#     while True:
#         num = get_number()
#         if num <= 0:
#             print("0以下の数字が入力されたので、プログラムを終了します。")
#             break
#         check_even_add(num)
#         total = calc_total(num)
#         print(f"1 から {num} までの合計は {total} です。")

# main()

# # ========== 各コードの解説 ==========

# def get_number():
#     # 関数の定義。整数入力を受け取って返します（不正なら再入力を促します）。
#     while True:
#         # 無限ループで正しい入力が来るまで繰り返します。
#         s = input("数字を入力してください：").strip()
#         # ユーザー入力を受け取り、strip＝「前後の空白を削除」します（例：" 12 "→"12"）。
#         try:
#             # 例外処理の開始。ここで int に変換を試みます。
#             n = int(s)
#             # 文字列 s を整数に変換します（例："10"→10）。成功したら n に入ります。
#             return n
#             # 正しく整数にできたので、その値 n を呼び出し元へ返します。
#         except ValueError:
#             # 数字以外が入力されたとき（例："abc"）にここへ来ます。
#             print("整数を入力してください。")
#             # 再入力を促すメッセージを表示し、while の先頭へ戻ります。

# def check_even_add(num):
#     # （※関数名はタイポ）引数 num が偶数か奇数かを判定して表示します。
#     if num % 2 == 0:
#         # num を 2 で割った余りが 0 なら偶数（例：4 % 2 == 0 → True）。
#         print(f"{num} は偶数です。")
#         # 偶数であることを表示します。
#     else:
#         # 余りが 1 なら奇数（例：5 % 2 == 1 → True）。
#         print(f"{num} は奇数です。")
#         # 奇数であることを表示します。

# def calc_total(num):
#     # 1 から num までの合計を計算して返します。
#     total = 0
#     # 合計の初期値を 0 に設定します。
#     for i in range(1, num+1):
#         # range(1, num+1)＝1～num までを順に取り出します（例：num=3 → 1,2,3）。
#         total += i
#         # total に i を足し込んでいきます（例：0→1→3→6）。
#     return total
#     # 計算し終えた合計を返します。

# def main():
#     # 全体の流れを管理する関数です。繰り返し入力できるようにします。
#     while True:
#         # 繰り返し処理。終了条件に当たるまで続きます。
#         num = get_number()
#         # ユーザーから整数入力を取得します（不正なら関数内で再入力）。
#         if num <= 0:
#             # 0 以下が入力されたら終了条件とします（例：0, -3 など）。
#             print("0以下の数字が入力されたので、プログラムを終了します。")
#             # 終了メッセージを表示します。
#             break
#             # while ループを抜けてプログラムを終えます。
#         check_even_add(num)
#         # 偶数/奇数の判定結果を表示します。
#         total = calc_total(num)
#         # 1 から num までの合計を計算して total に受け取ります。
#         print(f"1 から {num} までの合計は {total} です。")
#         # 合計結果を表示します。ここで while の先頭へ戻り、再入力が可能です。

# main()
# # プログラムの実行開始点。main 関数を呼び出します。

# ========== 修正・改善点 ==========

# 関数 calc_total内のコードを return sum(range(1, num+1))に変更。これにより4行のコードが1行にまとまりレスポンスが上がる。
# main()を 末尾の記述に変更することで、モジュールとして読み込んだときにプログラムが実行されないので実務的
# 変数 s は「string（文字列）」、n は「number」の略としてよく使用されるため。s・n を num にしても動作はする。
# main()に引数が不要なのは、すべての流れを組みた立てる関数だから。（mainの内側でプログラムが進むから）
# get_number()は、ユーザーから値を受け取る関数なので、引数は不要
# check_even_addとcalc_total関数は、判定や計算に使用する数値が外にあるため、引数で渡す必要がある。

def get_number():
    while True:
        s = input("数字を入力してください：").strip()
        try:
            n = int(s)
            return n
        except ValueError:
            print("整数を入力してください。")

def check_even_add(num):
    if num % 2 == 0:
        print(f"{num} は偶数です。")
    else:
        print(f"{num} は奇数です。")

def calc_total(num):
    return sum(range(1, num+1))

def main():
    while True:
        num = get_number()
        if num <= 0:
            print("0以下の数字が入力されたので、プログラムを終了します。")
            break
        check_even_add(num)
        total = calc_total(num)
        print(f"1 から {num} までの合計は {total} です。")

if __name__ == "__main__":
    main()
# この if 文は「このファイルが直接実行されたときだけ main() を動かす」という意味。
# __name__ は Python が自動で設定する特殊変数。ファイルを 直接実行 した場合 → __name__ == "__main__" になる。
# ファイルを モジュールとして import した場合 → __name__ はそのモジュール名になる（例：mymodule）。