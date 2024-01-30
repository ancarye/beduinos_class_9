**SELECT (Proyección):**
   - SQL: `SELECT columna1, columna2 FROM tabla WHERE condición;`
   - Pandas: `df[['columna1', 'columna2']].query('condición')`

   Ejemplo:
   ```python
   df[['Nombre', 'Edad']].query('Edad > 25')
   ```

2. **WHERE (Filtrado):**
   - SQL: `SELECT * FROM tabla WHERE condición;`
   - Pandas: `df[df['condición']]`

   Ejemplo:
   ```python
   df[df['Edad'] > 25]
   ```

3. **GROUP BY y AGGREGATE (Agrupación y Agregación):**
   - SQL: `SELECT columna1, COUNT(*), AVG(columna2) FROM tabla GROUP BY columna1;`
   - Pandas: `df.groupby('columna1').agg({'columna2': ['count', 'mean']})`

   Ejemplo:
   ```python
   df.groupby('Departamento').agg({'Salario': ['count', 'mean']})
   ```

4. **ORDER BY (Ordenamiento):**
   - SQL: `SELECT * FROM tabla ORDER BY columna DESC;`
   - Pandas: `df.sort_values(by='columna', ascending=False)`

   Ejemplo:
   ```python
   df.sort_values(by='Ingresos', ascending=False)
   ```

5. **JOIN (Combinación de tablas):**
   - SQL: `SELECT * FROM tabla1 INNER JOIN tabla2 ON tabla1.columna = tabla2.columna;`
   - Pandas: `pd.merge(df1, df2, on='columna', how='inner')`

   Ejemplo:
   ```python
   pd.merge(df_empleados, df_departamentos, on='DepartamentoID', how='inner')
   ```

6. **LIKE (Búsqueda de patrones):**
   - SQL: `SELECT * FROM tabla WHERE columna LIKE 'patrón%';`
   - Pandas: `df[df['columna'].str.startswith('patrón')]`

   Ejemplo:
   ```python
   df[df['Nombre'].str.startswith('A')]
   ```