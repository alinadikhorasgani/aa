from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ویژگی‌های سلامتی</title>
    <style>
        @font-face {
            font-family: 'BNazanin';
            src: url('https://cdn.fontcdn.ir/Font/Persian/BNazanin/BNazanin.woff2') format('woff2');
            font-weight: normal;
            font-style: normal;
        }
        body {
            font-family: 'BNazanin', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
            direction: rtl;
        }
        .container {
            display: flex;
            width: 600px;
            height: 400px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            overflow: hidden;
        }
        .half {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .positive { background-color: #e8f5e9; }
        .negative { background-color: #ffebee; }
        .word-cloud { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
        .word-cloud div { text-align: center; }
        .word-cloud span {
            padding: 10px;
            border-radius: 50%;
            font-size: 14px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.3s ease, background-color 0.3s ease;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .positive .word-cloud span { background-color: #66bb6a; color: white; }
        .negative .word-cloud span { background-color: #ef5350; color: white; }
        .hidden-text { display: none; margin-top: 10px; font-size: 14px; color: #333; }
        .show-text { display: block; }
        h2 { margin-bottom: 20px; font-size: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="half positive">
            <h2>ویژگی‌های مثبت</h2>
            <div class="word-cloud">
                {% for item in positive_features %}
                <div>
                    <span onclick="revealText(this)">🎁</span>
                    <div class="hidden-text">{{ item }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
        <div class="half negative">
            <h2>ویژگی‌های منفی</h2>
            <div class="word-cloud">
                {% for item in negative_features %}
                <div>
                    <span onclick="explodeBomb(this)">💣</span>
                    <div class="hidden-text">{{ item }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    <script>
        function explodeBomb(element) {
            const hiddenText = element.nextElementSibling;
            if (hiddenText) {
                element.style.display = 'none';
                hiddenText.classList.add('show-text');
            }
        }
        function revealText(element) {
            const hiddenText = element.nextElementSibling;
            if (hiddenText) {
                element.style.display = 'none';
                hiddenText.classList.add('show-text');
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    positive_features = ["قند خون پایین", "کبد سالم", "کلیه سالم"]
    negative_features = [
        "کاهش شنوایی حسی - عصبی", "فشار خون بالا", "چاقی",
        "ادم اندام", "کمر درد", "کاهش شنوایی ناشی از صوت"
    ]
    return render_template_string(TEMPLATE, positive_features=positive_features, negative_features=negative_features)

if __name__ == '__main__':
    app.run(debug=True)
