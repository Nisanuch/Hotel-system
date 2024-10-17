import psycopg2

class Client:

    """Создает класс c клиентами (Creates a class for clients)."""

    def __init__(self, surname, name, patronymic, id, entrance_date, num_days, level_room, room_number, points):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.id = id
        self.entrance_date = entrance_date
        self.num_days = num_days
        self.level_room = level_room
        self.room_number = room_number
        self.points = points
        self.connection = self.create_connection()

    def create_connection(self):
        """Создает соединение с базой данных PostgreSQL (Creates a connection to the PostgreSQL database)."""
        try:
            connection = psycopg2.connect(
                dbname="clientsb",
                user="user",
                password="qwerty",
                host="localhost",
                port="5432"
            )
            return connection
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

    def create_table(self):
        """Создает таблицу клиентов, если она не существует (Creates clients table if it does not exist)."""
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    surname VARCHAR(50),
                    name VARCHAR(50),
                    patronymic VARCHAR(50),
                    entrance_date DATE,
                    num_days INT,
                    level_room VARCHAR(50),
                    room_number INT,
                    points INT
                )
                """)

    def add_client(self):
        """Добавляет клиента в базу данных (Adds a client to the database)."""
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO clients (surname, name, patronymic, entrance_date, num_days, level_room, room_number, points)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (self.surname, self.name, self.patronymic, self.entrance_date, self.num_days, self.level_room, self.room_number, self.points))

    def get_client(self, client_id):
        """Получает информацию о клиенте по ID (Retrieves client information by ID)."""
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * FROM clients WHERE id = %s", (client_id,))
                client = cursor.fetchone()
                return client

client1 = Client("Жабраилов", "Амирхан", "Русланович", 585940, "02.04.2024", 7, 2, 101, 100)
client2 = Client("Прунцова", "Алиса", "Сергеевна", 22, "02.04.2024", 7, 2, 101, 100)
