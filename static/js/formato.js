document.addEventListener("DOMContentLoaded", function () {
  const montoInput = document.getElementById("monto");
  if (!montoInput) return;

  montoInput.addEventListener("input", function () {
    let valor = this.value.replace(/\D/g, "");
    if (valor === "") {
      this.value = "";
      return;
    }

    valor = parseInt(valor).toLocaleString("es-CL");
    this.value = "$" + valor;
  });

  montoInput.addEventListener("blur", function () {
    if (!this.value.startsWith("$")) {
      this.value = "$" + this.value;
    }
  });
});
