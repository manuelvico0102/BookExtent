------------------------------------------Creaci�n de tablas------------------------------------------


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


------------------------------------------Inserci�n de datos------------------------------------------


--Inserci�n tabla usuario--
INSERT INTO usuario (NOMBRE_USUARIO, PASSWORD_USUARIO) VALUES ('manuel', '12345');
INSERT INTO usuario (NOMBRE_USUARIO, PASSWORD_USUARIO) VALUES ('luis', '12345');


--Inserci�n tabla libro--
insert into libro (titulo, autor, descripcion) values('EL �LTIMO DESEO','ANDRZEJ SAPKOWSKI',TO_CLOB('El �ltimo deseo es el primer libro de la serie de novelas de fantas�a The Witcher del autor polaco Andrzej Sapkowski. El libro es una colecci�n de cuentos interconectados que presentan al personaje principal, Geralt de Rivia, un cazador de monstruos conocido como el brujo. A lo largo de las historias, Geralt lucha contra criaturas m�ticas y se enfrenta a dilemas �ticos complejos. Tambi�n se exploran temas m�s profundos como el amor, la amistad y la naturaleza humana. El �ltimo deseo es el primer libro de la serie de novelas de fantas�a The Witcher del autor polaco Andrzej Sapkowski. El libro es una colecci�n de cuentos interconectados que presentan al personaje principal, Geralt de Rivia, un cazador de monstruos conocido como el brujo. A lo largo de las historias, Geralt lucha contra criaturas m�ticas y se enfrenta a dilemas �ticos complejos. Tambi�n se exploran temas m�s profundos como el amor, la amistad y la naturaleza humana.'));
insert into libro (titulo, autor, descripcion) values('LA ESPADA DEL DESTINO','ANDRZEJ SAPKOWSKI',TO_CLOB('El libro sigue las aventuras del protagonista Geralt de Rivia, un cazador de monstruos conocido como un witcher. Geralt viaja a trav�s de un mundo medieval de fantas�a enfrent�ndose a peligrosos monstruos, luchando contra reyes y brujos, y en su camino encuentra a varios personajes interesantes y �nicos. En La Espada del Destino Geralt es contratado por el rey Foltest para investigar una serie de extra�as muertes en la ciudad de Vizima. Sin embargo, mientras est� en su b�squeda, Geralt se encuentra con varios enemigos y amigos, incluyendo a la hechicera Yennefer, la bandida Shani y el trovador Dandelion.'));
insert into libro (titulo, autor, descripcion) values('LA SANGRE DE LOS ELFOS','ANDRZEJ SAPKOWSKI',TO_CLOB('La Sangre de los Elfos es el tercer libro de la saga literaria The Witcher. El libro comienza con Geralt y su compa�era la hechicera Yennefer, llevando a la joven Ciri, una princesa con habilidades m�gicas, a Kaer Morhen, la fortaleza de los witchers, para entrenarla en el camino de convertirse en cazadora de monstruos. Mientras tanto, las fuerzas pol�ticas y militares del continente se preparan para la guerra mientras los elfos buscan protecci�n en el reino de los humanos.'));
insert into libro (titulo, autor, descripcion) values('TIEMPO DE ODIO','ANDRZEJ SAPKOWSKI',TO_CLOB('Tiempo de odio es el cuarto libro de la saga literaria The Witcher. El libro comienza con Geralt herido y en busca de ayuda despu�s de los eventos de "La Torre Oscura". En su camino, se encuentra con viejos amigos y enemigos, mientras se ve atrapado en la lucha entre las fuerzas pol�ticas y militares del norte y el sur. A lo largo del libro, Geralt se encuentra con personajes interesantes y �nicos, como Philippa Eilhart, una hechicera poderosa, y la duquesa Anna Henrietta, mientras lucha por proteger a aquellos que ama y descubrir la verdad detr�s de los acontecimientos que tienen lugar.'));
insert into libro (titulo, autor, descripcion) values('BAUTISMO DE FUEGO','ANDRZEJ SAPKOWSKI',TO_CLOB('Bautismo de fuego es el quinto libro de la saga literaria The Witcher. El libro comienza con Geralt y sus compa�eros tratando de encontrar a Ciri, quien ha desaparecido mientras hu�a de los cazadores que la persiguen por sus habilidades m�gicas. En su b�squeda, Geralt y sus amigos se ven involucrados en la guerra que se desarrolla entre el norte y el sur, y tienen que luchar por sobrevivir en un mundo cada vez m�s peligroso y hostil.'));
insert into libro (titulo, autor, descripcion) values('LA TORRE DE LA GOLONDRINA','ANDRZEJ SAPKOWSKI',TO_CLOB('La torre de la golondrina es el sexto libro de la saga literaria The Witcher. El libro comienza con Geralt en busca de Ciri, quien ha desaparecido de nuevo, mientras se ve atrapado en la guerra que se desarrolla entre Nilfgaard y el norte. A lo largo del libro, Geralt se encuentra con personajes interesantes y �nicos, como el hechicero Vilgefortz y la guerrera Cahir, mientras se enfrenta a una dif�cil elecci�n que podr�a cambiar el curso de la historia. Mientras tanto, Ciri se encuentra en una aventura por su cuenta, viajando por diferentes mundos y encontrando amigos y enemigos a lo largo del camino. Sus aventuras la llevan a descubrir m�s sobre sus propios poderes y su papel en el mundo.'));
insert into libro (titulo, autor, descripcion) values('LA DAMA DEL LAGO','ANDRZEJ SAPKOWSKI',TO_CLOB('La dama del lago es el s�ptimo y �ltimo libro de la saga literaria The Witcher. El libro comienza con Geralt en un estado de coma despu�s de los eventos en La torre de la golondrina. A lo largo del libro, Geralt es revivido y se encuentra atrapado en una lucha final entre Nilfgaard y el norte, mientras intenta proteger a sus amigos y descubrir la verdad detr�s de la desaparici�n de Ciri. Mientras tanto, Ciri est� atrapada en un mundo alternativo y luchando por encontrar una manera de regresar a su hogar y ayudar a Geralt en su lucha. Sus aventuras la llevan a trav�s de mundos extra�os y peligrosos, mientras descubre m�s sobre su propio destino y su papel en el mundo.'));

