function confirmarEliminacion(id) {
  const inputId = document.getElementById("eliminar-id");
  const modal = new bootstrap.Modal(document.getElementById("modalEliminar"));
  inputId.value = id;
  modal.show();
}
