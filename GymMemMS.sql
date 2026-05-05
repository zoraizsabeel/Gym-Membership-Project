CREATE TABLE Zipcodes (
    Zipcode VARCHAR(10) PRIMARY KEY,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(50) NOT NULL
);
CREATE TABLE MembershipPlans (
    PlanID INT PRIMARY KEY,
    PlanName VARCHAR(100) NOT NULL,
    DurationMonths INT NOT NULL,
    MonthlyFee DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Venues (
    VenueID INT PRIMARY KEY,
    VenueName VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Zipcode VARCHAR(10) REFERENCES Zipcodes(Zipcode)
);

CREATE TABLE Members (
	MemberID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    DOB DATE,
    JoinDate DATE NOT NULL,
    PlanID INT REFERENCES MembershipPlans(PlanID),
    Zipcode VARCHAR(10) REFERENCES Zipcodes(Zipcode)
);
