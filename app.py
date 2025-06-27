from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import calendar

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movimientos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "clave_secreta"
db = SQLAlchemy(app)

@app.template_filter()
def formato_clp(valor):
    try:
        valor = int(valor)
        return f"${valor:,.0f}".replace(",", ".")
    except:
        return valor

class Movimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(10), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        descripcion = request.form["descripcion"]
        monto = int(request.form["monto"].replace(".", "").replace("$", ""))
        tipo = request.form["tipo"]
        categoria = request.form["categoria"]
        mes = int(request.form["mes_movimiento"])
        anio = int(request.form["anio_movimiento"])
        fecha = datetime(anio, mes, 1)

        nuevo = Movimiento(
            descripcion=descripcion,
            monto=monto,
            tipo=tipo,
            categoria=categoria,
            fecha=fecha
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("index", mes=mes, anio=anio))

    mes_filtro = int(request.args.get("mes", datetime.now().month))
    anio_filtro = int(request.args.get("anio", datetime.now().year))

    movimientos = Movimiento.query.filter(
        db.extract("month", Movimiento.fecha) == mes_filtro,
        db.extract("year", Movimiento.fecha) == anio_filtro
    ).order_by(Movimiento.fecha.desc()).all()

    ingresos = sum(m.monto for m in movimientos if m.tipo == "ingreso")
    gastos = sum(m.monto for m in movimientos if m.tipo == "gasto")
    total_general = ingresos - gastos

    # Gráficos históricos
    ingresos_meses = []
    gastos_meses = []
    meses = []

    for i in range(11, -1, -1):
        mes = (datetime.now().month - i - 1) % 12 + 1
        anio = datetime.now().year if datetime.now().month - i > 0 else datetime.now().year - 1
        meses.append(calendar.month_abbr[mes])

        movimientos_mes = Movimiento.query.filter(
            db.extract("month", Movimiento.fecha) == mes,
            db.extract("year", Movimiento.fecha) == anio
        ).all()
        ingresos_meses.append(sum(m.monto for m in movimientos_mes if m.tipo == "ingreso"))
        gastos_meses.append(sum(m.monto for m in movimientos_mes if m.tipo == "gasto"))

    categoriasGasto = []
    totalesGasto = []

    categorias = db.session.query(Movimiento.categoria).distinct().all()
    for c in categorias:
        total_categoria = db.session.query(db.func.sum(Movimiento.monto)).filter(
            Movimiento.categoria == c[0],
            Movimiento.tipo == "gasto",
            db.extract("month", Movimiento.fecha) == mes_filtro,
            db.extract("year", Movimiento.fecha) == anio_filtro
        ).scalar() or 0
        if total_categoria > 0:
            categoriasGasto.append(c[0])
            totalesGasto.append(total_categoria)

    return render_template("index.html",
        movimientos=movimientos,
        ingresos=ingresos,
        gastos=gastos,
        total_general=total_general,
        mes_filtro=mes_filtro,
        anio_filtro=anio_filtro,
        meses=meses,
        ingresos_meses=ingresos_meses,
        gastos_meses=gastos_meses,
        categoriasGasto=categoriasGasto,
        totalesGasto=totalesGasto
    )

@app.route("/eliminar", methods=["POST"])
def eliminar():
    id = request.form["id"]
    mov = Movimiento.query.get(id)
    db.session.delete(mov)
    db.session.commit()
    return redirect(url_for("index", mes=mov.fecha.month, anio=mov.fecha.year))

@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    mov = Movimiento.query.get(id)
    mov.descripcion = request.form["descripcion"]
    mov.monto = int(request.form["monto"].replace(".", "").replace("$", ""))
    mov.tipo = request.form["tipo"]
    mov.categoria = request.form["categoria"]
    mes = int(request.form["mes_movimiento"])
    anio = int(request.form["anio_movimiento"])
    mov.fecha = datetime(anio, mes, 1)

    db.session.commit()
    return redirect(url_for("index", mes=mes, anio=anio))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
