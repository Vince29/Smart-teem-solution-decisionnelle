CREATE DATABASE IF NOT EXISTS WRK;
CREATE DATABASE IF NOT EXISTS SOC;
CREATE DATABASE IF NOT EXISTS STG;


GRANT ALL PRIVILEGES ON DATABASE WRK TO ROLE SYSADMIN;
GRANT ALL PRIVILEGES ON DATABASE SOC TO ROLE SYSADMIN;
GRANT ALL PRIVILEGES ON DATABASE STG TO ROLE SYSADMIN;