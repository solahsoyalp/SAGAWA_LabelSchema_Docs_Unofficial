# 変更履歴

本プロジェクトの主な変更を記録します。形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に準拠します。

## [Unreleased]

### Added
- `spec/*.json` を Single Source of Truth として導入。`docs/*.md`・`samples/*.csv`・`samples/sjis/*.csv` を `tools/build.py` で自動生成する構成に変更。
- 機械可読データ（`spec/*.json`）と Shift_JIS 版サンプル CSV（`samples/sjis/`）を追加。
- 離島地域の構造化データ `data/離島地域.{csv,json}` を追加。
- GitHub Actions による CI（生成物の整合・JSON妥当性・全角英数字検出）を追加。
- `LICENSE`（CC BY 4.0）、`CONTRIBUTING.md`、Issue/PR テンプレート、`CHANGELOG.md`、用語集、`docs/README.md`（索引）、`.editorconfig` を追加。
- 各レイアウトに CSV 仕様（文字コード・区切り文字・ヘッダ有無等）と必須項目（必須列）を明記。

### Changed
- `出荷履歴データ出力レイアウト` に欠落していた公式項目（指定シール・営業所受取・SRC区分・元着区分・削除時間・各不可可能性）を補完し、公式順に整列。
- リポジトリ全体を NFC・半角英数字に正規化。

### Notes
- サービス種別コード（00〜10）は未検証のため、`desc` にその旨を明記しています。
