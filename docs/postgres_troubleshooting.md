# Postgres Slow Query Troubleshooting

1. **Gather Query Stats**
   - Run `EXPLAIN (ANALYZE, BUFFERS) <your_query>;`
   - Look for sequential scans, nested loops on large tables, or high buffer usage.

2. **Check Indexes**
   - Ensure columns in WHERE, JOIN, or ORDER BY clauses are indexed.
   - For composite queries, consider multi-column indexes.

3. **Vacuum and Analyze**
   - `VACUUM (FULL)` in off-peak hours if you suspect table bloat.
   - `ANALYZE` keeps statistics updated to help the optimizer.

4. **Refactor or Partition**
   - Break down complex queries.
   - Partition large tables by date or other relevant key.

5. **Hardware and Config**
   - Check if CPU, memory, or IO is a bottleneck.
   - Tune `shared_buffers`, `work_mem`, etc., as needed.

6. **Further Reading**
   - [PostgreSQL Docs](https://www.postgresql.org/docs/) for advanced configuration tips.