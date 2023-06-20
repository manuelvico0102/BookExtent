------------------------------------------Creación de tablas------------------------------------------


--Tabla usuario--
CREATE TABLE usuario (
      ID NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
      NOMBRE_USUARIO VARCHAR2(50) NOT NULL,
      PASSWORD_USUARIO VARCHAR(255) NOT NULL,
      imagen_codificada BLOB
);

--Tabla libro--
CREATE TABLE libro (
      ID NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
      titulo VARCHAR2(255) NOT NULL,
      autor VARCHAR(255) NOT NULL,
      descripcion CLOB,
      imagen BLOB
);

--Tabla de secciones--
CREATE TABLE seccion (
  ID NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
  NOMBRE_SECCION VARCHAR(10) NOT NULL check(nombre_seccion IN('Favoritos', 'Siguiendo', 'Finalizado', 'Pendiente'))
);

--Tabla biblioteca-usuario--
CREATE TABLE biblioteca_usuario (
  ID NUMBER GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1) PRIMARY KEY,
  id_usuario NUMBER(11) NOT NULL,
  id_libro NUMBER(11) NOT NULL,
  id_seccion NUMBER(11) NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuario(ID),
  FOREIGN KEY (id_libro) REFERENCES libro(ID),
  FOREIGN KEY (id_seccion) REFERENCES seccion(ID)
);


------------------------------------------Inserción de datos------------------------------------------


--Inserción tabla usuario--
INSERT INTO usuario (NOMBRE_USUARIO, PASSWORD_USUARIO) VALUES ('manuel', '12345');
INSERT INTO usuario (NOMBRE_USUARIO, PASSWORD_USUARIO) VALUES ('luis', '12345');


