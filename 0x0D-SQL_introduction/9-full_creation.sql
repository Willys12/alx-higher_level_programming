-- Creates a new table with new items.
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "JOHN", 10),
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "ALEX", 3),
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "BOB", 14),
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "GEORGE", 8);
