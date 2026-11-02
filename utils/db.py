# utils/db.py
import pyodbc
import uuid
import datetime
import os

class Logger:
    def __init__(self, conn_str=None):
        self.conn_str = conn_str or os.getenv("DB_CONN_STR")

        if not self.conn_str:
            raise ValueError(
                "Nenhuma string de conexão definida. "
                "Verifique se o arquivo .env foi carregado "
                "e se DB_CONN_STR está configurada."
            )

    def log(self, session_id, user_input, assistant_output):
        """Insere um log na tabela Logs."""
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Logs (SessionId, Timestamp, UserInput, AssistantOutput)
                VALUES (?, GETUTCDATE(), ?, ?)
            """, session_id, user_input, assistant_output)
            conn.commit()