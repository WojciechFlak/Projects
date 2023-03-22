-- Creation of task table
CREATE TABLE IF NOT EXISTS tasks (
  task_id SERIAL UNIQUE,
  task varchar(450) NOT NULL,
  deadline TIMESTAMP NOT NULL,
  added TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (task_id)
);
