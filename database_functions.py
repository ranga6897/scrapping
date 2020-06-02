


def create_table(con):

    # con = lite.connect('price_details.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS data")

        cur.execute(
            "CREATE TABLE data(id INT, subcategory TEXT, subsubcatergory TEXT, brand TEXT,product TEXT,barcode INT,builders_sku INT NULL,leroy_sku INT,buco_sku INT,cashbuild_sku INT,builders_price INT,leroy_price INT,buco_price INT,cashbuild_price INT)")

        data = (
            (1, 'Cement', '42,5', 'NPC', 'NPC 42.5N Plus Cement - Black (50kg)', 6006077000022, 627935, None, 1203434, None,
             None, None, None, None),
            (2, 'Cement', '32,5', 'NPC', 'NPC 32.5N Plus Cement - Blue (50kg)', 6009194412396, 627940, None, 1161188, None,
             None, None, None, None),
            (3, 'Cement', '42,5', 'PPC', 'PPC Surebuild 42.5N Cement (50kg)', 6003543000326, 627933, None, 1016533, None,
             None, None, None, None),
            (4, 'Cement', '52,5', 'PPC', 'PPC Surebuild 52.5N Cement (50kg)', 6009161768846, 639106, None, None, None, None,
             None, None, None),
            (
            5, 'Cement', '32,5', 'PPC', 'PPC Surebuild 32.5N Cement (50kg)', 6009149254088, 517797, 81424182, 1313309, None,
            None, None, None, None),
            (6, 'Cement', '32,5', 'Sephaku', 'Sephaku 32.5N Building Cement (50kg)', 6009194458998, 634913, None, 1255586,
             303275, None, None, None, None),
            (
            7, 'Cement', '42,5', 'Sephaku', 'Sephaku 42.5N Cement (50kg)', 6009149549979, 627953, None, 1231008, None, None,
            None, None, None),
            (8, 'Cement', '32,5', 'Builders Pride', 'Builders Pride General Purpose Cement (50kg)', 6009194608171, 655546,
             None, None, None, None, None, None, None),
            (9, 'Cement', '32,5', 'KBC', 'KBC Cement 32.5N (50kg)', 7000083855206, None, 81412024, None, None, None, None,
             None, None),
            (10, 'Cement', '42,5', 'Afrisam', 'Afrisam Cement 42.5N (50kg) ALL PURPOSE', 6009601580410, None, 81422547,
             1179899, None, None, None, None, None),
            (11, 'Cement', '42,5', 'KBC', 'KBC Cement 42.5N (50kg)', 6009210005076, None, 81412025, None, None, None, None,
             None, None),
            (12, 'Cement', '32,5', 'Afrisam', 'Afrisam Cement 32.5N (50kg) STARBUILD', 6009601580731, None, 81422548,
             1291750, None, None, None, None, None),
            (13, 'Cement', '42,5', 'Lafarge', 'Lafarge Cement 42.5N BUILDCRETE (50kg)', 6009210018809, None, 81437685, None,
             None, None, None, None, None),
            (14, 'Cement', '32,5', 'Lafarge', 'Lafarge Cement 32.5N DURABUILD (50kg)', 6009210018793, None, 81437684,
             1035145, None, None, None, None, None),
            (15, 'Cement', '42,5', 'Champion', 'Champion Cement 42,5N (50kg)', None, None, None, None, 305661, None, None,
             None, None)

        )

        cur.executemany("INSERT INTO data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)

#
# def get_data_from_database(con):
#
#     # con = lite.connect('price_details.db')
#     cur = con.cursor()
#     cur.execute("SELECT * from data")
#     data_all = cur.fetchall()
#     cur.execute('PRAGMA table_info(data)')
#     data_columns = cur.fetchall()
#
#     return data_all,data_columns

def updateMultipleRecords(recordList,con):
    try:
        sqliteConnection = con
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_update_query = """Update data set builders_price = ?,leroy_price=?,buco_price=?,cashbuild_price = ? where id = ?"""
        cursor.executemany(sqlite_update_query, recordList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records updated successfully")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update multiple records of sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")
