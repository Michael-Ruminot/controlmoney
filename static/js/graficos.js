document.addEventListener("DOMContentLoaded", function () {
  if (typeof Chart === "undefined") return;

  // Gráfico de barras
  const ctxBarras = document.getElementById("graficoBarras");
  if (ctxBarras) {
    new Chart(ctxBarras, {
      type: "bar",
      data: {
        labels: window.meses,
        datasets: [
          {
            label: "Ingresos",
            backgroundColor: "rgba(75, 192, 192, 0.7)",
            data: window.ingresos,
          },
          {
            label: "Gastos",
            backgroundColor: "rgba(255, 99, 132, 0.7)",
            data: window.gastos.map((g) => -Math.abs(g)),
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "top" },
          title: { display: true, text: "Historial de Ingresos y Gastos (12 meses)" },
        },
        scales: {
          y: {
            ticks: {
              callback: function (value) {
                return "$" + value.toLocaleString("es-CL");
              },
            },
          },
        },
      },
    });
  }

  // Gráfico de torta
  const ctxTorta = document.getElementById("graficoTorta");
  if (ctxTorta) {
    const totalGastos = window.totalesGasto.reduce((a, b) => a + b, 0);
    new Chart(ctxTorta, {
      type: "doughnut",
      data: {
        labels: window.categoriasGasto,
        datasets: [{
          data: window.totalesGasto,
          backgroundColor: [
            "#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff", "#ff9f40", "#00c851"
          ],
        }],
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: "Gastos por Categoría"
          },
          datalabels: {
            formatter: (value, context) => {
              const label = context.chart.data.labels[context.dataIndex];
              const porcentaje = ((value / totalGastos) * 100).toFixed(1);
              return `${label}: ${porcentaje}%`;
            },
            color: "#000",
            font: {
              weight: "bold"
            }
          },
          legend: {
            position: "bottom"
          }
        }
      },
      plugins: [ChartDataLabels]
    });
  }
});
