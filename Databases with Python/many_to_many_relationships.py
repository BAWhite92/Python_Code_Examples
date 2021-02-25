#for many to many you need a JUNCTION TABLE
#models nothing but connection between two tables. So uses two many to one relationships.

#for example courses and users, users may be on many courses or a course may have many users so a middle table
#called member is used with 2 foreign keys that models what users id relates to what course id.
#can then use these foreign keys to get full data on user and courses that are linked.
#can use two primary keys (composite) for a table like this.

import sqlite3

#create Users
CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT,
    email   TEXT
)

#create course
CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT
)

#create junction table Member
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
        #show wether they are a teacher or a student
        role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)



INSERT INTO User (name, email) VALUES ('Jane', 'j@ou.co.uk');
INSERT INTO User (name, email) VALUES ('Ed', 'wick@ou.ac.uk');
INSERT INTO User (name, email) VALUES ('Ben', 'baw@ou.ac.uk');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('Java');
INSERT INTO Course (title) VALUES ('PHP');

#teacher = 1, students = 0
#entries for course 1
INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);
#entires for course 2
INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);
#entries for course 3
INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);


SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
#sorts a precedence so title > member(descending) > user
ORDER BY Course.title, Member.role DESC, User.name