insert into libro (titulo, autor, descripcion) values('EL CAMINO DE LOS REYES','BRANDON SANDERSON',TO_CLOB('El camino de los reyes es el primer libro de la serie El Archivo de las Tormentas. La historia se desarrolla en un mundo llamado Roshar, donde los humanos han aprendido a sobrevivir en un entorno hostil gracias a la magia y la tecnolog�a. La trama sigue a varios personajes principales, incluyendo a Kaladin, un soldado ca�do en desgracia que busca redenci�n; Shallan, una joven arist�crata que se convierte en aprendiz de un erudito; y Dalinar, un noble que busca unificar a los reinos dispersos de Roshar. A lo largo del libro, los personajes se enfrentan a desaf�os y peligros mientras luchan por sobrevivir y cumplir con sus objetivos. La trama tambi�n presenta una compleja mitolog�a y misterios que se desarrollan a lo largo de la serie.'));
insert into libro (titulo, autor, descripcion) values('PALABRAS RADIANTES','BRANDON SANDERSON',TO_CLOB('Palabras radiantes es el segundo libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, quien ha asumido un papel de liderazgo en la lucha contra los enemigos de Roshar; Shallan, quien contin�a su entrenamiento como aprendiz de un erudito y enfrenta desaf�os personales y profesionales; y Dalinar, quien busca descubrir la verdad detr�s de las visiones que lo acosan. El libro presenta una trama intrincada que se desarrolla a trav�s de m�ltiples puntos de vista, lo que permite una exploraci�n profunda de los personajes y sus motivaciones. Adem�s, la serie contin�a explorando la compleja mitolog�a y la magia �nica de Roshar, incluyendo el uso de gemas y la manipulaci�n de la energ�a de la tormenta.'));
insert into libro (titulo, autor, descripcion) values('JURAMENTADA','BRANDON SANDERSON',TO_CLOB('Juramentada es el tercer libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, quien lucha contra su propia depresi�n mientras lidera a un grupo de caballeros radiantes en la lucha contra los enemigos de Roshar; Shallan, quien enfrenta su pasado y descubre nuevos secretos mientras contin�a su entrenamiento como erudita; y Dalinar, quien debe enfrentar su propio pasado y sus errores mientras lidera a los ej�rcitos de Roshar. Juramentada profundiza en la compleja mitolog�a y los personajes de la serie, mientras que presenta una trama intrincada que se desarrolla a trav�s de m�ltiples puntos de vista. Adem�s, la serie contin�a explorando la compleja magia y la tecnolog�a de Roshar, incluyendo el uso de gemas y la manipulaci�n de la energ�a de la tormenta.'));
insert into libro (titulo, autor, descripcion) values('EL RITMO DE LA GUERRA','BRANDON SANDERSON',TO_CLOB('El ritmo de la guerra es el cuarto libro de la serie El Archivo de las Tormentas. La trama sigue a varios personajes principales, incluyendo a Kaladin, Shallan y Dalinar, mientras enfrentan los peligros y desaf�os que amenazan a Roshar. En este libro, se revelan secretos importantes de la historia de Roshar y la humanidad debe enfrentar una amenaza a�n mayor que nunca antes. La prosa de Sanderson es detallada y evocadora, y la serie presenta escenas de acci�n emocionantes y espectaculares. Adem�s, El ritmo de la guerra explora a�n m�s la compleja mitolog�a y los personajes de la serie, mientras que aborda temas profundos como la traici�n, el sacrificio y la lucha por la libertad.'));

--Inserci�n tabla seccion--
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Favoritos');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Siguiendo');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Finalizado');
INSERT INTO seccion (NOMBRE_SECCION) VALUES('Pendiente');

--Inserci�n tabla biblioteca_usuario--
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '1', '1');
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '2', '1');
insert into biblioteca_usuario (id_usuario, id_libro, id_seccion) values('1', '3', '2');

------------------------------------------Consultas------------------------------------------
--Libros--
SELECT libro.id, libro.titulo, libro.autor
FROM libro;

--Favoritos--Para los dem�s solo se cambia el nombre de la secci�n y la ID del usuario
SELECT libro.id, libro.titulo, libro.autor
FROM libro
INNER JOIN biblioteca_usuario ON libro.ID = biblioteca_usuario.id_libro
INNER JOIN seccion ON biblioteca_usuario.id_seccion = seccion.ID
WHERE biblioteca_usuario.id_usuario = 5 AND seccion.NOMBRE_SECCION = 'Favoritos'
ORDER BY libro.id;

SELECT COUNT(*) FROM biblioteca_usuario WHERE id_usuario = '1' AND id_libro = '3' AND id_seccion = '1';

------------------------------------------Comprobaci�n de tablas------------------------------------------
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