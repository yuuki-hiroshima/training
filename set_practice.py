
names = ["田中", "山口", "伊藤", "鈴木", "山田", "田中"]
names_b = {"鈴木", "木本", "山下", "津田", "加藤", "渋谷", "木本"}

unique_names = set(names)                              # names のみリストなので、セットに変換

unique_names.add("山下")                                # add では1件しか追加できない
unique_names.update({"瀬戸", "塚本", "木本", "上田"})     # update なら1件〜複数件を1度に追加できる

unique_names.discard("山口")                            # discard では1件しか削除できない
unique_names.difference_update({"伊藤", "鈴木", "塚本"})  # deifferece_update なら1件〜複数件を1度に削除できる
# unique_names -= {"伊藤", "鈴木", "塚本"}                # difference_updateと同じことができ、短く書ける

common = names_b & unique_names                         # 共通している名前
Either = names_b | unique_names                         # A+B全体（重複する名前は削除）
only_names = unique_names - names_b                     # unique_names にだけいる名前
only_b = names_b - unique_names                         # names_b にだけいる名前
taeget_difference = names_b ^ unique_names              # 片方にしかいない名前（Either - common）


names.sort()                                           # リストを並び替える場合（あいうえお順）
sort_names = sorted(names)                             # 上記と同じくリストの並び替えができる（あいうえお順）
sort_unique_names = sorted(unique_names)               # セットに並び順の概念はないが、表示順の固定はできる。

print(f"リストB: {names_b}")
print(f"リスト: {names}")
print(f"セット: {unique_names}")
print(f"ソート: {sort_names}")
print(f"ソート: {sort_unique_names}")

print(f"共通: {common}")
print(f"どちらかにはいる: {Either}")
print(f"namesだけにいる: {only_names}")
print(f"name_bだけにいる: {only_b}")
print(f"どちらかにしかいない: {taeget_difference}")