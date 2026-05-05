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