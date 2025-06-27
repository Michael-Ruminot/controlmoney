function editarMovimientoModal(id, descripcion, monto, tipo, categoria, anio, mes) {
  const modal = new bootstrap.Modal(document.getElementById("modalEditar"));
  const form = document.getElementById("formEditar");

  form.action = "/editar/" + id;
  form.querySelector("[name='descripcion']").value = descripcion;
  form.querySelector("[name='monto']").value = "$" + parseInt(monto).toLocaleString("es-CL");
  form.querySelector("[name='tipo']").value = tipo;
  form.querySelector("[name='categoria']").value = categoria;
  form.querySelector("[name='anio_movimiento']").value = anio;
  form.querySelector("[name='mes_movimiento']").value = mes;

  modal.show();
}
