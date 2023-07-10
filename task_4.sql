 1. запит, який для кожного user порахує суму всіх покупок

SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases
    FROM users
    LEFT JOIN purchases ON users.id = purchases.user_id
    LEFT JOIN books ON purchases.book_id = books.id
    GROUP BY users.id, users.first_name, users.last_name;


 2. запит, який виведе кількість покупок книжок для кожного user

SELECT users.id, COUNT(purchases.id) AS purchases_count
    FROM users
    LEFT JOIN purchases ON users.id = purchases.user_id
    GROUP BY users.id;


 3. запит, який виведе кількість покупок книжок для автора Rowling

SELECT COUNT(purchases.id) AS amount
    FROM authors
    JOIN books ON authors.id = books.author_id
    JOIN purchases ON books.id = purchases.book_id
    WHERE authors.name = 'Rowling';


 4. запит, який виведе загальні суми продажів для кожного автора та кількість покупок.

SELECT authors.id, authors.name, SUM(books.price) AS total_sales, COUNT(purchases.id) AS purchase_count
    FROM authors
    JOIN books ON authors.id = books.author_id
    JOIN purchases ON books.id = purchases.book_id
    GROUP BY authors.id, authors.name;


5. запит, який виведе всі назви книжок із кількістю їх продажів в порядку спадання кількості продажів.

SELECT books.title, COUNT(purchases.id) AS sales_count
    FROM books
    LEFT JOIN purchases ON books.id = purchases.book_id
    GROUP BY books.title
    ORDER BY sales_count DESC;