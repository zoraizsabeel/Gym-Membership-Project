CREATE TABLE Zipcodes (
    Zipcode VARCHAR(10) PRIMARY KEY NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(50) NOT NULL
);
CREATE TABLE MembershipPlans (
    PlanID INT PRIMARY KEY NOT NULL,
    PlanName VARCHAR(100) NOT NULL,
    DurationMonths INT NOT NULL,
    MonthlyFee DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Venues (
    VenueID INT PRIMARY KEY NOT NULL,
    VenueName VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Zipcode VARCHAR(10) NOT NULL REFERENCES Zipcodes(Zipcode)
);

CREATE TABLE Members (
	MemberID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    DOB DATE NOT NULL,
    JoinDate DATE NOT NULL,
    PlanID INT NOT NULL REFERENCES MembershipPlans(PlanID),
    Zipcode VARCHAR(10) NOT NULL REFERENCES Zipcodes(Zipcode)
);

CREATE TABLE Staff (
    StaffID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    Zipcode VARCHAR(10) NOT NULL REFERENCES Zipcodes(Zipcode)
);

CREATE TABLE Classes (
    ClassID INT PRIMARY KEY NOT NULL,
    ClassName VARCHAR(100) NOT NULL,
    StaffID INT NOT NULL REFERENCES Staff(StaffID),
    Schedule DATETIME NOT NULL,
    Capacity INT NOT NULL,
    VenueID INT NOT NULL REFERENCES Venues(VenueID)
);

CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID),
    ClassID INT NOT NULL REFERENCES Classes(ClassID),
    BookingDate DATE NOT NULL,
    Status VARCHAR(20) NOT NULL DEFAULT 'Confirmed'
);

CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY NOT NULL,
    MemberID INT NOT NULL REFERENCES Members(MemberID),
    Amount DECIMAL(10, 2) NOT NULL,
    PayDate DATE NOT NULL,
    Method VARCHAR(50) NOT NULL,
    Status VARCHAR(20) NOT NULL
);

-- Due to requirements asking for at least 15 rows in each table, we have populated the tables below

INSERT INTO Zipcodes (Zipcode, City, State) VALUES
('95112', 'San Jose', 'CA'),
('95126', 'San Jose', 'CA'),
('95128', 'San Jose', 'CA'),
('95110', 'San Jose', 'CA'),
('95113', 'San Jose', 'CA'),
('94102', 'San Francisco', 'CA'),
('94103', 'San Francisco', 'CA'),
('94105', 'San Francisco', 'CA'),
('94107', 'San Francisco', 'CA'),
('94109', 'San Francisco', 'CA'),
('94111', 'San Francisco', 'CA'),
('90001', 'Los Angeles', 'CA'),
('90002', 'Los Angeles', 'CA'),
('90210', 'Beverly Hills', 'CA'),
('92101', 'San Diego', 'CA'),
('92103', 'San Diego', 'CA'),
('93101', 'Santa Barbara', 'CA');

INSERT INTO MembershipPlans (PlanID, PlanName, DurationMonths, MonthlyFee) VALUES
(1, 'Basic Monthly', 1, 29.99),
(2, 'Basic Quarterly', 3, 26.66),
(3, 'Basic Annual', 12, 24.99),
(4, 'Premium Monthly', 1, 49.99),
(5, 'Premium Quarterly', 3, 44.99),
(6, 'Premium Annual', 12, 39.99),
(7, 'Student Monthly', 1, 19.99),
(8, 'Student Quarterly', 3, 17.99),
(9, 'Student Annual', 12, 15.99),
(10, 'Senior Monthly', 1, 22.99),
(11, 'Senior Annual', 12, 18.99),
(12, 'Day Pass', 0, 9.99),
(13, 'Week Pass', 0, 29.99),
(14, 'Corporate Monthly', 1, 39.99),
(15, 'Corporate Annual', 12, 34.99);

INSERT INTO Venues (VenueID, VenueName, Address, Zipcode) VALUES
(1, 'Downtown Fitness', '88 N 1st St', '95112'),
(2, 'Westside Gym', '310 Meridian Ave', '95126'),
(3, 'Eastside Rec Center', '1450 Blossom Hill Rd', '95128'),
(4, 'North Valley Gym', '720 Hostetter Rd', '95110'),
(5, 'Central Wellness', '400 W Santa Clara St', '95113'),
(6, 'SF Market St Gym', '101 Market St', '94102'),
(7, 'SoMa Fitness', '255 Folsom St', '94103'),
(8, 'Bay Club Embarcadero', '333 Spear St', '94105'),
(9, 'Mission Fitness', '3180 18th St', '94107'),
(10, 'Nob Hill Athletic', '1630 California St', '94109'),
(11, 'FiDi Gym', '580 California St', '94111'),
(12, 'LA Fitness Central', '800 S Figueroa St', '90001'),
(13, 'Hollywood Athletic', '6525 Sunset Blvd', '90002'),
(14, 'BH Sport Club', '9601 Wilshire Blvd', '90210'),
(15, 'SD Bayfront Gym', '1 Harbor Dr', '92101');

