SELECT purchases.id, purchases.date, users.first_name, users.last_name
    FROM purchases
    JOIN users ON purchases.user_id = users.id;