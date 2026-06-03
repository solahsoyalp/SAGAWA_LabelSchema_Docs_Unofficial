# コントリビューションガイド

本リポジトリへの修正・追加提案を歓迎します。Issue / Pull Request にてお寄せください。

## 重要：ドキュメントは自動生成です

`docs/*.md`・`samples/*.csv`・`samples/sjis/*.csv` の **レイアウト系ファイルは
`spec/*.json` から自動生成** されています。これらを直接編集しても、次回ビルドで
上書きされます。**修正は必ず `spec/*.json`（Single Source of Truth）に対して** 行ってください。

```
spec/*.json  ──(tools/build.py)──▶  docs/*.md
                                    samples/*.csv
                                    samples/sjis/*.csv
```

## 手順

1. リポジトリをフォーク／クローンします。
2. 該当する `spec/<レイアウト名>.json` を編集します。
   - フィールド: `name`（項目名）, `length`（桁数）, `type`（属性）, `required`（必須か）,
     `desc`（項目説明・コード値）, `codes`（コード値の連想配列／無ければ `null`）
3. 生成物を更新します（依存ライブラリ不要・Python 3 のみ）。
   ```bash
   python3 tools/build.py
   ```
4. ローカルで検証します。
   ```bash
   python3 tools/build.py --check   # spec と生成物の整合
   python3 tools/check.py           # JSON妥当性・全角英数字の混入チェック
   ```
5. 変更内容と **出典**（公式マニュアルの該当箇所・バージョン等）を添えて PR を作成します。

## 補足

- `docs/集配状態コード一覧.md`・`docs/貨物消込集配状態コード.md`・`docs/離島地域.md` は手動編集です
  （`data/離島地域.{csv,json}` は `docs/離島地域.md` から生成されます）。
- 文字は **NFC**・**半角英数字** で統一してください（CI で全角英数字を検出します）。
- 内容は公式情報での裏取りを推奨します。未検証の項目は `desc` にその旨を明記してください。
