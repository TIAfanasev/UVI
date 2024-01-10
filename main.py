import os

os.system("postgresql-16.1-1-windows-x64.exe --unattendedmodeui minimal --mode unattended --disable-components pgAdmin --superaccount vs_test --superpassword 4100")

os.system("setx /M path \"%path%;C:\\Program Files\\PostgreSQL\\16\\bin\"")

os.system("SET PGPASSWORD=4100; pg_restore -U vs_test -c -C -d postgres dumb.sql")

os.system("wsl --install")

