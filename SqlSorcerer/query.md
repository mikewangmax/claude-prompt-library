# SQL Query: Customers With Orders But No Reviews

## Request

Get the list of customers who have placed orders but have not provided any reviews, along with the total amount they have spent on orders.

## Query

```sql
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    SUM(o.total_amount) AS total_spent
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Reviews r ON c.customer_id = r.customer_id
WHERE r.review_id IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
ORDER BY total_spent DESC;
```

## Explanation

Here's a breakdown of how this query works:

### 1. `INNER JOIN Orders o ON c.customer_id = o.customer_id`

This joins the `Customers` table with the `Orders` table, ensuring we only include customers who have **placed at least one order**. An `INNER JOIN` filters out any customer with no orders.

### 2. `LEFT JOIN Reviews r ON c.customer_id = r.customer_id`

This performs a `LEFT JOIN` with the `Reviews` table. A left join keeps all rows from the left side (customers who placed orders) and attaches any matching review rows. If a customer has **no reviews**, the review columns will be `NULL`.

### 3. `WHERE r.review_id IS NULL`

This is the key filter. By checking that `r.review_id IS NULL`, we isolate only those customers whose left join to `Reviews` found **no matching rows** — meaning they have never written a review.

### 4. `SUM(o.total_amount) AS total_spent`

Aggregates the `total_amount` across all of each customer's orders to produce their total spend.

### 5. `GROUP BY c.customer_id, c.first_name, c.last_name, c.email`

Groups the results per customer so the `SUM` aggregation produces one row per person.

### 6. `ORDER BY total_spent DESC`

Sorts the results so the highest-spending customers appear first, which is useful for identifying valuable customers who might benefit from a review prompt or follow-up engagement.

## Sample Output

| customer_id | first_name | last_name | email               | total_spent |
|-------------|-----------|-----------|---------------------|-------------|
| 12          | Sarah     | Mitchell  | sarah.m@example.com | 1,245.00    |
| 7           | James     | O'Brien   | jobrien@example.com | 890.50      |
| 23          | Maria     | Gonzalez  | mgonz@example.com   | 534.75      |