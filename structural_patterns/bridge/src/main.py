import database
import scrapper

if __name__ == "__main__":

    credentials = database.Credentials(db="db", user="user", password="password", host="host", port="port")

    postgres_db = database.PostgreSql(credentials=credentials)
    maria_db = database.MariaSql(credentials=credentials)

    wind_direction_var = "WTUR.WiDir"
    wind_speed_var = "WTUR.WiSpeed"

    wind_dir_scrapper_postgres = scrapper.WindDir(variable=wind_direction_var, db=postgres_db)
    wind_dir_scrapper_maria = scrapper.WindSpeed(variable=wind_speed_var, db=maria_db)

    print(wind_dir_scrapper_postgres.scrap_time_period(0, 1))
    print(wind_dir_scrapper_maria.scrap_time_period(0, 1))

