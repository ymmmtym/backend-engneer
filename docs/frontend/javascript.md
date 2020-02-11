# JavaScript
## es6
- アロー関数
- 定数のスコープ
- コンストラクタのoverride
- デフォルトエクスポート、名前付きエクスポート
- forEach,find,filter,mapメソッド

### 変数宣言の種類
javascriptにおける変数宣言の方法は以下の3つ

- var
- let
- const

#### var
```
var hoge_var = 10;
var hoge_var = 100; //再宣言可能
 
hoge_var = 1000; //再代入可能
```

#### let
```
let hoge_let = 20;
let hoge_let = 200; //再宣言できない
 
hoge_let = 2000; //再代入可能
```

#### const
```
const test_const = 30;
const test_const = 300; //再宣言できない
 
test_const = 3000; //再代入できない
```

### スコープ

- グローバル変数
- ローカル変数

#### グローバル変数
グローバル変数はどこからでもアクセスできてしまうので、
他の変数との競合を引き起こしやすい。
その為、エラーになったり想定通りの出力がされない場合がある。

#### ローカル変数
for文や関数の中だけで使う変数
