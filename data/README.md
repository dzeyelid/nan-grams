# 100gあたりのml情報データセット

## 概要

このファイルは、「日本食品標準成分表（八訂）増補2023年」の「17 調味料及び香辛料類」から抽出された、100gあたりのml情報を含むデータセットです。

## データソース

- **出典**: [日本食品標準成分表（八訂）増補2023年](https://www.mext.go.jp/a_menu/syokuhinseibun/mext_00001.html)
- **カテゴリ**: 17 調味料及び香辛料類
- **元ファイル**: `references/20230428-mxt_kagsei-mext_00001_012(17調味料及び香辛料類).csv`

## 抽出条件

備考欄に「100 g： XX.X mL」の形式で記載されている項目を抽出しました。

## 統計

- **合計項目数**: 45項目
- **カテゴリ内訳**:
  - ウスターソース類: 3項目
  - 辛味調味料類: 1項目
  - しょうゆ類: 7項目
  - 食塩類: 4項目
  - 食酢類: 3項目
  - だし類: 2項目
  - 調味ソース類: 8項目
  - トマト加工品類: 3項目
  - ドレッシング類: 2項目
  - みそ類: 8項目
  - その他（調味料類）: 2項目
  - 香辛料類: 1項目
  - その他: 1項目

## ファイル形式

JSON形式で保存されており、以下の構造を持ちます：

```json
{
  "source": "日本食品標準成分表（八訂）増補2023年 - 17 調味料及び香辛料類",
  "description": "備考欄に100gあたりのmlが記載されている項目",
  "count": 45,
  "items": [
    {
      "food_name": "食品名",
      "ml_per_100g": 数値
    }
  ]
}
```

## 使用例

### Python

```python
import json

# データの読み込み
with open('data/ml_per_100g.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 全項目の表示
for item in data['items']:
    print(f"{item['food_name']}: {item['ml_per_100g']} ml")

# 特定の食品の検索
search_term = "しょうゆ"
results = [item for item in data['items'] 
           if search_term in item['food_name']]
```

### JavaScript

```javascript
// データの読み込み
const data = require('./data/ml_per_100g.json');

// 全項目の表示
data.items.forEach(item => {
  console.log(`${item.food_name}: ${item.ml_per_100g} ml`);
});

// 特定の食品の検索
const searchTerm = 'しょうゆ';
const results = data.items.filter(item => 
  item.food_name.includes(searchTerm)
);
```

## 更新方法

データを更新する場合は、以下のコマンドを実行してください：

```bash
python3 scripts/extract_ml_per_100g.py
```

## ライセンス

このデータは「日本食品標準成分表（八訂）増補2023年」に基づいています。元データの利用規約に従ってご利用ください。

## 作成日

2023年（元データ更新日：2023年4月28日）
