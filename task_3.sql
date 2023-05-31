SELECT users.id, users.first_name, users.last_name, books.title
    FROM users
    LEFT JOIN purchases ON users.id = purchases.user_id
    LEFT JOIN books ON purchases.book_id = books.id
    ORDER BY users.id;
