from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    try:
        income = float(request.form['income'])
        rent = float(request.form['rent'])
        food = float(request.form['food'])
        transport = float(request.form['transport'])
        entertainment = float(request.form['entertainment'])
        others = float(request.form['others'])

        expenses = {
            'Rent': rent,
            'Food': food,
            'Transport': transport,
            'Entertainment': entertainment,
            'Others': others
        }

        total_expense = sum(expenses.values())
        savings = income - total_expense
        summary = {}

        for category, amount in expenses.items():
            summary[category] = {
                'amount': amount,
                'percent': round((amount / income) * 100, 2)
            }

        suggestion = "✅ Good job on your savings!" if savings >= income * 0.1 else "⚠️ Try to cut down your expenses by at least 10%."

        return render_template("result.html", income=income, expenses=summary,
                               total_expense=total_expense, savings=savings,
                               suggestion=suggestion)

    except ValueError:
        return "❌ Please enter valid numeric inputs."

if __name__ == '__main__':
    app.run(debug=True)