--Inserción tabla libro--
insert into libro (titulo, autor, descripcion) values('EL ÚLTIMO DESEO','ANDRZEJ SAPKOWSKI',TO_CLOB('El último deseo es el primer libro de la serie de novelas de fantasía The Witcher del autor polaco Andrzej Sapkowski. El libro es una colección de cuentos interconectados que presentan al personaje principal, Geralt de Rivia, un cazador de monstruos conocido como el brujo. A lo largo de las historias, Geralt lucha contra criaturas míticas y se enfrenta a dilemas éticos complejos. También se exploran temas más profundos como el amor, la amistad y la naturaleza humana. El último deseo es el primer libro de la serie de novelas de fantasía The Witcher del autor polaco Andrzej Sapkowski. El libro es una colección de cuentos interconectados que presentan al personaje principal, Geralt de Rivia, un cazador de monstruos conocido como el brujo. A lo largo de las historias, Geralt lucha contra criaturas míticas y se enfrenta a dilemas éticos complejos. También se exploran temas más profundos como el amor, la amistad y la naturaleza humana.'));
insert into libro (titulo, autor, descripcion) values('LA ESPADA DEL DESTINO','ANDRZEJ SAPKOWSKI',TO_CLOB('El libro sigue las aventuras del protagonista Geralt de Rivia, un cazador de monstruos conocido como un witcher. Geralt viaja a través de un mundo medieval de fantasía enfrentándose a peligrosos monstruos, luchando contra reyes y brujos, y en su camino encuentra a varios personajes interesantes y únicos. En La Espada del Destino Geralt es contratado por el rey Foltest para investigar una serie de extrañas muertes en la ciudad de Vizima. Sin embargo, mientras está en su búsqueda, Geralt se encuentra con varios enemigos y amigos, incluyendo a la hechicera Yennefer, la bandida Shani y el trovador Dandelion.'));
insert into libro (titulo, autor, descripcion) values('LA SANGRE DE LOS ELFOS','ANDRZEJ SAPKOWSKI',TO_CLOB('La Sangre de los Elfos es el tercer libro de la saga literaria The Witcher. El libro comienza con Geralt y su compañera la hechicera Yennefer, llevando a la joven Ciri, una princesa con habilidades mágicas, a Kaer Morhen, la fortaleza de los witchers, para entrenarla en el camino de convertirse en cazadora de monstruos. Mientras tanto, las fuerzas políticas y militares del continente se preparan para la guerra mientras los elfos buscan protección en el reino de los humanos.'));
insert into libro (titulo, autor, descripcion) values('TIEMPO DE ODIO','ANDRZEJ SAPKOWSKI',TO_CLOB('Tiempo de odio es el cuarto libro de la saga literaria The Witcher. El libro comienza con Geralt herido y en busca de ayuda después de los eventos de "La Torre Oscura". En su camino, se encuentra con viejos amigos y enemigos, mientras se ve atrapado en la lucha entre las fuerzas políticas y militares del norte y el sur. A lo largo del libro, Geralt se encuentra con personajes interesantes y únicos, como Philippa Eilhart, una hechicera poderosa, y la duquesa Anna Henrietta, mientras lucha por proteger a aquellos que ama y descubrir la verdad detrás de los acontecimientos que tienen lugar.'));
insert into libro (titulo, autor, descripcion) values('BAUTISMO DE FUEGO','ANDRZEJ SAPKOWSKI',TO_CLOB('Bautismo de fuego es el quinto libro de la saga literaria The Witcher. El libro comienza con Geralt y sus compañeros tratando de encontrar a Ciri, quien ha desaparecido mientras huía de los cazadores que la persiguen por sus habilidades mágicas. En su búsqueda, Geralt y sus amigos se ven involucrados en la guerra que se desarrolla entre el norte y el sur, y tienen que luchar por sobrevivir en un mundo cada vez más peligroso y hostil.'));
insert into libro (titulo, autor, descripcion) values('LA TORRE DE LA GOLONDRINA','ANDRZEJ SAPKOWSKI',TO_CLOB('La torre de la golondrina es el sexto libro de la saga literaria The Witcher. El libro comienza con Geralt en busca de Ciri, quien ha desaparecido de nuevo, mientras se ve atrapado en la guerra que se desarrolla entre Nilfgaard y el norte. A lo largo del libro, Geralt se encuentra con personajes interesantes y únicos, como el hechicero Vilgefortz y la guerrera Cahir, mientras se enfrenta a una difícil elección que podría cambiar el curso de la historia. Mientras tanto, Ciri se encuentra en una aventura por su cuenta, viajando por diferentes mundos y encontrando amigos y enemigos a lo largo del camino. Sus aventuras la llevan a descubrir más sobre sus propios poderes y su papel en el mundo.'));
insert into libro (titulo, autor, descripcion) values('LA DAMA DEL LAGO','ANDRZEJ SAPKOWSKI',TO_CLOB('La dama del lago es el séptimo y último libro de la saga literaria The Witcher. El libro comienza con Geralt en un estado de coma después de los eventos en La torre de la golondrina. A lo largo del libro, Geralt es revivido y se encuentra atrapado en una lucha final entre Nilfgaard y el norte, mientras intenta proteger a sus amigos y descubrir la verdad detrás de la desaparición de Ciri. Mientras tanto, Ciri está atrapada en un mundo alternativo y luchando por encontrar una manera de regresar a su hogar y ayudar a Geralt en su lucha. Sus aventuras la llevan a través de mundos extraños y peligrosos, mientras descubre más sobre su propio destino y su papel en el mundo.'));

