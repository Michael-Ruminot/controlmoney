document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.querySelector("form");
  if (!formulario) return;

  formulario.addEventListener("submit", function (e) {
    const descripcion = formulario.querySelector("[name='descripcion']").value.trim();
    const monto = formulario.querySelector("[name='monto']").value.trim();
    const tipo = formulario.querySelector("[name='tipo']").value;
    const categoria = formulario.querySelector("[name='categoria']").value;
    const mes = formulario.querySelector("[name='mes_movimiento']").value;
    const anio = formulario.querySelector("[name='anio_movimiento']").value;

    if (!descripcion || !monto || !tipo || !categoria || !mes || !anio) {
      e.preventDefault();
      alert("Por favor, completa todos los campos.");
    }
  });
});
