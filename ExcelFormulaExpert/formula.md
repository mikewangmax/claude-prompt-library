# Excel Formula: Salesperson Sales by Category and Month

## Formula

```excel
=SUMIFS(C:C, A:A, "John Smith", B:B, "Electronics", D:D, ">="&DATE(2024,1,1), D:D, "<="&DATE(2024,1,31))
```

## Data Layout

| Column | Content |
|---|---|
| A | Salesperson Name |
| B | Product Category |
| C | Sales Amount |
| D | Date of Sale |

## Arguments Breakdown

| Argument | Purpose |
|---|---|
| `C:C` | Sum range — the sales amounts |
| `A:A, "John Smith"` | Criteria 1 — match salesperson name |
| `B:B, "Electronics"` | Criteria 2 — match product category |
| `D:D, ">="&DATE(2024,1,1)` | Criteria 3 — date on or after Jan 1 |
| `D:D, "<="&DATE(2024,1,31)` | Criteria 4 — date on or before Jan 31 |