insert into libro (titulo, autor, descripcion) values('EL CAMINO DE LOS REYES','BRANDON SANDERSON',TO_CLOB('El camino de los reyes es el primer libro de la serie El Archivo de las Tormentas. La historia se desarrolla en un mundo llamado Roshar, donde los humanos han aprendido a sobrevivir en un entorno hostil gracias a la magia y la tecnología. La trama sigue a varios personajes principales, incluyendo a Kaladin, un soldado caído en desgracia que busca redención; Shallan, una joven aristócrata que se convierte en aprendiz de un erudito; y Dalinar, un noble que busca unificar a los reinos dispersos de Roshar. A lo largo del libro, los personajes se enfrentan a desafíos y peligros mientras luchan por sobrevivir y cumplir con sus objetivos. La trama también presenta una compleja mitología y misterios que se desarrollan a lo largo de la serie.'));
insert into libro (titulo, autor, descripcion) values('PALABRAS RADIANTES','BRANDON SANDERSON',TO_CLOB('Palabras radiantes es el segundo libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, quien ha asumido un papel de liderazgo en la lucha contra los enemigos de Roshar; Shallan, quien continúa su entrenamiento como aprendiz de un erudito y enfrenta desafíos personales y profesionales; y Dalinar, quien busca descubrir la verdad detrás de las visiones que lo acosan. El libro presenta una trama intrincada que se desarrolla a través de múltiples puntos de vista, lo que permite una exploración profunda de los personajes y sus motivaciones. Además, la serie continúa explorando la compleja mitología y la magia única de Roshar, incluyendo el uso de gemas y la manipulación de la energía de la tormenta.'));
insert into libro (titulo, autor, descripcion) values('JURAMENTADA','BRANDON SANDERSON',TO_CLOB('Juramentada es el tercer libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, quien lucha contra su propia depresión mientras lidera a un grupo de caballeros radiantes en la lucha contra los enemigos de Roshar; Shallan, quien enfrenta su pasado y descubre nuevos secretos mientras continúa su entrenamiento como erudita; y Dalinar, quien debe enfrentar su propio pasado y sus errores mientras lidera a los ejércitos de Roshar. Juramentada profundiza en la compleja mitología y los personajes de la serie, mientras que presenta una trama intrincada que se desarrolla a través de múltiples puntos de vista. Además, la serie continúa explorando la compleja magia y la tecnología de Roshar, incluyendo el uso de gemas y la manipulación de la energía de la tormenta.'));
insert into libro (titulo, autor, descripcion) values('EL RITMO DE LA GUERRA','BRANDON SANDERSON',TO_CLOB('El ritmo de la guerra es el cuarto libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, Shallan y Dalinar, mientras enfrentan los peligros y desafíos que amenazan a Roshar. En este libro, se revelan secretos importantes de la historia de Roshar y la humanidad debe enfrentar una amenaza aún mayor que nunca antes. La prosa de Sanderson es detallada y evocadora, y la serie presenta escenas de acción emocionantes y espectaculares. Además, El ritmo de la guerra explora aún más la compleja mitología y los personajes de la serie, mientras que aborda temas profundos como la traición, el sacrificio y la lucha por la libertad.'));

--Inserción tabla seccion--
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Favoritos');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Siguiendo');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Finalizado');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Pendiente');

--Inserción tabla biblioteca_usuario--
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '1', '1');
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '2', '1');
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '3', '2');

------------------------------------------Consultas------------------------------------------
--Libros--
SELECT libro.id, libro.titulo, libro.autor
FROM libro;

--Favoritos--Para los demás solo se cambia el nombre de la sección y la ID del usuario
SELECT libro.id, libro.titulo, libro.autor
FROM libro
INNER JOIN biblioteca_usuario ON libro.ID = biblioteca_usuario.id_libro
INNER JOIN seccion ON biblioteca_usuario.id_seccion = seccion.ID
WHERE biblioteca_usuario.id_usuario = 5 AND seccion.NOMBRE_SECCION = 'Favoritos'
ORDER BY libro.id;

SELECT COUNT(*) FROM biblioteca_usuario WHERE id_usuario = '1' AND id_libro = '3' AND id_seccion = '1';

------------------------------------------Comprobación de tablas------------------------------------------
select * from usuario;
select * from libro;
select * from seccion;
select * from biblioteca_usuario;

delete from usuario where NOMBRE_USUARIO='prueba';
update libro set imagen = null where id=11;
------------------------------------------Confirmar cambios------------------------------------------
commit;

------------------------------------------Borrado de tablas------------------------------------------
DROP TABLE BIBLIOTECA_USUARIO;
DROP TABLE LIBRO;
DROP TABLE SECCION;
DROP TABLE USUARIO;