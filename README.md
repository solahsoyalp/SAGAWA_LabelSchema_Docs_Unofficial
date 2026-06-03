# Unofficial SAGAWA Label Schema Docs

佐川急便 **e飛伝Ⅲ** で取り扱う各種 CSV データレイアウト・コード一覧を整理した **非公式** リファレンスです。
レイアウト定義を機械可読な JSON（`spec/`）で一元管理し、ドキュメント・サンプル CSV を自動生成しています。

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## ⚠️ 免責事項

- 本リポジトリの内容は **非公式** であり、株式会社佐川急便とは一切関係ありません。
- 「佐川急便」「e飛伝」等の仕様・商標の権利は株式会社佐川急便に帰属します。
- 正式な仕様・データレイアウトは必ず [公式マニュアル](https://e-hiden3.sagawa-exp.co.jp/help_nsx/manual-takuhai.pdf) をご確認ください。
- 内容の正確性は保証できません。ご利用は自己責任でお願いします（サービス種別コード等、一部に未検証の項目があります）。

## ドキュメント

カテゴリ別の索引は **[docs/README.md](docs/README.md)** を参照してください。

| カテゴリ | 資料 |
|----------|------|
| 送り状 | [取込](docs/送り状データ取込レイアウト.md) / [出力](docs/送り状データ出力レイアウト.md) |
| メール便 | [取込](docs/メール便データ取込レイアウト.md) / [出力](docs/メール便データ出力レイアウト.md) |
| 出荷・荷物状況 | [出荷履歴出力](docs/出荷履歴データ出力レイアウト.md) / [荷物状況出力](docs/荷物状況データ出力レイアウト.md) |
| マスタ | [住所録](docs/住所録データ取込レイアウト.md)・[荷姿品名](docs/荷姿・品名データ取込レイアウト.md)・[部署ご担当者](docs/部署ご担当者データ取込レイアウト.md)（各取込／出力） |
| コード一覧 | [集配状態コード一覧](docs/集配状態コード一覧.md) / [貨物消込集配状態コード](docs/貨物消込集配状態コード.md) |
| 地域 | [離島地域](docs/離島地域.md) |
| その他 | [用語集](docs/用語集.md) |

## リポジトリ構成

```
spec/          機械可読なレイアウト定義（JSON）= Single Source of Truth
docs/          人間向けドキュメント（Markdown・自動生成）
samples/       列名のみのサンプルCSV（UTF-8・自動生成）
samples/sjis/  同・Shift_JIS(CP932) 版
data/          構造化データ（離島地域の CSV / JSON）
tools/         生成・検証スクリプト
```

## 機械可読データ（`spec/*.json`）

各レイアウトは `spec/<レイアウト名>.json` として提供しています。プログラムから項目名・桁数・属性・
必須・コード値を直接読み込めます。

```json
{
  "title": "送り状データ取込レイアウト",
  "direction": "import",
  "meta": { "encoding": "Shift_JIS (CP932)", "delimiter": ",", "header": false },
  "fields": [
    { "name": "お届け先コード取得区分", "length": "1", "type": "半角数字",
      "required": false, "codes": { "0": "飛脚宅配便", "1": "サービス共通" } }
  ]
}
```

## サンプルCSV

`samples/` に各レイアウト（取込／出力）の **列名のみ（ヘッダ1行）** の CSV を用意しています。
CSV 作成時の項目順・項目名の雛形としてご利用ください。

- `samples/*.csv` … UTF-8 / 改行 CRLF
- `samples/sjis/*.csv` … Shift_JIS (CP932)。e飛伝Ⅲ取込時はこちらが必要な場合があります。

## 開発（生成・検証）

依存ライブラリ不要。Python 3 のみで動作します。

```bash
python3 tools/build.py          # spec/ から docs・samples・data を生成
python3 tools/build.py --check  # spec と生成物の整合チェック（CI）
python3 tools/check.py          # JSON妥当性・全角英数字の混入チェック（CI）
```

修正は `docs/*.md` ではなく **`spec/*.json` を編集** してください。詳しくは [CONTRIBUTING.md](CONTRIBUTING.md) を参照。

## ライセンス

ドキュメント・データは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)、
スクリプト等を含む詳細は [LICENSE](LICENSE) を参照してください。

## フィードバック

修正提案・追加要望は Issue / Pull Request にてお寄せください。
