## String
```py
# 创建字符串
s1 = "Hello, World!"  # 双引号
s2 = 'Python字符串'      # 单引号
s3 = '''多行字符串\n这是第二行'''
s4 = """也可以用三双引号"""

# 字符串基本属性
length = len(s)  # 长度
first_char = s[0] if s else None  # 第一个字符
last_char = s[-1] if s else None  # 最后一个字符
sliced = s[1:4] if len(s) > 3 else ""  # 切片
reversed_s = s[::-1]  # 反转

# 大小写转换
"lower": s.lower(),
"upper": s.upper(),
"capitalize": s.capitalize(),
"title": s.title(),
"swapcase": s.swapcase()

# 字符串拼接
joined = s1 + ", " + s2  # 加号拼接
joined_with_space = " ".join([s1, s2])  # 使用join

# 字符串分割
split_by_comma = s.split(",")
split_lines = s.splitlines()

# 去除空白
stripped = s.strip()
left_stripped = s.lstrip()
right_stripped = s.rstrip()

# 查找
find_index = s.find(old)  # 查找子字符串

# REPLACE 替换 ｜ 注意：replace会return一个新的string，而不是在原本的string上进行修改
replace_result = s.replace(old, new, count) if count else s.replace(old, new)

# 判断字符串
"startswith_hello": s.startswith("Hello"),
"endswith_txt": s.endswith(".txt"),
"is_alpha": s.isalpha(),
"is_digit": s.isdigit(),
"is_alnum": s.isalnum(),
"is_space": s.isspace()

# 格式化字符串
f_string = f"My name is {name} and I'm {age} years old."
format_method = "My name is {} and I'm {} years old.".format(name, age)

# 填充字符串
zfilled = s.zfill(5)
centered = s.center(10, '*')

# ENCODING/DECODING 编码与解码
encoded = s.encode("utf-8")
decoded = encoded.decode("utf-8")

# SLICING 切片
s = "Python"
print(s[0])    # 输出: 'P' (首字符)
print(s[-1])   # 输出: 'n' (最后一个字符)
print(s[1:4])  # 输出: 'yth' (左闭右开)
print(s[::-1]) # 输出: 'nohtyP' (反转字符串)
r = s[mid:][::-1] # 可以连续切片

# string filtering and transformation using a generator expression
string = "A man, a plan, a canal: Panama!"
filtered = ''.join(c for c in string if c.isalnum()).lower()


```