use modmyride;

CREATE TABLE Users (
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (email)
);

insert into users value ('test@gmail.com', ' ', ' ');

CREATE TABLE if not exists makes (
    make_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE if not exists Models (
    make_name VARCHAR(255),
    model_name VARCHAR(255) PRIMARY KEY,
    model_info varchar(1000),
    FOREIGN KEY (make_name) REFERENCES makes(make_name)
);

CREATE TABLE if not exists Years (
	id int auto_increment primary key,
	make_name varchar(255),
    model_name VARCHAR(255),
    year INT,
    FOREIGN KEY (model_name) REFERENCES models(model_name),
    foreign key (make_name) REFERENCES makes(make_name)
);

insert into make_names values ('Toyota');
insert into make_names values ('Honda');
insert into make_names values ('Ford');

insert into models values ('Toyota', 'Camry', 
'The Toyota Camry is a Japanese Mid-size vehicle manufactured by Toyota since 1982. The Camry has been the best selling car in the United States for eight of the last nine years starting in 1997. The Camry name comes from the English phonetic of the Japanese word "Kammuri," which means "Crown."');

insert into models values ('Toyota', 'Corolla', 
'The Toyota Corolla is a compact car produced by Toyota of Japan, known worldwide for its reliability, conventional engineering, and low fuel consumption. In 1997, the Corolla became the best selling nameplate in the world.');

insert into models values ('Toyota', 'RAV4', 
'The Toyota RAV4 (Japanese: トヨタ・RAV4, Hepburn: Toyota Ravufō) is a compact crossover SUV produced by the Japanese automobile manufacturer Toyota. Considered the first ever compact crossover SUV, it made its debut in Japan and Europe in 1994, and in North America in 1995, being launched in January 1996.');

insert into models values ('Honda', 'Civic', 
'The Honda Civic (Japanese: ホンダ・シビック, Hepburn: Honda Shibikku) is a series of automobiles manufactured by Honda since 1972. Since 2000, the Civic has been categorized as a compact car, while previously it occupies the subcompact class. As of 2021, the Civic is positioned between the Honda Fit/City and Honda Accord in Honda''s global car line-up.');

insert into models values ('Honda', 'Accord', 
'Honda''s flagship in the U.S., the Accord is one of the best selling, best reviewed mid size sedans ever sold. Introduced in 1976, the Accord was the best-selling Japanese vehicle in the U.S. for 15 years from 1982 to 1997. In 1982, the Accord became the first Japanese car to be produced in the U.S. when production commenced in Marysville, Ohio.');

insert into models values ('Honda', 'CRV', 
'The Honda CR-V is a Crossover SUV manufactured by the Japanese automake_namer Honda since 1996 and introduced in the North American market in 1997. It uses the Civic platform with an SUV body design. The CR-V is Honda''s mid-range utility vehicle, slotting between the smaller HR-V and the larger North American market Passport/Pilot.');

insert into models values ('Ford', 'Mustang', 
'The Ford Mustang is an American automobile, originally based on the Ford Falcon compact. The first production Mustang, a white convertible with red interior rolled off the assembly line in Dearborn, Michigan on March 9, 1964. Introduced to the public at the New York World''s Fair on April 17, 1964, and via all three American television networks on April 19, it was the most successful product launch in automotive history, letting off near-pandemonium at Ford dealers across the continent.');

insert into models values ('Ford', 'F150', 
'The F-Series is a series of trucks from Ford Motor Company that have been sold for over now 6 decades. The most popular variant of the F-Series is the F-150, a full-size pickup truck. It has been the best-selling vehicle in the world for 36 years and the best-selling truck in the United States (and possibly the world) for 36 years. Analysts estimate that the F-Series alone make_names up half of the Ford Motor Company''s profits in recent years, the number of F-series sold in canada in 2020 was 131 000 unity.');

insert into models values ('Ford', 'Explorer', 
'The Ford Explorer is a mid-size sport utility vehicle sold mostly in North America built by the Ford Motor Company since 1990 and still in production as of 2009. It is manufactured in Louisville, Kentucky (it was also assembled in Hazelwood, Missouri until the plant closed on March 10, 2006). It has been the best-selling vehicle midsize SUV in the United States each year since its introduction, and is one of the vehicles instrumental in turning the SUV from a special-interest vehicle into one of the most popular vehicle types on the road.');

insert into years (make_name, model_name, year) values ('Honda', 'Accord', 2020);
insert into years (make_name, model_name, year) values ('Honda', 'Accord', 2021);
insert into years (make_name, model_name, year) values ('Honda', 'Accord', 2022);
insert into years (make_name, model_name, year) values ('Honda', 'Accord', 2023);
insert into years (make_name, model_name, year) values ('Honda', 'Accord', 2024);

insert into years (make_name, model_name, year) values ('Honda', 'Civic', 2020);
insert into years (make_name, model_name, year) values ('Honda', 'Civic', 2021);
insert into years (make_name, model_name, year) values ('Honda', 'Civic', 2022);
insert into years (make_name, model_name, year) values ('Honda', 'Civic', 2023);
insert into years (make_name, model_name, year) values ('Honda', 'Civic', 2024);

insert into years (make_name, model_name, year) values ('Honda', 'CRV', 2020);
insert into years (make_name, model_name, year) values ('Honda', 'CRV', 2021);
insert into years (make_name, model_name, year) values ('Honda', 'CRV', 2022);
insert into years (make_name, model_name, year) values ('Honda', 'CRV', 2023);
insert into years (make_name, model_name, year) values ('Honda', 'CRV', 2024);

insert into years (make_name, model_name, year) values ('Toyota', 'Camry', 2020);
insert into years (make_name, model_name, year) values ('Toyota', 'Camry', 2021);
insert into years (make_name, model_name, year) values ('Toyota', 'Camry', 2022);
insert into years (make_name, model_name, year) values ('Toyota', 'Camry', 2023);
insert into years (make_name, model_name, year) values ('Toyota', 'Camry', 2024);

insert into years (make_name, model_name, year) values ('Toyota', 'Corolla', 2020);
insert into years (make_name, model_name, year) values ('Toyota', 'Corolla', 2021);
insert into years (make_name, model_name, year) values ('Toyota', 'Corolla', 2022);
insert into years (make_name, model_name, year) values ('Toyota', 'Corolla', 2023);
insert into years (make_name, model_name, year) values ('Toyota', 'Corolla', 2024);

insert into years (make_name, model_name, year) values ('Toyota', 'RAV4', 2020);
insert into years (make_name, model_name, year) values ('Toyota', 'RAV4', 2021);
insert into years (make_name, model_name, year) values ('Toyota', 'RAV4', 2022);
insert into years (make_name, model_name, year) values ('Toyota', 'RAV4', 2023);
insert into years (make_name, model_name, year) values ('Toyota', 'RAV4', 2024);

insert into years (make_name, model_name, year) values ('Ford', 'Explorer', 2020);
insert into years (make_name, model_name, year) values ('Ford', 'Explorer', 2021);
insert into years (make_name, model_name, year) values ('Ford', 'Explorer', 2022);
insert into years (make_name, model_name, year) values ('Ford', 'Explorer', 2023);
insert into years (make_name, model_name, year) values ('Ford', 'Explorer', 2024);

insert into years (make_name, model_name, year) values ('Ford', 'F150', 2020);
insert into years (make_name, model_name, year) values ('Ford', 'F150', 2021);
insert into years (make_name, model_name, year) values ('Ford', 'F150', 2022);
insert into years (make_name, model_name, year) values ('Ford', 'F150', 2023);
insert into years (make_name, model_name, year) values ('Ford', 'F150', 2024);

insert into years (make_name, model_name, year) values ('Ford', 'Mustang', 2020);
insert into years (make_name, model_name, year) values ('Ford', 'Mustang', 2021);
insert into years (make_name, model_name, year) values ('Ford', 'Mustang', 2022);
insert into years (make_name, model_name, year) values ('Ford', 'Mustang', 2023);
insert into years (make_name, model_name, year) values ('Ford', 'Mustang', 2024);

-- Wheels Table
CREATE TABLE Wheels (
wheel_id INT AUTO_INCREMENT PRIMARY KEY,
wheel_name VARCHAR(255) NOT NULL,
wheel_size INT
);

INSERT INTO Wheels (wheel_name, wheel_size) VALUES
('Enkei RPF1', 18),
('BBS RS', 19),
('Volk TE37', 17),
('Rotiform BLQ', 20);

-- Decals Table
CREATE TABLE Decals (
decal_id INT AUTO_INCREMENT PRIMARY KEY,
decal_name VARCHAR(255) NOT NULL,
decal_size VARCHAR(50)
);

INSERT INTO Decals (decal_name, decal_size) VALUES
('Tribal Flames', 'Medium'),
('Skull and Crossbones', 'Small'),
('Racing Stripes', 'Large'),
('Dragon', 'Medium');

-- Vinyl Wrap Table
CREATE TABLE VinylWrap (
wrap_id INT AUTO_INCREMENT PRIMARY KEY,
wrap_name VARCHAR(255) NOT NULL,
wrap_color VARCHAR(50),
wrap_material VARCHAR(50)
);

INSERT INTO VinylWrap (wrap_name, wrap_color, wrap_material) VALUES
('Matte Black', 'Black', 'Vinyl'),
('Glossy White', 'White', 'Vinyl'),
('Carbon Fiber', 'Black', 'Carbon Fiber'),
('Satin Red', 'Red', 'Vinyl');

-- LED Lighting
CREATE TABLE LEDLighting (
lighting_id INT AUTO_INCREMENT PRIMARY KEY,
lighting_name VARCHAR(255) NOT NULL,
lighting_type VARCHAR(50),
lighting_color VARCHAR(50)
);

INSERT INTO LEDLighting (lighting_name, lighting_type, lighting_color) VALUES
('Underbody LED Kit', 'Underbody', 'RGB'),
('Interior LED Strips', 'Interior', 'White'),
('Headlight LED Bulbs', 'Headlight', 'Blue'),
('Taillight LED Conversion', 'Taillight', 'Red');

-- Additional Mods Table
CREATE TABLE AdditionalMods (
mod_id INT AUTO_INCREMENT PRIMARY KEY,
mod_name VARCHAR(255) NOT NULL
);

INSERT INTO AdditionalMods (mod_name) VALUES
('CarPlay Integration'),
('Bluetooth OBD2 Scanner'),
('Dash Cam'),
('Radar Detector'),
('Wireless Phone Charger'),
('Custom License Plate Frame'),
('Cup Holder Organizer');