INSERT INTO Staff (StaffID, Name, Role, Email, Phone, Zipcode) VALUES
(1, 'Jason Mercer', 'Manager', 'j.mercer@gmms.com', '408-555-0191', '95112'),
(2, 'Talia Okonkwo', 'Trainer', 't.okonkwo@gmms.com', '408-555-0347', '95126'),
(3, 'Derek Huang', 'Trainer', 'd.huang@gmms.com', '408-555-0582', '95128'),
(4, 'Priya Nair', 'Yoga Instructor', 'p.nair@gmms.com', '408-555-0614', '95110'),
(5, 'Brandon Tills', 'Receptionist', 'b.tills@gmms.com', '408-555-0723', '95113'),
(6, 'Megan Castillo', 'Trainer', 'm.castillo@gmms.com', '415-555-0139', '94102'),
(7, 'Omar Shaikh', 'Manager', 'o.shaikh@gmms.com', '415-555-0267', '94103'),
(8, 'Anita Reyes', 'Spin Instructor', 'a.reyes@gmms.com', '415-555-0418', '94105'),
(9, 'Chris Baxter', 'Personal Trainer', 'c.baxter@gmms.com', '415-555-0593', '94107'),
(10, 'Lena Park', 'Nutritionist', 'l.park@gmms.com', '415-555-0672', '94109'),
(11, 'Marcus Webb', 'Trainer', 'm.webb@gmms.com', '415-555-0751', '94111'),
(12, 'Sofia Delgado', 'Pilates Instructor', 's.delgado@gmms.com', '213-555-0184', '90001'),
(13, 'Kevin Yoo', 'Manager', 'k.yoo@gmms.com', '213-555-0329', '90002'),
(14, 'Natalie Fong', 'Trainer', 'n.fong@gmms.com', '310-555-0461', '90210'),
(15, 'Darius Cole', 'Trainer', 'd.cole@gmms.com', '619-555-0537', '92101'),
(16, 'Isabelle Mora', 'Zumba Instructor', 'i.mora@gmms.com', '619-555-0618', '92103'),
(17, 'Ryan Tran', 'Receptionist', 'r.tran@gmms.com', '805-555-0742', '93101');

INSERT INTO Members (MemberID, Name, Email, Phone, DOB, JoinDate, PlanID, Zipcode) VALUES
(1, 'Jordan Lee', 'jordan.lee@gmail.com', '408-555-2031', '1997-06-14', '2024-01-08', 4, '95112'),
(2, 'Maya Patel', 'mayap92@gmail.com', '408-555-2178', '1992-03-27', '2024-01-22', 1, '95126'),
(3, 'Ethan Brooks', 'ebrooks@outlook.com', '408-555-2254', '2001-11-03', '2024-02-05', 7, '95128'),
(4, 'Chloe Nguyen', 'chloe.n@gmail.com', '408-555-2390', '1988-08-19', '2024-02-14', 3, '95110'),
(5, 'Amir Hassan', 'amir.h@yahoo.com', '408-555-2467', '1994-01-30', '2024-02-28', 5, '95113'),
(6, 'Samira Wolfe', 'samira.w@gmail.com', '415-555-2512', '1985-05-11', '2024-03-09', 2, '94102'),
(7, 'Tyler Nguyen', 'tylern@gmail.com', '415-555-2643', '1999-09-22', '2024-03-17', 6, '94103'),
(8, 'Linda Osei', 'l.osei@gmail.com', '415-555-2729', '1972-12-05', '2024-03-25', 10, '94105'),
(9, 'Kai Yamamoto', 'kai.yama@gmail.com', '415-555-2815', '2002-04-17', '2024-04-03', 7, '94107'),
(10, 'Rachel Torres', 'rachel.t@outlook.com', '415-555-2961', '1991-07-08', '2024-04-11', 4, '94109'),
(11, 'Marcus Green', 'm.green@gmail.com', '415-555-3074', '1986-02-14', '2024-04-19', 6, '94111'),
(12, 'Priya Shah', 'priya.shah@gmail.com', '213-555-3118', '1995-10-29', '2024-05-02', 1, '90001'),
(13, 'Noah Kim', 'noahk01@gmail.com', '213-555-3247', '2003-01-16', '2024-05-13', 7, '90002'),
(14, 'Vanessa Cruz', 'v.cruz@yahoo.com', '310-555-3389', '1979-06-04', '2024-05-21', 3, '90210'),
(15, 'Dani Russo', 'dani.russo@gmail.com', '619-555-3452', '1993-03-08', '2024-06-06', 5, '92101'),
(16, 'Harold Simms', 'harold.s@gmail.com', '619-555-3561', '1967-09-21', '2024-06-14', 11, '92103'),
(17, 'Zoe Bennett', 'zoe.b@gmail.com', '805-555-3677', '2000-12-31', '2024-06-23', 7, '93101'),
(18, 'Andre Williams', 'andre.w@gmail.com', '408-555-3784', '1990-05-17', '2024-07-04', 4, '95112'),
(19, 'Fatima Al-Amin', 'fatima.a@outlook.com', '408-555-3892', '1983-08-09', '2024-07-11', 14, '95126'),
(20, 'Liam Castro', 'liam.c@gmail.com', '408-555-3945', '1998-02-25', '2024-07-19', 6, '95128');