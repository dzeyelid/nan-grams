# ML per 100g Extraction Script

このディレクトリには、日本食品標準成分表（八訂）増補2023年のCSVデータから、100gあたりのml情報を抽出するスクリプトが含まれています。

## スクリプト

### `extract_ml_per_100g.py`

このスクリプトは、「17 調味料及び香辛料類」のCSVファイルから、備考欄に100gあたりのmlが記載されている項目を抽出します。

#### 使い方

```bash
python3 scripts/extract_ml_per_100g.py
```

#### 入力

- `references/20230428-mxt_kagsei-mext_00001_012(17調味料及び香辛料類).csv`

#### 出力

- `data/ml_per_100g.json` - 抽出されたデータをJSON形式で保存

## 出力データの構造

出力されるJSONファイルは以下の構造を持ちます：

```json
{
  "source": "日本食品標準成分表（八訂）増補2023年 - 17 調味料及び香辛料類",
  "description": "備考欄に100gあたりのmlが記載されている項目",
  "count": 45,
  "items": [
    {
      "food_name": "＜調味料類＞　（ウスターソース類）　ウスターソース",
      "ml_per_100g": 83.7
    },
    ...
  ]
}
```

## プログラマブルアクセス

JSONファイルは、以下のようにプログラムから簡単にアクセスできます：

```python
import json

# ファイルを読み込む
with open('data/ml_per_100g.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# すべての項目を取得
for item in data['items']:
    print(f"{item['food_name']}: {item['ml_per_100g']} ml")

# 特定の食品を検索
search_term = "しょうゆ"
matching_items = [item for item in data['items'] 
                  if search_term in item['food_name']]

# 特定の食品のml値を取得
target_food = "＜調味料類＞　（しょうゆ類）　こいくちしょうゆ"
ml_value = next((item['ml_per_100g'] for item in data['items'] 
                 if item['food_name'] == target_food), None)
```

## 抽出された項目数

合計45項目の調味料・香辛料の100gあたりのml情報が抽出されています。
