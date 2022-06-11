use python_app_db;

insert into clients(name, phone_number) values
("Андрей", "79190372323"),
("Виктор", "79198313023"),
("Евгений", "79191667311");

insert into consoles(title) values
("Play Station 4"),
("X Box 360"),
("Nintendo Switch"),
("Playstation Portable"),
("Russian console");

insert into employees(name, password) values
("Андрей", "12345678");

insert into sales(console_id, client_id, employee_id) values
(1, 2, 1),
(1, 5, 1),
(3, 3, 1);