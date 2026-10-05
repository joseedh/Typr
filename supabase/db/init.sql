-- ============================================================
-- 1. TIPOS ENUMERADOS
-- ============================================================

CREATE TYPE tipo_salas AS ENUM (
    'privada',
    'rápida'
);

CREATE TYPE modos AS ENUM (
    'individual',
    'multijugador'
);

CREATE TYPE estado_sala AS ENUM (
    'esperando',
    'en curso',
    'finalizada'
);

CREATE TYPE idiomas_disponibles AS ENUM (
    'esp',
    'eng'
);

CREATE TYPE dificultades AS ENUM (
    'fácil',
    'medio',
    'avanzado',
    'experto'
);


-- ============================================================
-- 2. USUARIO
-- ============================================================

CREATE TABLE usuario (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    nombre VARCHAR(30) NOT NULL UNIQUE,
    correo VARCHAR(254) NOT NULL UNIQUE,
    password CHAR(64) NOT NULL,

    avatar_data BYTEA,
    avatar_mime VARCHAR(50) DEFAULT 'image/jpeg',

    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE
);


-- ============================================================
-- 3. TEXTOS
-- ============================================================

CREATE TABLE textos (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    contenido TEXT NOT NULL,
    idioma idiomas_disponibles NOT NULL,
    dificultad dificultades NOT NULL,

    t_ideal_ms INT,
    record_usr INT,

    CONSTRAINT chk_texto_tiempo_ideal
        CHECK (t_ideal_ms IS NULL OR t_ideal_ms > 0),

    CONSTRAINT fk_texto_record_usuario
        FOREIGN KEY (record_usr)
        REFERENCES usuario(id)
        ON DELETE SET NULL
);


-- ============================================================
-- 4. SALAS
-- ============================================================

CREATE TABLE salas (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    -- Código utilizado por otros usuarios para ingresar.
    codigo VARCHAR(10) NOT NULL UNIQUE,

    anfitrion INT NOT NULL,

    tipo tipo_salas NOT NULL DEFAULT 'privada',

    idioma idiomas_disponibles NOT NULL,
    dificultad dificultades NOT NULL,

    cantidad_rondas INT NOT NULL,
    tiempo_limite_seg INT NOT NULL,

    estado estado_sala NOT NULL DEFAULT 'esperando',

    fecha_creacion TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_sala_cantidad_rondas
        CHECK (cantidad_rondas > 0),

    CONSTRAINT chk_sala_tiempo_limite
        CHECK (tiempo_limite_seg > 0),

    CONSTRAINT fk_sala_anfitrion
        FOREIGN KEY (anfitrion)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 5. MIEMBROS DE LA SALA
-- ============================================================

CREATE TABLE sala_miembro (
    sala INT NOT NULL,
    miembro INT NOT NULL,

    -- Estado utilizado antes de iniciar la carrera.
    listo BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (sala, miembro),

    -- Un usuario solamente puede pertenecer a una sala
    -- simultáneamente.
    CONSTRAINT uq_sala_miembro_usuario
        UNIQUE (miembro),

    CONSTRAINT fk_sala_miembro_sala
        FOREIGN KEY (sala)
        REFERENCES salas(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_sala_miembro_usuario
        FOREIGN KEY (miembro)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);


-- ============================================================
-- 6. PARTIDA
-- ============================================================

CREATE TABLE partida (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    -- NULL para partidas individuales.
    sala INT DEFAULT NULL,

    texto INT NOT NULL,

    modo modos NOT NULL DEFAULT 'individual',

    -- En multijugador identifica la ronda dentro de la sala.
    -- En modo individual puede permanecer NULL.
    numero_ronda INT DEFAULT NULL,

    tiempo_inicio TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tiempo_fin TIMESTAMPTZ DEFAULT NULL,

    CONSTRAINT chk_partida_numero_ronda
        CHECK (numero_ronda IS NULL OR numero_ronda > 0),

    CONSTRAINT chk_partida_tiempos
        CHECK (
            tiempo_fin IS NULL
            OR tiempo_fin >= tiempo_inicio
        ),

    CONSTRAINT fk_partida_sala
        FOREIGN KEY (sala)
        REFERENCES salas(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_partida_texto
        FOREIGN KEY (texto)
        REFERENCES textos(id)
        ON DELETE RESTRICT
);


-- ============================================================
-- 7. PARTICIPACIÓN EN PARTIDA
-- ============================================================

CREATE TABLE participacion_partida (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    partida INT NOT NULL,
    usuario INT NOT NULL,

    tiempo_ms INT DEFAULT NULL,
    ppm INT DEFAULT NULL,

    precision_pct REAL DEFAULT NULL,
    progreso REAL DEFAULT NULL,

    posicion INT DEFAULT NULL,
    puntaje INT DEFAULT NULL,

    -- Un usuario solamente puede participar una vez
    -- en una misma partida.
    CONSTRAINT uq_participacion_partida_usuario
        UNIQUE (partida, usuario),

    CONSTRAINT chk_participacion_tiempo
        CHECK (
            tiempo_ms IS NULL
            OR tiempo_ms >= 0
        ),

    CONSTRAINT chk_participacion_ppm
        CHECK (
            ppm IS NULL
            OR ppm >= 0
        ),

    CONSTRAINT chk_participacion_precision
        CHECK (
            precision_pct IS NULL
            OR (
                precision_pct >= 0
                AND precision_pct <= 100
            )
        ),

    CONSTRAINT chk_participacion_progreso
        CHECK (
            progreso IS NULL
            OR (
                progreso >= 0
                AND progreso <= 100
            )
        ),

    CONSTRAINT chk_participacion_posicion
        CHECK (
            posicion IS NULL
            OR posicion > 0
        ),

    CONSTRAINT chk_participacion_puntaje
        CHECK (
            puntaje IS NULL
            OR puntaje >= 0
        ),

    CONSTRAINT fk_participacion_partida
        FOREIGN KEY (partida)
        REFERENCES partida(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_participacion_usuario
        FOREIGN KEY (usuario)
        REFERENCES usuario(id)
        ON DELETE CASCADE
);
