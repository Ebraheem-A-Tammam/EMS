CREATE TABLE course(
    name            VARCHAR(50),
    doc             VARCHAR(20),
    code            VARCHAR(20)
);

CREATE TABLE doctors(
    name            VARCHAR(50),
    email           VARCHAR(50),
    password        VARCHAR(50),
    id              VARCHAR(20)
);

CREATE TABLE students(
    name            VARCHAR(50),
    email           VARCHAR(50),
    password        VARCHAR(50),
    id              VARCHAR(20)
);

CREATE TABLE teaching(
    doctor_id       VARCHAR(20),
    course_id       VARCHAR(20)
);

CREATE TABLE enrollment(
    student_id      VARCHAR(20),
    course_id       VARCHAR(20)
);

CREATE TABLE timeline(
    post_id         VARCHAR(20),
    publisher       VARCHAR(50),
    publisher_id    VARCHAR(20),
    publisher_name  VARCHAR(50),
    post            TEXT,
    created_at      DATETIME
);

CREATE TABLE replies(
    post_id         VARCHAR(20),
    publisher       VARCHAR(50),
    reply           TEXT,
    created_at      DATETIME,
);