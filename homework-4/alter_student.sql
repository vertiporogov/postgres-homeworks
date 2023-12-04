-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

CREATE TABLE student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE student ADD COLUMN middle_name varchar

-- 3. Удалить колонку middle_name

ALTER TABLE student DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date

ALTER TABLE student RENAME birthday TO birthday_date

-- 5. Изменить тип данных колонки phone на varchar(32)

ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32)

-- 6. Вставить три любых записи с автогенерацией идентификатора

INSERT INTO student VALUES (1, 'FF', 'SD', '1980.01.17', '2763265'), (2, 'FFGGD', 'SDDDG', '1980.01.13', '27632DGDG65'), (3, 'FFFFFF', 'SFFFD', '1980.01.14', '2763DDD265')

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

TRUNCATE TABLE student RESTART IDENTITY
