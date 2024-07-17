-- Active: 1663945334496@@127.0.0.1@3306@pythonCourse
CREATE Table testTable(
    id BIGINT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(50),
    user_age TINYINT UNSIGNED,
    price FLOAT UNSIGNED,
    user_comment TEXT,
    smoker ENUM('yes','no'),
    PRIMARY KEY(id)
);


DROP Table `testTable`


alter table `testTable`
add column `id` BIGINT;
add column `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP;
-- add column `mofified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE `testTable` ADD PRIMARY KEY(id);




-- -- insert 1 row into all columns
-- INSERT INTO `testTable` VALUES ('Ada', 50, 34.5,'','yes');
INSERT INTO `testTable` (user_name, price, user_age) VALUES
('Pesho', 34.5, 34);


-- Drop all rows, where `user_name` is null:
-- DELETE FROM `testTable` WHERE user_name IS NULL;


-- Update Pesho's age =35
UPDATE `testTable`
SET user_age=35
WHERE user_name='Pesho';

ALTER TABLE `testTable` ADD INDEX(`price`);