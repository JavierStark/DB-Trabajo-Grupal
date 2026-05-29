#!/usr/bin/env python3
"""Genera la memoria del proyecto PAU en PDF usando weasyprint."""

import weasyprint

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
@page {
  size: A4;
  margin: 1.6cm 1.6cm 1.8cm 1.6cm;
  @bottom-center {
    content: counter(page);
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    color: #888;
  }
}
@page :first {
  @bottom-center { content: none; }
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 9pt;
  line-height: 1.35;
  color: #1a1a2e;
}

/* ========== COVER PAGE ========== */
.cover {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  page-break-after: always;
  background: linear-gradient(135deg, #0f0c29 0%, #1a1a4e 40%, #24243e 100%);
  color: white;
  text-align: center;
  padding: 1.5cm;
  margin: -1.6cm -1.6cm;
  width: 21cm;
  height: 29.7cm;
}
.cover .shield {
  font-size: 48pt;
  margin-bottom: 20px;
  opacity: 0.9;
}
.cover h1 {
  font-size: 22pt;
  font-weight: 800;
  letter-spacing: 1px;
  margin-bottom: 6px;
  color: #e0e0ff;
}
.cover h2 {
  font-size: 12pt;
  font-weight: 400;
  color: #aaaaff;
  margin-bottom: 20px;
}
.cover .divider {
  width: 60px; height: 2px;
  background: #6c63ff;
  margin: 12px auto;
  border-radius: 2px;
}
.cover .info {
  margin-top: 25px;
  font-size: 9pt;
  color: #ccccee;
  line-height: 1.6;
}
.cover .info strong { color: #ffffff; }
.cover .badge {
  display: inline-block;
  margin-top: 25px;
  padding: 8px 20px;
  border: 1px solid #6c63ff;
  border-radius: 25px;
  font-size: 9pt;
  color: #aaaaff;
  letter-spacing: 2px;
}

/* ========== TABLE OF CONTENTS ========== */
.toc {
  page-break-after: always;
}
.toc h2 {
  font-size: 14pt;
  color: #1a1a4e;
  margin-bottom: 15px;
  padding-bottom: 4px;
  border-bottom: 2px solid #6c63ff;
}
.toc ul {
  list-style: none;
  padding: 0;
}
.toc li {
  padding: 3px 0;
  border-bottom: 1px dotted #ddd;
  font-size: 9pt;
}
.toc li span.num {
  display: inline-block;
  width: 30px;
  font-weight: 700;
  color: #6c63ff;
}
.toc li span.dots {
  float: right;
  color: #aaa;
}

/* ========== HEADINGS ========== */
h1 { font-size: 15pt; color: #1a1a4e; margin-top: 18px; margin-bottom: 8px; padding-bottom: 4px; border-bottom: 2px solid #6c63ff; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 11.5pt; color: #2d2d6b; margin-top: 14px; margin-bottom: 6px; }
h3 { font-size: 10.5pt; color: #3d3d7b; margin-top: 10px; margin-bottom: 5px; }
h4 { font-size: 10pt; color: #4d4d8b; margin-top: 8px; margin-bottom: 4px; }

p { margin-bottom: 6px; text-align: justify; }

/* ========== TABLES ========== */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 8px 0;
  font-size: 8pt;
}
table th {
  background: #1a1a4e;
  color: white;
  padding: 4px 6px;
  text-align: left;
  font-weight: 600;
}
table td {
  padding: 3px 6px;
  border-bottom: 1px solid #e0e0e0;
}
table tr:nth-child(even) td {
  background: #f8f8ff;
}

/* ========== CODE BLOCKS ========== */
pre {
  background: #1e1e2e;
  color: #cdd6f4;
  padding: 6px 8px;
  border-radius: 4px;
  font-family: 'DejaVu Sans Mono', monospace;
  font-size: 6.5pt;
  line-height: 1.25;
  overflow-x: auto;
  margin: 6px 0;
  white-space: pre-wrap;
}
code {
  font-family: 'DejaVu Sans Mono', monospace;
  font-size: 8pt;
  background: #f0f0ff;
  padding: 1px 3px;
  border-radius: 2px;
  color: #2d2d6b;
}
pre code {
  background: transparent;
  padding: 0;
  color: inherit;
  font-size: inherit;
}

/* ========== CALLOUTS ========== */
.callout {
  padding: 5px 8px;
  margin: 6px 0;
  border-left: 3px solid #6c63ff;
  background: #f0eeff;
  border-radius: 0 4px 4px 0;
  font-size: 8pt;
}
.callout.info { border-left-color: #3b82f6; background: #eff6ff; }
.callout.warn { border-left-color: #f59e0b; background: #fffbeb; }
.callout.done { border-left-color: #10b981; background: #ecfdf5; }
.callout.err { border-left-color: #ef4444; background: #fef2f2; }

/* ========== MISC ========== */
.subtitle {
  font-size: 9pt;
  color: #666;
  margin-bottom: 10px;
}
.section-desc {
  font-size: 8.5pt;
  color: #555;
  margin-bottom: 6px;
  font-style: italic;
}
.strong { font-weight: 700; }
.tag {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 8pt;
  font-weight: 600;
}
.tag.sql { background: #e8f5e9; color: #2e7d32; }
.tag.plsql { background: #e3f2fd; color: #1565c0; }
.tag.sec { background: #fce4ec; color: #c62828; }
.tag.bug { background: #fff3e0; color: #e65100; }

ul, ol { margin: 4px 0 4px 20px; }
li { margin-bottom: 2px; }

.page-break { page-break-before: always; }

/* ========== TOC IN PAGE ========== */
.section-toc { margin: 15px 0; }
.section-toc li { font-size: 10pt; }

.cover-logo { font-size: 60px; margin-bottom: 10px; }

.object-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 10px 0;
}
.object-item {
  background: #f0eeff;
  border: 1px solid #d0cee8;
  border-radius: 6px;
  padding: 6px 12px;
  font-size: 9pt;
  color: #2d2d6b;
}
.object-item code { background: transparent; padding: 0; font-size: 9pt; }
</style>
</head>
<body>

<!-- ========== COVER ========== -->
<div class="cover">
  <div class="cover-logo">&#x1F393;</div>
  <h1>Gestión de PAU<br>con Oracle Database</h1>
  <h2>Memoria Técnica del Proyecto</h2>
  <div class="divider"></div>
  <div class="info">
    <strong>Bases de Datos II</strong><br>
    ETSI Informática — Universidad de Málaga<br>
    Curso 2025–2026<br><br>
    <strong>Autores:</strong> José Antonio Cañete López, Javier Torralbo Cortés, Fernando Jerez Martín, Sergio Delgado Cobos<br>
    <strong>Repositorio:</strong> github.com/SergioDelgadoCobos/DB-Trabajo-Grupal<br>
    <strong>Script principal:</strong> <code>Entrega_Final.sql</code> (1244 líneas)
  </div>
  <div class="badge">PL/SQL &bull; ORACLE 18c &bull; SEGURIDAD</div>
</div>

<!-- ========== TOC ========== -->
<div class="toc">
  <h2>Índice</h2>
  <ul>
    <li><span class="num">1</span> Introducción</li>
    <li><span class="num">2</span> Esquema Físico</li>
    <li><span class="num">3</span> Modelo Relacional</li>
    <li><span class="num">4</span> Carga de Datos</li>
    <li><span class="num">5</span> Procedimientos y Paquetes</li>
    <li><span class="num">6</span> Optimización: Índices, MV, Sinónimos</li>
    <li><span class="num">7</span> Triggers (Disparadores)</li>
    <li><span class="num">8</span> Seguridad Multicapa</li>
    <li><span class="num">9</span> Pruebas y Verificación</li>
    <li><span class="num">10</span> Decisiones Técnicas y Trade-offs</li>
    <li><span class="num">11</span> Conclusiones</li>
  </ul>
</div>

<!-- ========== 1. INTRODUCTION ========== -->
<h1>1. Introducción</h1>

<p class="section-desc">Contexto, objetivos y estructura del proyecto.</p>

<p>Sistema en <strong>Oracle Database 18c</strong> para la gestión logística de las <strong>PAU</strong>: esquema relacional, lógica de negocio PL/SQL, y seguridad multicapa.</p>

<h2>1.1 Objetivos</h2>
<ul>
  <li>Gestionar estudiantes, sedes, aulas, centros y tribunales (vocales).</li>
  <li>Asignación automática centros → sedes (algoritmo greedy).</li>
  <li>Control de aforo, ocupación y vigilancia.</li>
  <li>Seguridad con VPD, roles dinámicos y auditoría.</li>
  <li>Reubicación de última hora (procedimiento <em>DESPISTE</em>).</li>
</ul>

<h2>1.2 Estructura del Proyecto</h2>
<p>El proyecto consta de los siguientes scripts y documentos:</p>
<table>
  <tr><th>Script</th><th>Descripción</th></tr>
  <tr><td><code>Entrega_Final.sql</code></td><td>Script principal (1244 L). Tablespaces, tablas, FKs, external table, vistas, 6 procedimientos, 3 paquetes, 4 triggers, índices, MV, sinónimos, roles, VPD, auditoría, CHECK constraints</td></tr>
  <tr><td><code>Limpieza_Total.sql</code></td><td>Limpieza completa del entorno. Ejecutado como SYS: elimina política de auditoría, usuarios dinámicos, roles, sinónimos, directorio, usuario PAU en CASCADE y tablespaces con sus datafiles</td></tr>
  <tr><td><code>Pruebas_Completas.sql</code></td><td>Suite de 20+ tests funcionales que verifican todos los objetos, procedimientos, paquetes, triggers y políticas de seguridad</td></tr>
</table>

<h2>1.3 Script de Limpieza Total</h2>
<p>El script <code>Limpieza_Total.sql</code> (133 líneas) permite eliminar por completo el entorno creado, dejando la base de datos en el estado anterior a la ejecución. Debe ejecutarse como usuario <strong>SYS</strong>. Realiza las siguientes operaciones en orden:</p>
<ul>
  <li>Desactiva y elimina la política de auditoría unificada (<code>audit_asistencia_updates</code>).</li>
  <li>Elimina todos los usuarios dinámicos creados por <code>PK_SEGURIDAD_PAU</code> (patrón <code>EST_%</code> y <code>VOC_%</code>) con <code>CASCADE</code>.</li>
  <li>Borra los roles (<code>ROL_ESTUDIANTE</code>, <code>ROL_VOCAL</code>, <code>ROL_ACCESO</code>).</li>
  <li>Elimina el sinónimo público (<code>S_ESTUDIANTES</code>) y el directorio (<code>directorio_ext</code>).</li>
  <li>Borra el usuario <code>PAU</code> con <code>CASCADE</code>, eliminando todos sus objetos del esquema.</li>
  <li>Elimina los tablespaces <code>TS_PAU</code> y <code>TS_INDICES</code> incluyendo sus archivos de datos (<code>INCLUDING DATAFILES</code>).</li>
</ul>
<div class="callout warn">
<strong>Nota:</strong> Este script es destructivo e irreversible. Su propósito es permitir una re-ejecución limpia del script principal para pruebas o nueva implantación.
</div>




<!-- ========== 2. SCHEMA ========== -->
<h1>2. Esquema Físico</h1>

<p class="section-desc">Tablespaces, usuario, privilegios y estructura de almacenamiento.</p>

<h2>2.1 Tablespaces</h2>
<p>Se crean dos tablespaces para separar datos de índices, mejorando el rendimiento de E/S y facilitando el mantenimiento:</p>

<pre>CREATE TABLESPACE TS_PAU DATAFILE 'ts_pau.dbf' SIZE 100M AUTOEXTEND ON;
CREATE TABLESPACE TS_INDICES DATAFILE 'ts_indices.dbf' SIZE 50M;</pre>

<div class="callout info">
<strong>Decisión técnica:</strong> Separar datos (TS_PAU) e índices (TS_INDICES) es una práctica recomendada en Oracle para entornos de producción. Permite distribuir la carga de E/S y realizar operaciones de mantenimiento de forma independiente.
</div>

<h2>2.2 Usuario PAU</h2>
<p>El usuario propietario del esquema se crea con privilegios mínimos necesarios, evitando <code>GRANT DBA</code>:</p>

<pre>CREATE USER PAU IDENTIFIED BY pau
  DEFAULT TABLESPACE TS_PAU
  QUOTA UNLIMITED ON TS_PAU
  QUOTA UNLIMITED ON TS_INDICES;

GRANT CONNECT, RESOURCE TO PAU;
GRANT CREATE VIEW, CREATE MATERIALIZED VIEW, CREATE PROCEDURE,
      CREATE SEQUENCE, CREATE TRIGGER, CREATE SYNONYM,
      CREATE PUBLIC SYNONYM TO PAU;
GRANT AUDIT_VIEWER TO PAU;
GRANT EXECUTE ON SYS.DBMS_RANDOM TO PAU;
GRANT EXECUTE ON SYS.DBMS_RLS TO PAU;
GRANT CREATE USER TO PAU;</pre>

<h2>2.3 Directorio para Tabla Externa</h2>
<p>Se define un directorio Oracle para la lectura del archivo CSV:</p>
<pre>CREATE OR REPLACE DIRECTORY directorio_ext AS 'C:\\app\\alumnos\\admin\\orcl\\dpdump';
GRANT READ, WRITE ON DIRECTORY directorio_ext TO PAU;</pre>




<!-- ========== 3. RELATIONAL MODEL ========== -->
<h1>3. Modelo Relacional</h1>

<p class="section-desc">13 tablas, 14 claves foráneas, restricciones CHECK y decisiones de diseño.</p>

<h2>3.1 Tablas del Sistema</h2>
<p>El modelo relacional consta de 10 tablas principales más 3 tablas auxiliares:</p>

<table>
  <tr><th>Tabla</th><th>PK</th><th>Propósito</th></tr>
  <tr><td><code>VOCAL</code></td><td>DNI</td><td>Miembros del tribunal examinador</td></tr>
  <tr><td><code>MATERIA</code></td><td>Codigo</td><td>Materias evaluables</td></tr>
  <tr><td><code>SEDE</code></td><td>Codigo</td><td>Sedes donde se realizan los exámenes</td></tr>
  <tr><td><code>CENTRO</code></td><td>Codigo</td><td>Centros educativos de procedencia</td></tr>
  <tr><td><code>AULA</code></td><td>Codigo</td><td>Aulas dentro de las sedes</td></tr>
  <tr><td><code>ESTUDIANTE</code></td><td>DNI</td><td>Alumnos matriculados</td></tr>
  <tr><td><code>ANE</code></td><td>DNI</td><td>Alumnos con necesidades especiales (AEN)</td></tr>
  <tr><td><code>EXAMEN</code></td><td>FechayHora</td><td>Sesiones de examen</td></tr>
  <tr><td><code>EXAMEN_MATERIA</code></td><td>(FechayHora, Materia)</td><td>Materias por examen (N:M)</td></tr>
  <tr><td><code>EXAMEN_VOCAL_Vigilantes</code></td><td>(FechayHora, Vocal)</td><td>Vocales vigilantes (N:M)</td></tr>
  <tr><td><code>ESTUDIANTE_MATERIA</code></td><td>(DNI, Materia)</td><td>Matrícula alumno-materia (N:M)</td></tr>
  <tr><td><code>ASISTENCIA</code></td><td>(Fecha, DNI, Materia)</td><td>Registro de asistencia a exámenes</td></tr>
  <tr><td><code>LOG_ASISTENCIA</code></td><td>—</td><td>Auditoría de cambios en ASISTENCIA (punto extra)</td></tr>
</table>

<h2>3.2 Claves Foráneas</h2>
<p>Se definen 14 restricciones de integridad referencial que conectan todas las tablas del modelo. Cada FK incluye nombre descriptivo. Las relaciones clave son: ASISTENCIA → ESTUDIANTE/EXAMEN/MATERIA, AULA → SEDE, CENTRO → SEDE, ESTUDIANTE → CENTRO, ESTUDIANTE_MATERIA → ESTUDIANTE/MATERIA, EXAMEN → AULA/VOCAL, EXAMEN_MATERIA → EXAMEN/MATERIA, EXAMEN_VOCAL_Vigilantes → EXAMEN/VOCAL, SEDE → VOCAL (x2), VOCAL → MATERIA, ANE → ESTUDIANTE.</p>

<h2>3.3 Restricciones CHECK</h2>
<p>Se implementan restricciones semánticas y de formato para garantizar la calidad de los datos:</p>

<table>
  <tr><th>Restricción</th><th>Tabla</th><th>Validación</th></tr>
  <tr><td><code>CHK_ESTUDIANTE_DNI_FORMAT</code></td><td>ESTUDIANTE</td><td>Formato 8 dígitos + letra mayúscula (NOVALIDATE)</td></tr>
  <tr><td><code>CHK_VOCAL_DNI_FORMAT</code></td><td>VOCAL</td><td>Formato 8 dígitos + letra mayúscula (NOVALIDATE)</td></tr>
  <tr><td><code>CHK_AULA_CAPACIDAD</code></td><td>AULA</td><td>Capacidad &gt; 0</td></tr>
  <tr><td><code>CHK_AULA_CAP_EXAMEN</code></td><td>AULA</td><td>Capacidad_Examen &gt; 0 AND ≤ Capacidad</td></tr>
  <tr><td><code>CHK_EXAMEN_NUM_EST</code></td><td>EXAMEN</td><td>Num_Estudiantes_Presentes ≥ 0</td></tr>
  <tr><td><code>CHK_ASISTENCIA_ASISTE_VALUES</code></td><td>ASISTENCIA</td><td>Asiste IN ('S','N')</td></tr>
  <tr><td><code>CHK_ASISTENCIA_ENTREGA_VALUES</code></td><td>ASISTENCIA</td><td>Entrega IN ('S','N')</td></tr>
</table>

<div class="callout warn">
<strong>NOVALIDATE:</strong> Las restricciones de formato DNI usan <code>NOVALIDATE</code> para no rechazar los datos ya importados que no cumplan el patrón. Solo los nuevos inserts quedan sujetos a validación.
</div>

<h2>3.4 Diseño de la PK de EXAMEN</h2>
<p>La tabla <code>EXAMEN</code> tiene como clave primaria únicamente <code>FechayHora</code>. Esto es una <strong>decisión de diseño conocida</strong> que implica una limitación: no pueden existir dos exámenes simultáneos en distintas aulas. La alternativa (PK compuesta con <code>Aula_Codigo</code>) requeriría modificar en cascada todas las FKs y tablas relacionadas. Bajo la premisa del proyecto —un único examen por franja horaria— esta decisión es funcionalmente aceptable.</p>


<!-- ========== 4. DATA LOADING ========== -->
<h1>4. Carga de Datos</h1>

<p class="section-desc">Tabla externa, vista de transformación e importación de datos.</p>

<h2>4.1 Tabla Externa y Vista de Transformación</h2>
<p>Los datos de estudiantes se cargan mediante una <strong>tabla externa</strong> que lee un CSV con Oracle Loader (formato <code>;|-separated</code>, UTF-8). La vista <code>V_ESTUDIANTES</code> transforma los datos planos en un modelo relacional, generando automáticamente el correo electrónico combinando inicial + apellido1 + 3 dígitos del DNI.</p>

<h2>4.3 Población de Tablas</h2>
<p>Los datos se importan en tres fases:</p>
<ol>
  <li><strong>Datos maestros</strong> — VOCAL, MATERIA, SEDE se importan manualmente desde archivos XLSX/CSV mediante SQL Developer.</li>
  <li><strong>Centros y estudiantes</strong> — Se insertan desde <code>V_ESTUDIANTES</code> con <code>INSERT INTO ... SELECT</code>, resolviendo la FK Centro mediante JOIN por nombre.</li>
  <li><strong>Matriculación</strong> — El procedimiento <code>PR_MATRICULA_ESTUDIANTES</code> recorre todos los estudiantes y para cada uno procesa sus materias (campo <code>detalle_materias</code> con formato separado por comas).</li>
</ol>


<!-- ========== 5. PROCEDURES & PACKAGES ========== -->
<h1>5. Procedimientos y Paquetes</h1>

<p class="section-desc">Lógica de negocio implementada en PL/SQL.</p>

<h2>5.1 Procedimientos</h2>
<table>
  <tr><th>Procedimiento</th><th>Función</th></tr>
  <tr><td><code>PR_INSERTA_MATERIAS</code></td><td>Parsea materias separadas por comas y matricula al estudiante. Ignora no encontradas/duplicadas</td></tr>
  <tr><td><code>PR_MATRICULA_ESTUDIANTES</code></td><td>Itera todos los estudiantes llamando a PR_INSERTA_MATERIAS</td></tr>
  <tr><td><code>PR_RELLENA_AULAS(N, CAP)</code></td><td>Genera N aulas/sede; Capacidad_Examen = CAP/2</td></tr>
  <tr><td><code>PR_BORRA_AULA_SEDE</code></td><td>Elimina aulas de una sede</td></tr>
  <tr><td><code>PR_BORRA_AULAS</code></td><td>Borra aulas de todas las sedes (usa PR_BORRA_AULA_SEDE)</td></tr>
  <tr><td><code>PR_BORRA_AULA</code></td><td>Borra aula individual (requisito rúbrica)</td></tr>
</table>

<h2>5.2 Paquete PK_ASIGNA — Algoritmo Greedy</h2>
<p>Implementa la asignación automática de centros a sedes. <code>F_PLAZAS(PSEDE)</code> calcula plazas libres como Capacidad_Examen total menos estudiantes asignados. <code>PR_ASIGNA_SEDE</code> opera en dos fases: (1) auto-asigna institutos con nombre coincidente a su sede homónima; (2) para centros restantes, asigna a la sede con más plazas libres. Si no hay espacio, lanza excepción con ROLLBACK.</p>

<h2>5.3 Paquete PK_OCUPACION — Control de Aforo</h2>
<p>Contiene 5 funciones para verificar la correcta ocupación de aulas y asignación de vigilantes:</p>

<table>
  <tr><th>Función</th><th>Retorno</th><th>Propósito</th></tr>
  <tr><td><code>OCUPACION_MAXIMA(p_sede, p_aula)</code></td><td>NUMBER</td><td>Máximo número de personas (estudiantes + vocales) en un aula para una sede dada.</td></tr>
  <tr><td><code>OCUPACION_OK</code></td><td>BOOLEAN</td><td>Verifica que ningún examen futuro exceda la capacidad del aula.</td></tr>
  <tr><td><code>VOCAL_DUPLICADO(p_dni)</code></td><td>BOOLEAN</td><td>Comprueba si un vocal está asignado a dos aulas distintas en el mismo horario.</td></tr>
  <tr><td><code>VOCALES_DUPLICADOS</code></td><td>BOOLEAN</td><td>Versión global: detecta si <em>algún</em> vocal está duplicado en el mismo horario.</td></tr>
  <tr><td><code>VOCAL_RATIO(p_ratio)</code></td><td>BOOLEAN</td><td>Verifica que el ratio estudiantes/vigilantes no exceda el límite especificado.</td></tr>
</table>

<h2>5.4 Procedimientos Avanzados</h2>

<h3>DESPISTE — Reubicación de Última Hora</h3>
<p>Permite reubicar a un estudiante despistado que acudió a sede incorrecta. Opera en una <strong>ventana de 1 hora</strong>. Reubica el primer examen y busca aulas libres para los siguientes exámenes del día en la sede destino.</p>

<h3>MIGRAR_CENTRO — Migración de Centro</h3>
<p>Reasigna todos los estudiantes de un centro a una nueva sede. Busca aulas con capacidad disponible en la sede destino. Disparado automáticamente por <code>TR_MIGRAR_CENTRO</code> al actualizar <code>Sede_Codigo</code> en CENTRO.</p>




<!-- ========== 6. OPTIMIZATION ========== -->
<h1>6. Optimización</h1>

<p class="section-desc">Índices, vista materializada, sinónimos y secuencias.</p>

<h2>6.1 Índices</h2>
<p>Todos los índices residen en el tablespace <code>TS_INDICES</code>. Se implementan cuatro tipos diferentes:</p>

<table>
  <tr><th>Índice</th><th>Tipo</th><th>Tabla</th><th>Propósito</th></tr>
  <tr><td><code>IDX_ESTUDIANTE_APELLIDOS_UP</code></td><td>Function-based (UPPER)</td><td>ESTUDIANTE</td><td>Búsquedas insensibles a mayúsculas por apellidos</td></tr>
  <tr><td><code>IDX_ESTUDIANTE_CORREO</code></td><td>B-tree</td><td>ESTUDIANTE</td><td>Búsqueda rápida por correo electrónico</td></tr>
  <tr><td><code>IDX_ESTUDIANTE_CENTRO_BM</code></td><td>BITMAP</td><td>ESTUDIANTE</td><td>Agregaciones por centro (baja cardinalidad)</td></tr>
  <tr><td><code>IDX_ASISTENCIA_EST</code></td><td>B-tree</td><td>ASISTENCIA</td><td>Búsquedas por estudiante en asistencia</td></tr>
  <tr><td><code>IDX_ASISTENCIA_EXAMEN</code></td><td>B-tree</td><td>ASISTENCIA</td><td>Búsquedas por examen en asistencia</td></tr>
</table>

<div class="callout info">
<strong>Decisión técnica:</strong> El índice BITMAP es apropiado para <code>Centro_Codigo</code> porque tiene baja cardinalidad (pocos centros, muchos estudiantes por centro). Los índices function-based con UPPER permiten búsquedas eficientes sin preocuparse por mayúsculas/minúsculas.
</div>

<h2>6.2 Vista Materializada</h2>
<p><code>VM_ESTUDIANTES</code> almacena estudiantes + nombre del centro con refresco diario automático (<code>REFRESH FORCE ON DEMAND START WITH TRUNC(SYSDATE+1)</code>). Sinónimo público <code>S_ESTUDIANTES</code> para acceso cross-schema.</p>

<h2>6.3 Secuencia para Centros</h2>
<p><code>SEQ_CENTROS</code> + trigger <code>tr_centros</code> auto-asignan código secuencial a nuevos centros cuando no se proporciona.</p>


<!-- ========== 7. TRIGGERS ========== -->
<h1>7. Triggers (Disparadores)</h1>

<p class="section-desc">Cuatro triggers que implementan reglas de negocio y auditoría.</p>

<table>
  <tr><th>Trigger</th><th>Evento</th><th>Propósito</th></tr>
  <tr><td><code>TR_AUDIT_ASISTENCIA</code></td><td>AFTER I/U/D ON ASISTENCIA</td><td>Audita cambios en LOG_ASISTENCIA (punto extra)</td></tr>
  <tr><td><code>tr_centros</code></td><td>BEFORE INSERT ON CENTRO</td><td>Auto-asigna código secuencial</td></tr>
  <tr><td><code>TR_BORRA_AULA</code></td><td>BEFORE DELETE ON AULA</td><td>Bloquea borrado si hay exámenes &lt;48h; limpia en cascada</td></tr>
  <tr><td><code>TR_MIGRAR_CENTRO</code></td><td>AFTER UPDATE Sede_Codigo ON CENTRO</td><td>Dispara MIGRAR_CENTRO automáticamente</td></tr>
</table>

<h2>7.1 TR_BORRA_AULA — Protección de 48h</h2>
<p>Impide borrar aulas con exámenes en las últimas 48h (pasados o futuros). Si procede, limpia en cascada ASISTENCIA, EXAMEN_MATERIA, EXAMEN_VOCAL_Vigilantes y EXAMEN antes de permitir la eliminación.</p>


<!-- ========== 8. SECURITY ========== -->
<h1>8. Seguridad Multicapa</h1>

<p class="section-desc">Tres capas de seguridad: roles, VPD, usuarios dinámicos, auditoría y política de contraseñas.</p>

<h2>8.1 Roles y Privilegios</h2>
<p>Se definen tres roles con privilegios específicos siguiendo el principio de mínimo privilegio:</p>

<table>
  <tr><th>Rol</th><th>Privilegios principales</th></tr>
  <tr><td><code>ROL_ESTUDIANTE</code></td><td>SELECT en V_MI_ASIGNACION, V_MIS_DATOS, V_OCUPACION_ASIGNADA</td></tr>
  <tr><td><code>ROL_VOCAL</code></td><td>SELECT/UPDATE(cols) en EXAMEN, ASISTENCIA; vistas vigilancia y sede</td></tr>
  <tr><td><code>ROL_ACCESO</code></td><td>SELECT V_ASIGNACION_GLOBAL + ocupación, EXECUTE PK_ASIGNA</td></tr>
</table>

<h2>8.2 Vistas de Seguridad por Perfil</h2>
<p>Cinco vistas filtran los datos según el usuario conectado, utilizando la columna <code>Usuario_BD</code>:</p>

<table>
  <tr><th>Vista</th><th>Filtro</th><th>Perfil</th></tr>
  <tr><td><code>V_MI_ASIGNACION</code></td><td><code>Usuario_BD = USER</code></td><td>Estudiante</td></tr>
  <tr><td><code>V_MIS_DATOS</code></td><td><code>Usuario_BD = USER</code></td><td>Estudiante</td></tr>
  <tr><td><code>V_MI_VIGILANCIA</code></td><td><code>v.Usuario_BD = USER</code></td><td>Vocal</td></tr>
  <tr><td><code>V_MI_SEDE_GESTION</code></td><td><code>v.Usuario_BD = USER</code></td><td>Vocal responsable</td></tr>
  <tr><td><code>V_ASIGNACION_GLOBAL</code></td><td>Sin filtro</td><td>Rol ACCESO</td></tr>
</table>

<h2>8.3 Virtual Private Database (VPD)</h2>
<p>Política de seguridad a nivel de fila sobre <code>ESTUDIANTE</code> que añade automáticamente <code>Usuario_BD = USER</code> a toda consulta. Incluye excepción para el usuario PAU (propietario) que ve todo sin filtro:</p>

<pre>FUNCTION FN_ESTUDIANTE_VPD(p_schema, p_object) RETURN VARCHAR2 AS
BEGIN
  IF SYS_CONTEXT('USERENV', 'SESSION_USER') = 'PAU' THEN RETURN NULL; END IF;
  RETURN 'Usuario_BD = USER';
END;
/
DBMS_RLS.ADD_POLICY(object_schema=>'PAU', object_name=>'ESTUDIANTE',
  policy_name=>'POL_ESTUDIANTE_VPD', function_schema=>'PAU',
  policy_function=>'FN_ESTUDIANTE_VPD');</pre>

<h2>8.4 Paquete PK_SEGURIDAD_PAU — Usuarios Dinámicos</h2>
<p>Genera cuentas Oracle para cada persona: <code>EST_&lt;DNI&gt;</code> (estudiantes) y <code>VOC_&lt;DNI&gt;</code> (vocales). Usa <code>DBMS_RANDOM.STRING('X', 10)</code> para contraseñas aleatorias de 10 caracteres. Asigna automáticamente el rol correspondiente y actualiza <code>Usuario_BD</code> en la tabla.</p>

<h2>8.5 Política de Contraseñas</h2>
<p>Se refuerza el perfil DEFAULT de Oracle con los siguientes parámetros:</p>

<table>
  <tr><th>Parámetro</th><th>Valor</th><th>Efecto</th></tr>
  <tr><td><code>FAILED_LOGIN_ATTEMPTS</code></td><td>5</td><td>Bloqueo tras 5 intentos fallidos</td></tr>
  <tr><td><code>PASSWORD_LIFE_TIME</code></td><td>30</td><td>Contraseña caduca a los 30 días</td></tr>
  <tr><td><code>PASSWORD_GRACE_TIME</code></td><td>5</td><td>Periodo de gracia de 5 días tras caducidad</td></tr>
  <tr><td><code>PASSWORD_LOCK_TIME</code></td><td>1</td><td>Desbloqueo automático tras 1 día</td></tr>
</table>

<h2>8.6 Auditoría Unificada (Oracle 18c)</h2>
<p>Política de auditoría que registra todo UPDATE sobre ASISTENCIA:</p>
<pre>CREATE AUDIT POLICY audit_asistencia_updates ACTIONS UPDATE ON PAU.ASISTENCIA;
AUDIT POLICY audit_asistencia_updates;</pre>


<!-- ========== 9. TESTS ========== -->
<h1>9. Pruebas y Verificación</h1>

<p class="section-desc">Suite de tests funcionales y verificación multi-modelo de IA contra la rúbrica.</p>

<h2>9.1 Pruebas_Completas.sql (20+ tests)</h2>
<p>El script de pruebas cubre todos los aspectos funcionales del sistema:</p>

<table>
  <tr><th>#</th><th>Prueba</th><th>Qué verifica</th></tr>
  <tr><td>1–3</td><td>Estructura</td><td>Tablas, datos importados, índices en TS_INDICES</td></tr>
  <tr><td>4–5</td><td>Aulas</td><td>PR_RELLENA_AULAS, PR_BORRA_AULA_SEDE, PR_BORRA_AULAS</td></tr>
  <tr><td>6–6.5</td><td>Asignación</td><td>PK_ASIGNA.PR_ASIGNA_SEDE, F_PLAZAS</td></tr>
  <tr><td>7–11</td><td>Exámenes</td><td>Inserción EXAMEN/ASISTENCIA, verificación de datos</td></tr>
  <tr><td>12</td><td>Auditoría</td><td>LOG_ASISTENCIA y trigger</td></tr>
  <tr><td>13–14</td><td>Ocupación</td><td>Vistas de ocupación + PK_OCUPACION completo</td></tr>
  <tr><td>15–16</td><td>Seguridad</td><td>PK_SEGURIDAD_PAU, vistas V_MI_*</td></tr>
  <tr><td>17–20</td><td>Triggers/Constraints</td><td>TR_BORRA_AULA, CHECK, MV, FKs, triggers</td></tr>
  <tr><td>21–22</td><td>Avanzado</td><td>VPD/Auditoría, MIGRAR_CENTRO/DESPISTE</td></tr>
</table>

<h2>9.2 Verificación Cruzada con Modelos de IA</h2>
<p>Se realizó una validación independiente del script <code>Entrega_Final.sql</code> contra la rúbrica oficial utilizando <strong>tres modelos de IA</strong> para detectar posibles errores y falsos positivos:</p>

<table>
  <tr><th>Modelo</th><th>Hallazgos</th><th>Falsos positivos</th><th>Errores reales</th></tr>
  <tr><td><code>nemotron-3-super-free</code></td><td>0</td><td>—</td><td>—</td></tr>
  <tr><td><code>qwen3.6-plus-free</code></td><td>9 (3 críticos + 3 moderados + 3 menores)</td><td>7</td><td>2</td></tr>
  <tr><td><code>deepseek-v4-flash-free</code></td><td>6 advertencias</td><td>4</td><td>2</td></tr>
</table>

<p>De los hallazgos totales, solo <strong>2 errores reales</strong> fueron confirmados y corregidos:</p>
<ul>
  <li><strong>OCUPACION_MAXIMA</strong> — No filtraba por aula específica. Corregido en 3 funciones del paquete PK_OCUPACION añadiendo <code>AND Aula_Codigo = p_aula</code>.</li>
  <li><strong>COMMIT en trigger</strong> (ORA-04092) — MIGRAR_CENTRO contenía COMMIT/ROLLBACK que fallaban desde TR_MIGRAR_CENTRO. Corregido eliminando el control de transacción interno.</li>
</ul>
<p>El resto de hallazgos fueron <strong>falsos positivos</strong> o decisiones de diseño deliberadas (PK de EXAMEN no compuesta, permisos sobre V_MI_SEDE_GESTION, etc.). Todos los requisitos de la rúbrica están implementados correctamente.</p>





<!-- ========== 10. DECISIONS ========== -->
<h1>10. Decisiones Técnicas y Trade-offs</h1>

<p class="section-desc">Análisis de las decisiones clave tomadas durante el desarrollo.</p>

<h2>10.1 Principio de Mínimo Privilegio</h2>
<p>Se evitó <code>GRANT DBA</code>, concediendo solo privilegios necesarios (<code>CREATE VIEW</code>, <code>CREATE PROCEDURE</code>, etc.).</p>

<h2>10.2 Tablespaces Separados</h2>
<p>TS_PAU (datos) y TS_INDICES (índices) para rendimiento, mantenimiento aislado y gestión de espacio independiente.</p>

<h2>10.3 Algoritmo Greedy</h2>
<p>Asignación en dos fases: emparejamiento por nombre (institutos) + asignación a sede con más plazas. No óptimo global pero eficiente para el volumen esperado (~50 centros).</p>

<h2>10.4 VPD + Vistas de Seguridad</h2>
<p>Implementación redundante: VPD como capa obligatoria a nivel fila + vistas como capa de presentación por perfil.</p>

<h2>10.5 NOVALIDATE en DNI</h2>
<p>CHECK con NOVALIDATE para no rechazar datos importados pre-existentes. Solo nuevos inserts se validan.</p>

<h2>10.6 Limitación: PK de EXAMEN</h2>
<p>PK solo <code>FechayHora</code> (no compuesta con Aula_Codigo). Cambio requeriría modificar 7 tablas con FKs. Aceptable bajo premisa de un único examen por franja horaria.</p>


<!-- ========== 11. CONCLUSIONS ========== -->
<h1>11. Conclusiones</h1>

<p>El proyecto ha logrado implementar un sistema completo de gestión de PAU sobre Oracle Database 18c que cumple con todos los requisitos especificados en la rúbrica. Los aspectos más destacados son:</p>

<h2>11.1 Resumen de Logros</h2>
<ul>
  <li><strong>Esquema relacional:</strong> 13 tablas, 14 FKs, 8 CHECK, tabla externa, MV, sinónimos.</li>
  <li><strong>Lógica PL/SQL:</strong> 6 procedimientos, 3 paquetes (11 funciones), 4 triggers.</li>
  <li><strong>Seguridad multicapa:</strong> VPD + roles + usuarios dinámicos + auditoría unificada + política contraseñas.</li>
  <li><strong>Verificación:</strong> 20+ tests funcionales que cubren todos los objetos y casos de uso.</li>
</ul>



<h2>11.2 Trabajo Futuro</h2>
<ul>
  <li>Rediseñar PK de EXAMEN como compuesta (FechayHora, Aula_Codigo).</li>
  <li>Triggers INSTEAD OF para V_MI_SEDE_GESTION (vistas JOIN).</li>
  <li>APIs REST con ORDS para separar lógica BD de interfaz de usuario.</li>
</ul>

<p style="text-align: center; margin-top: 40px; color: #888; font-style: italic;">
  29 de mayo de 2026.
</p>

</body>
</html>
"""

if __name__ == '__main__':
    output_path = '/home/javierstark/Desktop/TempTarea/BD/GrupalGit/Memoria_PAU_Grupal.pdf'
    print(f"Generando PDF...")
    doc = weasyprint.HTML(string=HTML_CONTENT)
    doc.write_pdf(output_path)
    print(f"PDF generado: {output_path}")
