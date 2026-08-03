import { useEffect, useMemo, useState } from "react";
import {
  actualizarTransaccion,
  crearTransaccion,
  eliminarTransaccion,
  obtenerTransacciones,
} from "../api/transacciones";

const FORMULARIO_VACIO = {
  codigo: "",
  tipo: "CREDITO",
  monto: "",
  impacto: "",
};

const FORMATO_MONEDA = new Intl.NumberFormat("es-CO", {
  style: "currency",
  currency: "COP",
  minimumFractionDigits: 0,
});

function Transacciones() {
  const [transacciones, setTransacciones] = useState([]);
  const [formulario, setFormulario] = useState(FORMULARIO_VACIO);
  const [editandoId, setEditandoId] = useState(null);
  const [error, setError] = useState("");

  async function cargarTransacciones() {
    try {
      const datos = await obtenerTransacciones();
      setTransacciones(Array.isArray(datos) ? datos : []);
    } catch (errorCarga) {
      console.error(errorCarga);
      setError("No fue posible cargar las transacciones.");
    }
  }

  useEffect(() => {
    cargarTransacciones();
  }, []);

  function manejarCambio(evento) {
    const { name, value } = evento.target;

    setFormulario((formularioAnterior) => ({
      ...formularioAnterior,
      [name]: value,
    }));
  }

  function editar(transaccion) {
    setEditandoId(transaccion.id);

    setFormulario({
      codigo: transaccion.codigo,
      tipo: transaccion.tipo,
      monto: transaccion.monto,
      impacto: transaccion.impacto,
    });

    setError("");
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function cancelarEdicion() {
    setEditandoId(null);
    setFormulario(FORMULARIO_VACIO);
    setError("");
  }

  async function eliminar(id) {
    const confirmar = window.confirm(
      "¿Estás seguro de que deseas eliminar esta transacción?"
    );

    if (!confirmar) {
      return;
    }

    try {
      const respuesta = await eliminarTransaccion(id);

      if (respuesta?.error) {
        setError(respuesta.error);
        return;
      }

      await cargarTransacciones();
    } catch (errorEliminacion) {
      console.error(errorEliminacion);
      setError("No fue posible eliminar la transacción.");
    }
  }

  async function enviarFormulario(evento) {
    evento.preventDefault();
    setError("");

    const datos = {
      codigo: formulario.codigo.trim(),
      tipo: formulario.tipo,
      monto: Number(formulario.monto),
      impacto: Number(formulario.impacto),
    };

    if (!datos.codigo) {
      setError("El código es obligatorio.");
      return;
    }

    if (datos.monto <= 0) {
      setError("El monto debe ser mayor que cero.");
      return;
    }

    try {
      const respuesta = editandoId
        ? await actualizarTransaccion(editandoId, datos)
        : await crearTransaccion(datos);

      if (respuesta?.error) {
        setError(respuesta.error);
        return;
      }

      cancelarEdicion();
      await cargarTransacciones();
    } catch (errorEnvio) {
      console.error(errorEnvio);
      setError("No fue posible guardar la transacción.");
    }
  }

  const totalCreditos = useMemo(() => {
    return transacciones
      .filter((transaccion) => transaccion.tipo === "CREDITO")
      .reduce(
        (acumulado, transaccion) =>
          acumulado + Number(transaccion.monto || 0),
        0
      );
  }, [transacciones]);

  const totalDebitos = useMemo(() => {
    return transacciones
      .filter((transaccion) => transaccion.tipo === "DEBITO")
      .reduce(
        (acumulado, transaccion) =>
          acumulado + Number(transaccion.monto || 0),
        0
      );
  }, [transacciones]);

  const saldoNeto = totalCreditos - totalDebitos;

  return (
    <div className="min-h-screen bg-linear-to-b from-slate-100 to-white px-4 py-10">
      <div className="mx-auto max-w-5xl">
        <header className="flex items-center gap-4">
          <div className="h-14 w-2 rounded-full bg-emerald-600" />

          <div>
            <h1 className="text-3xl font-bold text-slate-900">
              Quantum Core Finance
            </h1>

            <p className="mt-1 text-sm text-slate-600">
              Sistema de gestión financiera desarrollado con React, Flask,
              Prisma, MySQL y Docker.
            </p>
          </div>
        </header>

        <section className="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          <article className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <p className="text-sm font-medium text-slate-500">
              Total de transacciones
            </p>

            <p className="mt-2 text-3xl font-bold text-slate-900">
              {transacciones.length}
            </p>
          </article>

          <article className="rounded-xl border border-emerald-100 bg-emerald-50 p-5 shadow-sm">
            <p className="text-sm font-medium text-emerald-700">
              Total de créditos
            </p>

            <p className="mt-2 text-2xl font-bold text-emerald-800">
              {FORMATO_MONEDA.format(totalCreditos)}
            </p>
          </article>

          <article className="rounded-xl border border-red-100 bg-red-50 p-5 shadow-sm">
            <p className="text-sm font-medium text-red-700">
              Total de débitos
            </p>

            <p className="mt-2 text-2xl font-bold text-red-800">
              {FORMATO_MONEDA.format(totalDebitos)}
            </p>
          </article>

          <article className="rounded-xl border border-blue-100 bg-blue-50 p-5 shadow-sm">
            <p className="text-sm font-medium text-blue-700">Saldo neto</p>

            <p className="mt-2 text-2xl font-bold text-blue-900">
              {FORMATO_MONEDA.format(saldoNeto)}
            </p>
          </article>
        </section>

        <form
          onSubmit={enviarFormulario}
          className="mt-8 grid gap-5 rounded-2xl border border-slate-200 bg-white p-6 shadow-md md:grid-cols-2"
        >
          <div>
            <label
              htmlFor="codigo"
              className="block text-sm font-medium text-slate-800"
            >
              Código
            </label>

            <input
              id="codigo"
              name="codigo"
              value={formulario.codigo}
              onChange={manejarCambio}
              placeholder="T001"
              required
              className="mt-2 w-full rounded-lg border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
            />
          </div>

          <div>
            <label
              htmlFor="tipo"
              className="block text-sm font-medium text-slate-800"
            >
              Tipo
            </label>

            <select
              id="tipo"
              name="tipo"
              value={formulario.tipo}
              onChange={manejarCambio}
              className="mt-2 w-full rounded-lg border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
            >
              <option value="CREDITO">CRÉDITO</option>
              <option value="DEBITO">DÉBITO</option>
              <option value="TRANSFERENCIA">TRANSFERENCIA</option>
            </select>
          </div>

          <div>
            <label
              htmlFor="monto"
              className="block text-sm font-medium text-slate-800"
            >
              Monto
            </label>

            <input
              id="monto"
              name="monto"
              type="number"
              min="0"
              step="0.01"
              value={formulario.monto}
              onChange={manejarCambio}
              placeholder="100000"
              required
              className="mt-2 w-full rounded-lg border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
            />
          </div>

          <div>
            <label
              htmlFor="impacto"
              className="block text-sm font-medium text-slate-800"
            >
              Impacto
            </label>

            <input
              id="impacto"
              name="impacto"
              type="number"
              step="0.01"
              value={formulario.impacto}
              onChange={manejarCambio}
              placeholder="0.12"
              required
              className="mt-2 w-full rounded-lg border border-slate-300 px-3 py-2.5 text-sm text-slate-900 outline-none transition focus:border-emerald-500 focus:ring-2 focus:ring-emerald-100"
            />
          </div>

          {error && (
            <p className="rounded-lg bg-red-50 px-4 py-3 text-sm font-medium text-red-700 md:col-span-2">
              {error}
            </p>
          )}

          <div className="flex flex-wrap gap-3 md:col-span-2">
            <button
              type="submit"
              className="rounded-lg bg-emerald-600 px-5 py-2.5 text-sm font-semibold text-white shadow-sm transition hover:bg-emerald-700"
            >
              {editandoId ? "Guardar cambios" : "Crear transacción"}
            </button>

            {editandoId && (
              <button
                type="button"
                onClick={cancelarEdicion}
                className="rounded-lg bg-slate-100 px-5 py-2.5 text-sm font-semibold text-slate-700 transition hover:bg-slate-200"
              >
                Cancelar edición
              </button>
            )}
          </div>
        </form>

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-md">
          <div className="border-b border-slate-200 px-5 py-4">
            <h2 className="text-lg font-semibold text-slate-900">
              Registro de transacciones
            </h2>

            <p className="mt-1 text-sm text-slate-500">
              Consulta, actualiza o elimina los movimientos registrados.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full min-w-175">
              <thead className="bg-slate-900 text-left text-sm text-white">
                <tr>
                  <th className="px-5 py-3 font-medium">Código</th>
                  <th className="px-5 py-3 font-medium">Tipo</th>
                  <th className="px-5 py-3 font-medium">Monto</th>
                  <th className="px-5 py-3 font-medium">Impacto</th>
                  <th className="px-5 py-3 font-medium">Acciones</th>
                </tr>
              </thead>

              <tbody>
                {transacciones.length === 0 ? (
                  <tr>
                    <td
                      colSpan="5"
                      className="px-5 py-10 text-center text-sm text-slate-500"
                    >
                      No hay transacciones registradas.
                    </td>
                  </tr>
                ) : (
                  transacciones.map((transaccion) => (
                    <tr
                      key={transaccion.id}
                      className="border-t border-slate-100 text-sm text-slate-800 transition hover:bg-slate-50"
                    >
                      <td className="px-5 py-3 font-semibold">
                        {transaccion.codigo}
                      </td>

                      <td className="px-5 py-3">
                        <span
                          className={
                            transaccion.tipo === "CREDITO"
                              ? "rounded-full bg-emerald-100 px-2.5 py-1 text-xs font-semibold text-emerald-700"
                              : transaccion.tipo === "DEBITO"
                                ? "rounded-full bg-red-100 px-2.5 py-1 text-xs font-semibold text-red-700"
                                : "rounded-full bg-blue-100 px-2.5 py-1 text-xs font-semibold text-blue-700"
                          }
                        >
                          {transaccion.tipo}
                        </span>
                      </td>

                      <td className="px-5 py-3 font-semibold">
                        {FORMATO_MONEDA.format(transaccion.monto)}
                      </td>

                      <td className="px-5 py-3">{transaccion.impacto}</td>

                      <td className="px-5 py-3">
                        <button
                          type="button"
                          onClick={() => editar(transaccion)}
                          className="mr-4 font-semibold text-blue-600 transition hover:text-blue-800 hover:underline"
                        >
                          Editar
                        </button>

                        <button
                          type="button"
                          onClick={() => eliminar(transaccion.id)}
                          className="font-semibold text-red-600 transition hover:text-red-800 hover:underline"
                        >
                          Eliminar
                        </button>
                      </td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </section>

        <footer className="mt-10 border-t border-slate-200 py-6 text-center">
          <p className="text-sm font-semibold text-slate-800">
            Quantum Core Finance
          </p>

          <p className="mt-1 text-xs text-slate-500">
            Desarrollado por Heyller De Jesús Galeano Guarín
          </p>

          <p className="text-xs text-slate-500">
            Ingeniería de Sistemas · CEIPA
          </p>
        </footer>
      </div>
    </div>
  );
}

export default Transacciones;