CREATE TYPE ESTADO AS ENUM ('activo', 'inactivo');
CREATE TYPE SEXO AS ENUM ('femenino', 'masculino', 'otros');

CREATE TABLE cursos(
    id SERIAL PRIMARY KEY
    , descripcion VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE docentes(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    estado ESTADO NOT NULL DEFAULT 'activo',
    ci VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE estudiantes
(
    id SERIAL PRIMARY KEY NOT NULL,
    nombres VARCHAR(60) NOT NULL,
    apellidos VARCHAR(60) NOT NULL,
    ci VARCHAR(60) UNIQUE NOT NULL,
    sexo SEXO NOT NULL,
    id_curso integer NOT NULL,
    FOREIGN KEY(id_curso) REFERENCES cursos(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE asignatura(
    id_asignatura SERIAL PRIMARY KEY
    , asignatura VARCHAR(20) UNIQUE NOT NULL
    , estado ESTADO NOT NULL DEFAULT 'activo'
    , id_curso INTEGER NOT NULL
    , id_docente INTEGER NOT NULL
    , FOREIGN KEY(id_curso) REFERENCES cursos(id) ON DELETE RESTRICT ON UPDATE CASCADE
    , FOREIGN KEY(id_docente) REFERENCES docentes(id) ON DELETE RESTRICT ON UPDATE CASCADE
)