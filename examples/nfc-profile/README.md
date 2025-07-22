# NFCプロフィール機能の使用方法

このディレクトリには、tanzakuテーマのNFCプロフィール機能を使用するためのサンプルファイルが含まれています。

## 📁 ファイル構成

- `profile-sample.md` - プロフィールページのサンプル
- `pelicanconf-sample.py` - Pelican設定ファイルのサンプル
- `README.md` - この説明ファイル

## 🎨 機能概要

NFCプロフィール機能は、以下の要素を含むモダンなプロフィールページを作成できます：

### ✨ デザイン要素
- **プロフィールカード**: 影とグラデーション効果のあるカード型レイアウト
- **アバター画像**: 円形のプロフィール写真表示
- **SNSアイコン**: Simple Iconsを使用した美しいアイコン
- **QRコードエリア**: QRコード表示用の専用セクション

### 📱 レスポンシブ対応
- デスクトップ: 横並びレイアウト
- タブレット: スタック型レイアウト  
- モバイル: 1カラムレイアウト

## 🚀 使用方法

### 1. ファイルの配置
`profile-sample.md` を参考にして、Pelicanの `pages/` ディレクトリにプロフィールページを作成します。

```
blogbody/
├── pages/
│   └── profile.md  # ここにプロフィールページを配置
```

### 2. HTMLの記述
マークダウンファイル内に以下のHTMLクラスを使用してプロフィールセクションを記述します：

```html
<div class="nfc-profile-container">
  <!-- プロフィール内容 -->
</div>
```

### 3. 設定のカスタマイズ
`pelicanconf-sample.py` を参考にして、Pelicanの設定を調整してください。

## 🔧 カスタマイズ

### プロフィール写真の変更
```html
<img src="あなたの写真URL" alt="プロフィール写真" class="avatar-image">
```

### SNSアイコンの追加・変更
Simple Iconsから好きなアイコンを選択できます：
```html
<img src="https://cdn.simpleicons.org/[サービス名]/[カラーコード]" alt="アイコン" class="contact-icon">
```

利用可能なアイコン: [Simple Icons](https://simpleicons.org/)

### QRコードの設定
実際のQRコード画像に置き換えます：
```html
<img src="QRコード画像のURL" alt="QRコード" class="qr-code">
```

## 📄 利用可能なCSSクラス

| クラス名 | 用途 |
|---------|------|
| `nfc-profile-container` | メインコンテナ |
| `profile-header` | ヘッダーセクション |
| `profile-avatar` | アバター画像コンテナ |
| `avatar-image` | プロフィール写真 |
| `profile-basic-info` | 基本情報エリア |
| `profile-name` | 名前 |
| `profile-title` | 肩書き |
| `profile-motto` | モットー・キャッチフレーズ |
| `profile-intro` | 自己紹介セクション |
| `profile-contacts` | 連絡先セクション |
| `contact-grid` | 連絡先グリッド |
| `contact-item` | 個別連絡先項目 |
| `contact-icon` | SNSアイコン |
| `contact-label` | 連絡先ラベル |
| `profile-qr` | QRコードセクション |
| `qr-container` | QRコードコンテナ |
| `qr-code` | QRコード画像 |
| `qr-description` | QRコード説明文 |

## 🎯 使用例

NFCカードやビジネスカードに印刷するQRコードから、このプロフィールページにリンクすることで、美しい自己紹介ページを提供できます。

## 📝 ライセンス

この機能はtanzakuテーマに含まれており、同じライセンス条件で利用できます。