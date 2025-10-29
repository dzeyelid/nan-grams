# nan-grams
いろんな素材の大さじ、小さじが何グラムかを表示するアプリ

日本の料理でよく使われる調味料や材料について、大さじ（15ml）・小さじ（5ml）のグラム数を表示する静的サイトです。

## 機能

- 📊 大さじ・小さじからグラムへの即時変換
- 🏷️ 素材のタグ付け（液体、粉末、調味料など）
- 📱 Tailwind CSSによるレスポンシブデザイン
- 🚀 Astroによる高速な静的サイト生成

## ローカル環境のセットアップ

### 必要な環境

- Node.js（バージョン18以上）
- npm

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/dzeyelid/nan-grams.git
cd nan-grams

# 依存関係をインストール
npm install
```

### 開発

```bash
# 開発サーバーを起動
npm run dev
# http://localhost:4321/ でサイトが利用可能になります（ポート4321が使用中の場合は別のポートになります）

# 本番用にビルド
npm run build

# 本番ビルドをプレビュー
npm run preview
```

## プロジェクト構成

```
/
├── public/           # 静的アセット（faviconなど）
├── src/
│   ├── data/        # 素材データ
│   ├── layouts/     # Astroレイアウト
│   ├── lib/         # ユーティリティ関数
│   ├── pages/       # Astroページ
│   └── types/       # TypeScript型定義
├── astro.config.mjs # Astro設定
├── tailwind.config.mjs # Tailwind CSS設定
└── package.json
```

## 利用可能なスクリプト

- `npm run dev` - 開発サーバーを起動
- `npm run build` - 本番用にビルド（型チェックを含む）
- `npm run preview` - 本番ビルドをローカルでプレビュー
- `npm run astro` - Astro CLIコマンドを実行

## 今後の予定

完全なプロジェクトロードマップは [docs/plan.md](docs/plan.md) をご覧ください：

- コミュニティによる素材投稿機能
- いいね・報告機能
- Azure Functions + Cosmos DB統合
- Azure OpenAIによるモデレーション
- GitHub Actionsデプロイメントパイプライン

## 技術スタック

- **フレームワーク**: [Astro](https://astro.build/) v5
- **スタイリング**: [Tailwind CSS](https://tailwindcss.com/)
- **言語**: TypeScript（strictモード）
- **デプロイ**: GitHub Pages（予定）

## ライセンス

[LICENSE](LICENSE) ファイルをご覧ください。

