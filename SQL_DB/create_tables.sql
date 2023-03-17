-- Creation of task table
CREATE TABLE IF NOT EXISTS tasks (
  task_id INT NOT NULL,
  task varchar(450) NOT NULL,
  deadline TIMESTAMP,
  PRIMARY KEY (task_id)
);
