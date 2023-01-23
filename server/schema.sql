DROP TABLE IF EXISTS serial_data;

CREATE TABLE serial_data(
    lat DECIMAL NOT NULL,
    lon DECIMAL NOT NULL,
    heading_deg DECIMAL NOT NULL,
    bearing_deg DECIMAL NOT NULL,
    range_ft DECIMAL NOT NULL,
    target_lat DECIMAL NOT NULL,
    target_lon DECIMAL NOT NULL,
    airspeed_fps DECIMAL NOT NULL,
    groundspeed_fps DECIMAL NOT NULL,
    theta_deg DECIMAL NOT NULL,
    phi_deg DECIMAL NOT NULL,
    gps_altitude_ft DECIMAL NOT NULL,
    baro_altitude_ft DECIMAL NOT NULL,
    bat_voltage_V DECIMAL NOT NULL,
    local_time DECIMAL NOT NULL,
    time_recorded DATETIME NOT NULL
)