# Unofficial SAGAWA Label SchemaDocs

## 概要

このリポジトリは、佐川急便のe飛伝Ⅲで取り扱う各種CSVデータレイアウトやコード一覧を整理し、参照できるようにしたものです。

## 免責事項

- このリポジトリの内容は非公式のものであり、株式会社佐川急便とは一切関係ありません。
- 佐川急便の公式な仕様やデータレイアウトについては、[公式マニュアル](https://e-hiden3.sagawa-exp.co.jp/help_nsx/manual-takuhai.pdf) をご確認ください。
- 本リポジトリの内容の正確性については保証できません。ご利用の際は自己責任でお願いします。

## ファイル一覧

各ファイルの内容は以下の通りです。


- **[送り状データ出力レイアウト](docs/送り状データ出力レイアウト.md)** - 送り状データの出力フォーマット。
- **[送り状データ取込レイアウト](docs/送り状データ取込レイアウト.md)** - 送り状データの取込フォーマット。
- **[メール便データ出力レイアウト](docs/メール便データ出力レイアウト.md)** - メール便データの出力フォーマット。
- **[メール便データ取込レイアウト](docs/メール便データ取込レイアウト.md)** - メール便データの取込フォーマット。
- **[出荷履歴データ出力レイアウト](docs/出荷履歴データ出力レイアウト.md)** - 出荷履歴データの出力フォーマット。
- **[集配状態コード一覧](docs/集配状態コード一覧.md)** - 集配状態を表すコードの一覧。
- **[貨物消込集配状態コード](docs/貨物消込集配状態コード.md)** - 貨物の消込状態に関するコード一覧。
- **[住所録データ出力レイアウト](docs/住所録データ出力レイアウト.md)** - 住所録データの出力フォーマット。
- **[住所録データ取込レイアウト](docs/住所録データ取込レイアウト.md)** - 住所録データの取込フォーマット。
- **[荷物状況データ出力レイアウト](docs/荷物状況データ出力レイアウト.md)** - 荷物の状況を示すデータの出力フォーマット。
- **[荷姿・品名データ出力レイアウト](docs/荷姿・品名データ出力レイアウト.md)** - 荷姿および品名データの出力フォーマット。
- **[荷姿・品名データ取込レイアウト](docs/荷姿・品名データ取込レイアウト.md)** - 荷姿および品名データの取込フォーマット。
- **[部署ご担当者データ出力レイアウト](docs/部署ご担当者データ出力レイアウト.md)** - 部署担当者のデータ出力フォーマット。
- **[部署ご担当者データ取込レイアウト](docs/部署ご担当者データ取込レイアウト.md)** - 部署担当者のデータ取込フォーマット。
- **[離島地域](docs/離島地域.md)** - 佐川急便の離島地域の一覧。※離島地域情報については非公式情報を参照しています。

## 利用方法

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/solahsoyalp/SAGAWA_LabelSchema_Docs_Unofficial.git
   ```
2. `docs` フォルダ内の各ファイルを参照してください。

## 今後の予定

- 仕様変更があった場合の更新

## フィードバック

本リポジトリの内容についてのフィードバックや修正提案は歓迎します。Issue や Pull Request を通じてご連絡ください。

