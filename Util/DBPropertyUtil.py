class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-P8QAI2N\SQLEXPRESS"
        database_name = "payXpert"
        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )
        return conn_str
