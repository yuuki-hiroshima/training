
# ========== 完成形のイメージ （オリジナル）==========

# テーマ：身長と体重からBMIを計算する。

# ユーザーに身長と体重を入力してもらう get_Value を作成。
#   変数 h, w に身長と体重を入力してもらう
#   input + strip で空白を除去し変数 h, w に格納。
#   値を float で浮動小数点に変換
#   値が数字でない場合、「数字を入力してください」と表示
#   値が数字でない場合、while と continue を使い再入力
#   return で変数 h, w を返す

# BMIを計算する関数 calc_bmi を作成。
#   引数でheight, weightを取得
#   bmi = weight / (height * height) 体重÷(身長×身長)でBMIを計算
#   return で 変数 bmi を返す

# BMIを判定する関数 judge_bmi を作成
#   引数で bmi_date を取得
#   if 18.5 >= bmi_date <= 25   BMIが18.5未満か判定
#       「あなたのBMI値は低体重です。」と表示
#   elif 18.5 <= bmi_date < 25 BMIが18.5以上〜25未満か判定
#       「あたなのBMI値は普通体重です。」と表示
#   else:                       それ以外の場合
#       「あなたのBMI値は肥満です。」と表示
#   return で結果を返す。

# main関数で全体を制御
#   変数 height, weight に get_Value で取得した数字を格納
#   変数 bmi_date に calc_bmi で取得した値を格納
#   変数 judge_bmi から取得した結果を表示

# ========== 完成形のイメージ （Chat GPT）==========

# 修正ポイント1：1つの関数で「身長と体重を両方返す」よりも、プロンプトを渡して1つの値を返す関数にすると再利用性が高いです。
# 修正ポイント2：BMI の公式は「体重 ÷ (身長(m) × 身長(m))」です。ここで注意：入力は「cm」なので、m に変換する必要あり。
# 修正ポイント3：BMI判定の記述に誤りがある。詳細はNotionに記述
# judge_bmi は文字列を返す関数とし、printはmainで実行すうｒと役割分担が明確になる。

# 1. get_value(prompt)
#    - ユーザーに入力を求める
#    - strip で空白を除去
#    - float に変換（エラーなら再入力を促す）
#    - 数値を返す

# 2. calc_bmi(height, weight)
#    - height(cm) を m に変換
#    - BMI を計算して返す

# 3. judge_bmi(bmi)
#    - BMI の値を条件分岐で判定
#    - 結果の文字列を返す

# 4. main()
#    - get_value で height, weight を取得
#    - calc_bmi で BMI を計算
#    - judge_bmi で判定結果を取得
#    - print で結果を表示

# ========== 擬似コード（オリジナル） ==========

# 1. get_value(prompt) ユーザーの身長と体重を入力してもらい、空白を除去したあと、float型に変換し値を返す関数
#    while True:
#       height = get_value("身長(cm)を入力してください：").strip() 身長を入力してもらい、空白を削除
#       weight = get_value("体重(kg)を入力してください：").strip() 体重を入力してもらう、空白を削除
#       try:
#           height = float(height) float に変換（エラーなら再入力を促す）
#           weight = float(weight) float に変換（エラーなら再入力を促す）
#       except ValueError:
#           「数字を入力してください。」と表示。再入力へ
#            return height, weight

# 2. calc_bmi(height, weight) get_valueで取得した身長の単位をcmからmに変換、身長と体重からBMI値を測定して返す関数
#    height_m = height / 100 身長を100で割、mに変換する
#    bmi = weight / (height_m * height_m) BMI値を計算する
#    return bmi 計算したBMI値を返す

# 3. judge_bmi(bmi) 取得したbmiと値と、BMIの基準値を比較して文字列を返す。
#    if bmi < 18.5: BMI の値を条件分岐で判定
#       result = str("低体重")
#    elif 18.5 <= bmi < 25:
#       result = str("普通体重")
#    elif 18.5 <= bmi < 30:
#       result = str("肥満度1")
#    elif 18.5 <= bmi < 35:
#       result = str("肥満度2")
#    elif 18.5 <= bmi < 40:
#       result = str("肥満度3")
#    else:
#       result = str("肥満度4")
#    return result

# 4. main() それぞれの関数を制御
#    height, weight = get_value(prompt) get_value で height, weight を取得
#    bmi = calc_bmi(height, weight) calc_bmi で BMI を計算
#    result = judge_bmi(bmi) judge_bmi で判定結果を取得
#    print(f"あなたのBMI値は {bmi} で肥満度は {result} です。") print で結果を表示

# ========== 擬似コード（Chat GPT） ==========

# 修正ポイント1： get_value に入力はさせない。入力は main にまかせて空白の除去と float に変換して値を返すだけにするとスッキリする。
# 修正ポイント2： judge_bmi の条件分岐の値が、すべて18.5以上で始まっていて重複していた部分を改修。
# 修正ポイント3： main で身長と体重を入力してもらい、get_value で空白除去と float 変換をする。

# 1. get_value(prompt)
#    while True:
#        s = input(prompt).strip()
#        try:
#            value = float(s)   # float に変換
#            return value       # 数字なら返す
#        except ValueError:
#            「数字を入力してください。」と表示 → 再入力へ

# 2. calc_bmi(height, weight)
#    height_m = height / 100
#    bmi = weight / (height_m * height_m)
#    return bmi

# 3. judge_bmi(bmi)
#    if bmi < 18.5:
#        result = "低体重"
#    elif 18.5 <= bmi < 25:
#        result = "普通体重"
#    elif 25 <= bmi < 30:
#        result = "肥満（1度）"
#    elif 30 <= bmi < 35:
#        result = "肥満（2度）"
#    elif 35 <= bmi < 40:
#        result = "肥満（3度）"
#    else:
#        result = "肥満（4度以上）"
#    return result

# 4. main()
#    height = get_value("身長(cm)を入力してください：")
#    weight = get_value("体重(kg)を入力してください：")
#    bmi = calc_bmi(height, weight)
#    result = judge_bmi(bmi)
#    print(f"あなたのBMI値は {bmi:.1f} で、判定は「{result}」です。")


# ========== Pythonコード ==========

def get_value(prompt):
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)
            return value
        except ValueError:
            print("数字を入力してください。")

def calc_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m * height_m)
    return bmi

def judge_bmi(bmi):
    if bmi < 18.5:
        result = "低体重"
    elif 18.5 <= bmi < 25:
        result = "普通体重"
    elif 25 <= bmi < 30:
        result = "肥満（1度）"
    elif 30 <= bmi < 35:
        result = "肥満（2度）"
    elif 35 <= bmi < 40:
        result = "肥満（3度）"
    else:
        result = "肥満（4度以上）"
    return result

def main():
    while True:
        height = get_value("身長を入力してください(cm)：")
        weight = get_value("体重を入力してください(kg)：")

        if height <= 0 or weight <= 0:
            print("0以下が入力されたので終了します。")
            break

        bmi = calc_bmi(height, weight)
        result = judge_bmi(bmi)
        print("-" * 45)
        print(f"あなたのBMI値は {bmi:.1f} で結果は {result} です。")
        print("-" * 45)

if __name__ == "__main__":
    main()

# ========== 修正・改善点 ==========

# ========== 総括 ==========