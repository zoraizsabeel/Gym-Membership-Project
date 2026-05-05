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
